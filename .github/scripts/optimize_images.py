#!/usr/bin/env python3
"""把 assets/ 裡過大的圖壓到適合網頁的大小。

GitHub Pages 的 deploy 在 syncing_files 有 10 分鐘上限，網站本體幾乎
全是原圖。這支腳本做的事：

- 寬度超過 2000px 的圖，等比例縮到 2000px。
- 不透明的大圖存成 progressive JPEG（quality 85，4:2:0）。
  真的有透明像素的 PNG 維持 PNG，只縮圖並重新壓縮。
- 檔名從 .png 改成 .jpg 時，一併改文章、API JSON、HTML 裡的路徑。
  只換檔名，不改句子。
- 已經壓過的 JPEG 會帶一個 COM 註記，再跑一次不會重壓（避免一代比一代糊）。

不會參與 Jekyll / pages-build-deployment。Pages 仍直接發布 repo 裡的檔案。
新圖要維持小檔，請在 commit 前跑這支腳本。CI 用 --check 擋下超寬或超過 1MB 的圖。

    pip install pillow
    python3 .github/scripts/optimize_images.py
    python3 .github/scripts/optimize_images.py --check
"""

from __future__ import annotations

import io
import re
import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.stderr.write("需要 Pillow：pip install pillow\n")
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "assets"

MAX_WIDTH = 2000
# 超過這個大小就值得重壓。已經很小的 icon 不要轉成 JPEG。
MIN_BYTES = 200_000
# CI 與腳本共同的上限。quality 85 仍超過時會往下調到 70。
MAX_BYTES = 1_000_000
JPEG_QUALITY = 85
MARKER = "mw-imgopt-q85-w2000"

SKIP_DIRS = {
    ".git",
    "_site",
    "vendor",
    "node_modules",
    ".bundle",
    ".jekyll-cache",
    ".sass-cache",
    "__pycache__",
}
SKIP_TEXT_EXT = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".svg",
    ".ico",
    ".woff",
    ".woff2",
    ".ttf",
    ".eot",
    ".zip",
    ".gz",
    ".pdf",
    ".mp4",
}

IMAGE_EXT = {".png", ".jpg", ".jpeg"}


def has_marker(im: Image.Image) -> bool:
    comment = im.info.get("comment")
    if comment is None:
        return False
    if isinstance(comment, str):
        comment = comment.encode()
    return MARKER.encode() in comment


def uses_alpha(im: Image.Image) -> bool:
    if im.mode in ("RGBA", "LA"):
        alpha = im.getchannel("A")
        lo, hi = alpha.getextrema()
        if lo == 255:
            return False
        hist = alpha.histogram()
        total = sum(hist) or 1
        if hist[255] / total > 0.995 and lo > 250:
            return False
        return True
    if im.mode == "P" and "transparency" in im.info:
        return True
    return False


def fit_width(im: Image.Image) -> Image.Image:
    if im.width <= MAX_WIDTH:
        return im
    height = max(1, round(im.height * MAX_WIDTH / im.width))
    return im.resize((MAX_WIDTH, height), Image.Resampling.LANCZOS)


def encode_jpeg(im: Image.Image, icc: bytes | None, quality: int) -> bytes:
    buf = io.BytesIO()
    kwargs = {
        "quality": quality,
        "optimize": True,
        "progressive": True,
        "subsampling": 2,
        "comment": MARKER,
    }
    if icc:
        kwargs["icc_profile"] = icc
    im.convert("RGB").save(buf, "JPEG", **kwargs)
    return buf.getvalue()


def encode_png(im: Image.Image) -> bytes:
    buf = io.BytesIO()
    im.save(buf, "PNG", optimize=True, compress_level=9)
    return buf.getvalue()


def best_jpeg(im: Image.Image, icc: bytes | None) -> bytes:
    chosen = encode_jpeg(im, icc, JPEG_QUALITY)
    if len(chosen) <= MAX_BYTES:
        return chosen
    for quality in (80, 75, 70):
        data = encode_jpeg(im, icc, quality)
        chosen = data
        if len(data) <= MAX_BYTES:
            return data
    return chosen


def iter_images():
    for path in sorted(ASSETS.rglob("*")):
        if path.is_file() and path.suffix.lower() in IMAGE_EXT:
            yield path


def open_image(path: Path) -> Image.Image:
    im = Image.open(path)
    im.load()
    transposed = ImageOps.exif_transpose(im)
    return transposed if transposed is not None else im


class Rewrite:
    def __init__(self, old_base: str, new_base: str):
        self.old_base = old_base
        self.new_base = new_base


def plan_image(path: Path) -> tuple[bytes | None, str, tuple[int, int], tuple[int, int]]:
    """回傳 (新檔內容或 None, 副檔名含點, 原尺寸, 新尺寸)。

    內容為 None 代表這張圖維持不動。
    """
    original_size = path.stat().st_size
    im = open_image(path)
    old_wh = (im.width, im.height)
    icc = im.info.get("icc_profile")
    if isinstance(icc, str):
        icc = icc.encode()

    fitted = fit_width(im)
    resized = fitted.size != im.size
    new_wh = (fitted.width, fitted.height)
    ext = path.suffix.lower()

    if ext in (".jpg", ".jpeg") and has_marker(im) and not resized:
        return None, ext, old_wh, new_wh
    if not resized and original_size <= MIN_BYTES:
        return None, ext, old_wh, new_wh

    alpha = uses_alpha(fitted)
    if alpha:
        if not resized and original_size <= MAX_BYTES:
            return None, ext, old_wh, new_wh
        png = encode_png(fitted)
        if resized or len(png) < original_size * 0.90:
            return png, ".png", old_wh, new_wh
        return None, ext, old_wh, new_wh

    jpeg = best_jpeg(fitted, icc)
    if ext == ".png":
        # 小而只是略超寬的圖，JPEG 不一定比較小。比較縮圖後的 PNG。
        if len(jpeg) < original_size * 0.90 or (resized and len(jpeg) <= original_size):
            return jpeg, ".jpg", old_wh, new_wh
        if resized:
            png = encode_png(fitted)
            if len(png) < len(jpeg) and len(png) < original_size * 1.05:
                return png, ".png", old_wh, new_wh
            return jpeg, ".jpg", old_wh, new_wh
        return None, ext, old_wh, new_wh

    if resized or len(jpeg) < original_size * 0.90 or original_size > MAX_BYTES:
        if len(jpeg) < original_size or resized or original_size > MAX_BYTES:
            return jpeg, ext, old_wh, new_wh
    return None, ext, old_wh, new_wh


def apply_image(path: Path, data: bytes, new_ext: str) -> Path:
    dest = path.with_suffix(new_ext)
    if dest != path and dest.exists():
        raise SystemExit(f"不覆寫已存在的檔案：{dest}")
    tmp = dest.with_name(dest.name + ".opt-tmp")
    tmp.write_bytes(data)
    tmp.replace(dest)
    if dest != path and path.exists():
        path.unlink()
    return dest


def rewrite_tree(changes: list[Rewrite]) -> int:
    if not changes:
        return 0
    names = [c.old_base for c in changes]
    if len(names) != len(set(names)):
        dupes = sorted({n for n in names if names.count(n) > 1})
        raise SystemExit(f"有重複檔名，無法安全改引用：{dupes}")

    patterns = []
    for change in sorted(changes, key=lambda c: len(c.old_base), reverse=True):
        pat = re.compile(
            r"(?<![A-Za-z0-9_-])"
            + re.escape(change.old_base)
            + r"(?![A-Za-z0-9_.-])"
        )
        patterns.append((pat, change))

    updated = 0
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in SKIP_TEXT_EXT:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        new = text
        for pat, change in patterns:
            if change.old_base not in new:
                continue
            new = pat.sub(change.new_base, new)
        if new != text:
            path.write_text(new, encoding="utf-8")
            updated += 1
    return updated


def check() -> int:
    problems = []
    for path in iter_images():
        im = open_image(path)
        width, height = im.size
        size = path.stat().st_size
        reasons = []
        if width > MAX_WIDTH:
            reasons.append(f"寬 {width}px")
        if size > MAX_BYTES:
            reasons.append(f"{size / 1024 / 1024:.2f} MB")
        if reasons:
            problems.append(f"{path.relative_to(ROOT)} ({'、'.join(reasons)}, {width}x{height})")
    if problems:
        sys.stderr.write(f"{len(problems)} 張圖超過上限（寬 {MAX_WIDTH}px 或 {MAX_BYTES / 1024 / 1024:.0f} MB）：\n")
        for line in problems[:40]:
            sys.stderr.write(f"  {line}\n")
        if len(problems) > 40:
            sys.stderr.write(f"  …還有 {len(problems) - 40} 張\n")
        sys.stderr.write("請跑 python3 .github/scripts/optimize_images.py\n")
        return 1
    print(f"OK：assets 圖片寬度 ≤ {MAX_WIDTH}px，單檔 ≤ {MAX_BYTES / 1024 / 1024:.0f} MB")
    return 0


def optimize() -> int:
    before = sum(p.stat().st_size for p in iter_images())
    changes: list[Rewrite] = []
    rewritten = 0
    for path in list(iter_images()):
        data, new_ext, old_wh, new_wh = plan_image(path)
        if data is None:
            continue
        old_base = path.name
        dest = apply_image(path, data, new_ext)
        rewritten += 1
        if dest.name != old_base:
            changes.append(Rewrite(old_base, dest.name))
        print(f"{old_base} -> {dest.name}  {old_wh[0]}x{old_wh[1]} -> {new_wh[0]}x{new_wh[1]}  {len(data)/1024:.0f} KB")

    text_files = rewrite_tree(changes)
    after = sum(p.stat().st_size for p in iter_images())
    print(
        f"\n重壓 {rewritten} 張，改了 {text_files} 個文字檔。"
        f"圖片合計 {before/1024/1024:.1f} MB -> {after/1024/1024:.1f} MB"
    )
    missing = []
    for change in changes:
        for path in ROOT.rglob("*"):
            if not path.is_file() or any(part in SKIP_DIRS for part in path.parts):
                continue
            if path.suffix.lower() in SKIP_TEXT_EXT:
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            if re.search(
                r"(?<![A-Za-z0-9_-])" + re.escape(change.old_base) + r"(?![A-Za-z0-9_.-])",
                text,
            ):
                missing.append(f"{change.old_base} 仍出現在 {path.relative_to(ROOT)}")
                break
    if missing:
        sys.stderr.write("還有引用沒改到：\n")
        for line in missing:
            sys.stderr.write(f"  {line}\n")
        return 1
    return 0


def main() -> int:
    if not ASSETS.is_dir():
        sys.stderr.write(f"找不到 {ASSETS}\n")
        return 2
    if "--check" in sys.argv:
        return check()
    return optimize()


if __name__ == "__main__":
    sys.exit(main())
