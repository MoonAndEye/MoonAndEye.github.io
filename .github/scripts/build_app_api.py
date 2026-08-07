#!/usr/bin/env python3
"""從 _posts/**/*.md 產生 Flutter app 用的靜態 JSON API，寫進 api/v1/。

設計背景（詳見 api/README.md）：
- 內容格式是 raw Markdown，不是 rendered HTML，也不是結構化 blocks。
- read path 完全走 GitHub Pages 靜態 CDN，這一期不寫 Cloudflare Worker。
- 這支腳本被 .github/workflows/app-api.yml 呼叫，跑在裸的 GitHub Actions
  runner 上，所以只能用 Python 3 標準庫，不能 pip install 任何套件。
- 完全不會、也不能碰 Jekyll 的 build 流程；只讀 _posts/**/*.md 的「原始」
  Markdown 檔案，不讀 _site/ 產出的 HTML。

重要：這支腳本自己重新實作了一份 Jekyll permalink 解析邏輯（見
`resolve_permalink` 一節），因為 GitHub Actions runner 上不會裝 Ruby/Jekyll。
這份邏輯已經用本機真的 `bundle exec jekyll build` 產生的 280 篇文章 URL
逐一比對驗證過，全部相符（比對方式見交付說明，不在這支腳本裡）。

非破壞性原則：這支腳本只寫 api/v1/**，絕對不會修改 _posts/ 下的任何檔案。
"""
from __future__ import annotations

import glob
import hashlib
import json
import os
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# 常數設定
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[2]
POSTS_GLOB = str(ROOT / "_posts" / "**" / "*.md")
API_DIR = ROOT / "api" / "v1"
YOUTUBE_DATA = ROOT / "_data" / "youtube.json"

SITE_URL = "https://www.marvinswift.com"
SITE_TITLE = "Marv[in]sight"
LANGUAGES = ["zh", "en"]

# 五個既有分類目錄（對應 life.markdown / programming.markdown / swift.markdown /
# finance.markdown / unit-testing.markdown 這幾個既有的分類列表頁）
KNOWN_CATEGORY_DIRS = {"life", "swift", "programming", "finance", "unitTesting"}

# 部落格的編輯時區。少數舊文的 date front matter 沒有帶 UTC offset
# （例如 `date: 2013-07-18 14:20`），Jekyll 在 build 當下會用「執行 build
# 那台機器」的系統時區去補上 offset —— 這是不確定的（本機是 +08:00，
# GitHub Actions runner 是 UTC）。為了讓這支腳本每次跑出來的結果都一樣
# （沒有新文章時 hash 不該變），我們固定假設 +08:00（台北），這也是這個
# 部落格實際上大多數文章明確寫出來的 offset。
# 注意：這個假設只影響 ISO8601 字串裡的 offset 標示，不影響 year/month/day
# （所以不會影響 permalink 是否正確——Jekyll 的 year/month/day 也是直接取
# 字串上的數字，不受 offset 換算影響）。
DEFAULT_TZ = timezone(timedelta(hours=8))

# 判斷「這篇文章沒有 lang 資訊時，用內文猜語言」用的 CJK 字元範圍
CJK_RE = re.compile(r"[一-鿿㐀-䶿豈-﫿]")

# 已知的標準 HTML tag 名稱（用來判斷內文裡殘留的 inline HTML）。特別排除
# 掉會被我們安全轉換掉的 br/hr/strong/em/b/i——這幾個轉完之後在最終文字裡
# 已經不存在了，不需要出現在這份白名單判斷結果裡，但仍列在這裡以便掃描到
# 就代表「轉換沒吃乾淨」。
KNOWN_HTML_TAGS = set(
    """a abbr address area article aside audio b base bdi bdo blockquote body br
button canvas caption cite code col colgroup data datalist dd del details dfn dialog div dl dt em
embed fieldset figcaption figure footer form h1 h2 h3 h4 h5 h6 head header hgroup hr html i iframe
img input ins kbd label legend li link main map mark meta meter nav noscript object ol optgroup
option output p param picture pre progress q rp rt ruby s samp script section select small source
span strong style sub summary sup table tbody td template textarea tfoot th thead time title tr
track u ul var video wbr center font strike big tt""".split()
)


# ---------------------------------------------------------------------------
# Front matter 解析（手刻版 YAML 子集合，因為 stdlib 沒有 yaml 模組）
# ---------------------------------------------------------------------------
# 已經實際掃過全站 280 篇文章的 front matter，這個部落格只用到：
#   - 純量：key: value / key: "value" / key: 'value' / key:（空值）
#   - 單行 inline list：key: [a, b, c]
# 沒有任何一篇用到多行 block scalar（`>-`、`|`）或 YAML block list（- item），
# 所以不需要支援那些語法，故意保持簡單。
#
# 注意：Jekyll 的 front matter key 是「大小寫敏感」的字串比對，例如某篇舊文
# 誤植成 `Category:`（大寫 C），Jekyll 完全不會把它當成 categories 用。
# 這支 parser 用同樣邏輯（直接用原始 key 字串當 dict key），所以會自動
# 重現一樣的行為，不需要特別處理。

FRONT_MATTER_RE = re.compile(r"\A---[ \t]*\n(.*?\n)---[ \t]*\n?", re.S)
FM_LINE_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):[ \t]*(.*?)[ \t]*$")


def _unquote(raw: str) -> str:
    raw = raw.strip()
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in ("'", '"'):
        inner = raw[1:-1]
        if raw[0] == '"':
            inner = inner.replace('\\"', '"')
        return inner
    return raw


def _split_inline_list(inner: str) -> list[str]:
    """切開 `[a, "b, c", d]` 這種 inline list，並且不會被逗號裡的引號騙到。"""
    parts, cur, quote = [], "", None
    for ch in inner:
        if quote:
            cur += ch
            if ch == quote:
                quote = None
        elif ch in ("'", '"'):
            quote = ch
            cur += ch
        elif ch == ",":
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    parts.append(cur)
    return [_unquote(p) for p in parts if p.strip() != ""]


def _parse_scalar(raw: str):
    if raw == "":
        return None
    if raw.startswith("[") and raw.endswith("]"):
        return _split_inline_list(raw[1:-1])
    return _unquote(raw)


def parse_front_matter(text: str) -> tuple[dict, str]:
    """回傳 (front_matter dict, 去掉 front matter 之後的 body)。"""
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return {}, text
    fm_text = m.group(1)
    body = text[m.end():]
    data: dict[str, object] = {}
    for line in fm_text.splitlines():
        if not line.strip():
            continue
        lm = FM_LINE_RE.match(line)
        if not lm:
            continue  # 容錯：看不懂的行直接跳過，不整篇報錯
        key, val = lm.group(1), lm.group(2)
        data[key] = _parse_scalar(val)
    return data, body


# ---------------------------------------------------------------------------
# Slug / date / categories / lang：這些欄位的計算方式都必須跟 Jekyll 一致，
# 因為 url 欄位的正確性完全依賴這幾個計算結果。
# ---------------------------------------------------------------------------


def compute_slug(filename: str) -> str:
    """從檔名算出 Jekyll 的 :title placeholder（也就是 post.slug）。

    注意：只去掉「最後一個」副檔名（跟 Jekyll 一樣用 splitext 邏輯），
    因為 repo 裡有兩篇文章檔名不小心打成兩層 .md.md
    （2024-07-17-data-intensive-applications.md.md、
    2025-03-15-using-cursor-in-jira.md.md），Jekyll 實際上就是把中間那個
    「.md」也留在 slug 裡，因此正式網站上這兩篇的網址真的長這樣：
    /en/programming/data-intensive-applications.md/
    這是一個既有的內容瑕疵（檔名打錯），不是這支腳本的 bug；為了讓 url
    欄位跟正式網站一致，這裡刻意「原樣重現」這個瑕疵，不要自作聰明修掉。
    """
    stem, _ext = os.path.splitext(filename)
    m = re.match(r"^\d{4}-\d{2}-\d{2}-(.+)$", stem)
    return m.group(1) if m else stem


_DATE_RE = re.compile(
    r"^(?P<y>\d{4})-(?P<mo>\d{2})-(?P<d>\d{2})"
    r"(?:[T ](?P<h>\d{2}):(?P<mi>\d{2})(?::(?P<s>\d{2}))?)?"
    r"[ \t]*(?P<off>[+-]\d{2}:?\d{2}|Z)?[ \t]*$"
)


def _parse_jekyll_date(raw: str) -> datetime | None:
    m = _DATE_RE.match(raw.strip())
    if not m:
        return None
    y, mo, d = int(m["y"]), int(m["mo"]), int(m["d"])
    h, mi, s = int(m["h"] or 0), int(m["mi"] or 0), int(m["s"] or 0)
    off = m["off"]
    if off is None:
        tz = DEFAULT_TZ
    elif off == "Z":
        tz = timezone.utc
    else:
        off = off.replace(":", "")
        sign = 1 if off[0] == "+" else -1
        oh, om = int(off[1:3]), int(off[3:5])
        tz = timezone(sign * timedelta(hours=oh, minutes=om))
    try:
        return datetime(y, mo, d, h, mi, s, tzinfo=tz)
    except ValueError:
        return None


def compute_date(fm: dict, filename: str) -> datetime:
    raw = fm.get("date")
    if isinstance(raw, str):
        dt = _parse_jekyll_date(raw)
        if dt:
            return dt
    # fallback：front matter 沒有合法的 date，就從檔名的 YYYY-MM-DD 取日期，
    # 時間補 00:00:00（全站只有 1 篇文章會走到這個 fallback）。
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})-", filename)
    if m:
        y, mo, d = (int(x) for x in m.groups())
        return datetime(y, mo, d, 0, 0, 0, tzinfo=DEFAULT_TZ)
    # 理論上不會發生（280 篇都至少能從檔名取到日期）
    return datetime(1970, 1, 1, tzinfo=timezone.utc)


def compute_categories_raw(fm: dict) -> list[str]:
    """回傳「跟 Jekyll 產生 URL 時用的一模一樣」的 categories 陣列。

    刻意保留原始值（就算是明顯打錯的資料，例如某篇財經文章的
    category 被誤填成整個標題），因為這個值會直接影響 :categories
    placeholder 算出來的 url，必須跟正式網站一致。給人看的 `category`
    欄位另外用 `display_category()` 做容錯清理。
    """
    val = fm.get("category")
    if val is None:
        val = fm.get("categories")
    if val is None:
        return []
    if isinstance(val, list):
        return [str(v) for v in val if str(v).strip()]
    # Jekyll 對「純量 categories」的行為是用空白切開（例如 `categories: a b`）
    return [v for v in str(val).split() if v]


_SLUG_LIKE_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_-]*$")


def dir_category(rel_path: str) -> str | None:
    """從檔案路徑推斷「資料夾分類」，只當作 display_category 的 fallback。"""
    parts = Path(rel_path).parts
    for p in parts[1:-1]:  # 跳過開頭的 "_posts" 跟結尾的檔名
        if p in KNOWN_CATEGORY_DIRS:
            return p
    return None


def display_category(categories_raw: list[str], dcat: str | None) -> str | None:
    """給 app 用的乾淨分類值。

    全站掃過一輪後，只有 1 篇文章的 category 是明顯壞資料（把整個中文
    標題誤植進 category 欄位），這裡用「長得像不像合法 slug」當判斷依據，
    壞資料就退回用資料夾分類；其餘（就算資料夾跟 front matter 對不上，
    例如某幾篇放在 finance/ 資料夾但 category 寫 programming）一律照實
    呈現 front matter 的值，因為那才是正式網站真正呈現出來的分類。
    """
    if not categories_raw:
        return dcat
    cat = categories_raw[0]
    if _SLUG_LIKE_RE.match(cat):
        return cat
    return dcat or cat


def compute_lang(fm: dict, rel_path: str, title: str, plain_text: str) -> str:
    lang = fm.get("lang")
    if isinstance(lang, str) and lang in ("zh", "en"):
        return lang
    parts = Path(rel_path).parts
    if len(parts) >= 2:
        parent = parts[-2]
        if parent == "zh":
            return "zh"
        if parent == "en":
            return "en"
    # 根層舊文（以及少數扁平放在 finance/、unitTesting/ 底下、沒有 lang
    # 子目錄的文章）既沒有 lang 資料夾、也沒有 front matter lang 欄位時，
    # 優先看「標題」有沒有 CJK 字元——標題是作者自己寫的，訊號比全文可靠
    # 得多。已經實測發現：如果直接看全文的 CJK/英文字元比例，會有一篇
    # 財經文章（FTX 那篇）被誤判成英文，因為內文貼了一大段引用的英文
    # 法律信件全文，字元數蓋過作者自己寫的中文評論——但那篇的標題
    # 「FTX 向客戶發 email...」明顯是中文，用標題判斷就不會出錯。
    # 全站掃過一輪，62 篇會走到這個 fallback 的文章，標題全部都是中文，
    # 用這個規則全部判斷正確（見交付說明的驗證結果）。
    if CJK_RE.search(title):
        return "zh"
    if title.strip() and not CJK_RE.search(title):
        return "en"
    # 標題本身抽不出任何語言訊號時（理論上不會發生），才退回看全文比例
    cjk = len(CJK_RE.findall(plain_text))
    latin_words = len(CJK_RE.sub(" ", plain_text).split())
    return "zh" if cjk >= latin_words else "en"


# ---------------------------------------------------------------------------
# Permalink 解析：重現 Jekyll 在這個 repo _config.yml 設定下的實際行為。
# ---------------------------------------------------------------------------
# _config.yml 的 defaults 只對「_posts/**/zh」與「_posts/**/en」這兩個 scope
# 設定 permalink（分別是 /zh/:categories/:title/ 與 /en/:categories/:title/），
# 其餘文章沒有全站 permalink 設定，因此走 Jekyll 內建預設值
# "/:categories/:year/:month/:day/:title:output_ext"。
# 92 篇舊文在 front matter 自己寫死了 permalink，那個優先權最高（會直接
# override 上面兩條規則），因為 Jekyll 的 defaults 只在文件「沒有」自己
# 設定該欄位時才套用。
# 這整套邏輯已經用本機 `bundle exec jekyll build` 產生的 280 筆真實 url
# 全數比對過，完全相符。

DEFAULT_PERMALINK_TEMPLATE = "/:categories/:year/:month/:day/:title:output_ext"


def resolve_permalink(template: str, categories_raw: list[str], slug: str, date: datetime) -> str:
    # Jekyll 在把 categories 代入 :categories placeholder 時，會對每一段做
    # slugify（全部轉小寫），跟 post.category 這個「給人看」的原始值是分開的
    # 兩件事。實測發現：unitTesting 分類的英文文章沒有寫死 permalink，是走
    # `_posts/**/en` scope 的 `/en/:categories/:title/`，算出來的網址是
    # /en/unittesting/...（小寫），跟 category 顯示值 "unitTesting" 不同。
    cat_path = "/".join(c.lower() for c in categories_raw)
    replacements = {
        ":categories": cat_path,
        ":title": slug,
        ":year": f"{date.year:04d}",
        ":month": f"{date.month:02d}",
        ":day": f"{date.day:02d}",
        ":output_ext": ".html",
    }
    result = template
    for key in sorted(replacements, key=len, reverse=True):
        result = result.replace(key, replacements[key])
    # :categories 是空字串時會留下 "//"，Jekyll 會把它收斂成單一個 "/"
    result = re.sub(r"/{2,}", "/", result)
    return result


def compute_url_path(fm: dict, rel_path: str, categories_raw: list[str], slug: str, date: datetime) -> str:
    explicit = fm.get("permalink")
    if isinstance(explicit, str) and explicit.strip():
        template = explicit.strip()
    else:
        parts = Path(rel_path).parts
        parent = parts[-2] if len(parts) >= 2 else None
        if parent == "zh":
            template = "/zh/:categories/:title/"
        elif parent == "en":
            template = "/en/:categories/:title/"
        else:
            template = DEFAULT_PERMALINK_TEMPLATE
    return resolve_permalink(template, categories_raw, slug, date)


# ---------------------------------------------------------------------------
# 內文正規化：把老文章從 Blogspot / Medium 搬過來殘留的髒 HTML 處理乾淨，
# 同時保持「非破壞性」——只在記憶體裡處理要寫進 JSON 的字串，絕對不改寫
# _posts/ 底下的原始檔案。
# ---------------------------------------------------------------------------

_NESTED_IMG_RE = re.compile(r"\[!\[([^\]]*)\]\(([^)]+)\)\]\(([^)]+)\)")
_HR_LINE_RE = re.compile(r"^[ \t]*<hr[ \t]*/?>[ \t]*$", re.I | re.M)
_BR_RE = re.compile(r"<br[ \t]*/?>", re.I)
_STRONG_B_RE = re.compile(r"<(strong|b)>(.*?)</\1>", re.I | re.S)
_EM_I_RE = re.compile(r"<(em|i)>(.*?)</\1>", re.I | re.S)
_MD_IMG_RE = re.compile(r"(!\[[^\]]*\]\()([^)]+)(\))")
_HTML_IMG_SRC_RE = re.compile(r"<img\b[^>]*\bsrc=[\"']http://", re.I)
_TAG_SCAN_RE = re.compile(r"</?([a-zA-Z][a-zA-Z0-9]*)\b[^>]*>")
_FENCE_RE = re.compile(r"```.*?```", re.S)
_TILDE_FENCE_RE = re.compile(r"~~~.*?~~~", re.S)
_INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


def _flatten_nested_images(text: str) -> str:
    """把 `[![](thumb)](full)` 這種巢狀縮圖連結攤平成 `![alt](full)`。

    老文章從 Blogspot 搬過來的圖片幾乎都是這個格式：內層 `![]()`是縮圖、
    外層連結才是原始大圖。Flutter 端的 markdown renderer 對「連結包圖片」
    這種巢狀語法支援度不一，攤平之後兩邊都能正常吃。alt text（如果內層
    有寫）會被保留下來。
    """

    def repl(m: re.Match) -> str:
        alt, _thumb, full = m.groups()
        return f"![{alt}]({full})"

    return _NESTED_IMG_RE.sub(repl, text)


def _strip_code_regions(text: str) -> str:
    """把 fenced code block／inline code 換成等長空白，只用來做 tag 掃描，
    避免程式碼範例裡的泛型語法（例如 Swift 的 `Array<Int>`）被誤判成
    HTML tag。回傳字串長度刻意跟原字串一樣，方便除錯時對照位置。"""
    t = _FENCE_RE.sub(lambda m: " " * len(m.group(0)), text)
    t = _TILDE_FENCE_RE.sub(lambda m: " " * len(m.group(0)), t)
    t = _INLINE_CODE_RE.sub(lambda m: " " * len(m.group(0)), t)
    return t


def _normalize_hard_breaks(text: str) -> str:
    """把行尾雙空白硬換行，轉成明確的 `\\` 硬換行語法。

    只有在「這一行有實際內容」而且「下一行也還有內容（同一段落）」時，
    才補上反斜線；純空白的 spacer 行（老文章拿來當作間距用）直接清成
    真正的空行，避免留下要靠 renderer 猜測行為的模糊格式。
    """
    lines = text.split("\n")
    n = len(lines)
    out = []
    for i, line in enumerate(lines):
        rtrimmed = line.rstrip(" \t")
        trailing_ws_len = len(line) - len(rtrimmed)
        if rtrimmed == "":
            out.append("")
            continue
        next_has_content = i + 1 < n and lines[i + 1].strip() != ""
        if trailing_ws_len >= 2 and next_has_content:
            out.append(rtrimmed + "\\")
        else:
            out.append(rtrimmed)
    return "\n".join(out)


def normalize_content(raw_body: str, site_url: str) -> tuple[str, str, list[str], bool]:
    """回傳 (normalized_markdown, content_format, inline_html_tags, has_insecure_images)。"""
    text = raw_body.lstrip("\n")

    text = _flatten_nested_images(text)
    text = _HR_LINE_RE.sub("---", text)
    text = _BR_RE.sub("\n", text)
    text = _STRONG_B_RE.sub(r"**\2**", text)
    text = _EM_I_RE.sub(r"*\2*", text)

    insecure_md = False

    def _img_repl(m: re.Match) -> str:
        nonlocal insecure_md
        prefix, url, suffix = m.groups()
        if url.startswith("http://"):
            insecure_md = True
            return m.group(0)  # 外部 http:// 圖片保留原樣，不要自作聰明改寫
        if url.startswith("https://") or url.startswith("data:"):
            return m.group(0)
        if url.startswith("/"):
            return f"{prefix}{site_url}{url}{suffix}"
        # 全站掃過一輪，沒有真正的「純相對路徑」圖片（唯一一個非絕對/非
        # root-relative 的案例是 base64 data URI），這條分支是保險用的。
        return f"{prefix}{site_url}/{url}{suffix}"

    text = _MD_IMG_RE.sub(_img_repl, text)
    insecure_html = bool(_HTML_IMG_SRC_RE.search(text))
    has_insecure_images = insecure_md or insecure_html

    scan_target = _strip_code_regions(text)
    tags = set()
    for m in _TAG_SCAN_RE.finditer(scan_target):
        t = m.group(1).lower()
        if t in KNOWN_HTML_TAGS:
            tags.add(t)
    content_format = "markdown+html" if tags else "markdown"

    text = _normalize_hard_breaks(text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip("\n") + "\n"

    return text, content_format, sorted(tags), has_insecure_images


# ---------------------------------------------------------------------------
# 純文字抽取（給 word_count / summary fallback / hero_image 用）
# ---------------------------------------------------------------------------

_MD_IMAGE_STRIP_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
_MD_LINK_STRIP_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
_HTML_TAG_STRIP_RE = re.compile(r"<[^>]+>")
_MD_PUNCT_RE = re.compile(r"^[ \t]*[#>*_=-]+[ \t]*", re.M)


def to_plain_text(markdown_text: str) -> str:
    t = _FENCE_RE.sub(" ", markdown_text)
    t = _TILDE_FENCE_RE.sub(" ", t)
    t = _INLINE_CODE_RE.sub(" ", t)
    t = _MD_IMAGE_STRIP_RE.sub(" ", t)
    t = _MD_LINK_STRIP_RE.sub(r"\1", t)
    t = _HTML_TAG_STRIP_RE.sub(" ", t)
    t = _MD_PUNCT_RE.sub(" ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def compute_word_stats(plain_text: str) -> tuple[int, int]:
    cjk_count = len(CJK_RE.findall(plain_text))
    latin_words = len(CJK_RE.sub(" ", plain_text).split())
    word_count = cjk_count + latin_words
    # 概略閱讀速度：中文抓 300 字/分鐘、英文抓 200 字/分鐘
    minutes = (cjk_count / 300.0) + (latin_words / 200.0)
    reading_minutes = max(1, round(minutes))
    return word_count, reading_minutes


def extract_hero_image(normalized_content: str) -> str | None:
    m = _MD_IMG_RE.search(normalized_content)
    if m:
        return m.group(2)
    return None


def make_summary(fm: dict, plain_text: str, lang: str) -> str:
    for key in ("summary", "description"):
        val = fm.get(key)
        if isinstance(val, str) and val.strip():
            return val.strip()
    limit = 120 if lang == "zh" else 220
    snippet = plain_text[:limit].strip()
    if len(plain_text) > limit:
        snippet += "…"
    return snippet


# ---------------------------------------------------------------------------
# 主要組裝流程
# ---------------------------------------------------------------------------


def build_post_record(abs_path: str) -> dict:
    rel_path = os.path.relpath(abs_path, ROOT).replace(os.sep, "/")
    filename = os.path.basename(abs_path)
    raw_text = Path(abs_path).read_text(encoding="utf-8")

    fm, raw_body = parse_front_matter(raw_text)

    slug = compute_slug(filename)
    date = compute_date(fm, filename)
    categories_raw = compute_categories_raw(fm)
    dcat = dir_category(rel_path)
    category = display_category(categories_raw, dcat)

    normalized_content, content_format, inline_html_tags, has_insecure_images = normalize_content(
        raw_body, SITE_URL
    )
    plain_text = to_plain_text(normalized_content)

    title = fm.get("title")
    if not isinstance(title, str) or not title.strip():
        # Jekyll 對沒有 title 的文件會用檔名 slug 轉成 Title Case 當標題
        title = " ".join(w.capitalize() for w in slug.split("-"))

    lang = compute_lang(fm, rel_path, title, plain_text)

    url_path = compute_url_path(fm, rel_path, categories_raw, slug, date)
    url = SITE_URL + url_path

    tags_val = fm.get("tags")
    if isinstance(tags_val, list):
        tags = [str(t) for t in tags_val if str(t).strip()]
    elif isinstance(tags_val, str) and tags_val.strip():
        tags = [tags_val.strip()]
    else:
        tags = []

    summary = make_summary(fm, plain_text, lang)
    hero_image = extract_hero_image(normalized_content)
    word_count, reading_minutes = compute_word_stats(plain_text)

    return {
        "slug": slug,
        "title": title,
        "lang": lang,
        "date": date.isoformat(),
        "category": category,
        "tags": tags,
        "summary": summary,
        "url": url,
        "hero_image": hero_image,
        "content": normalized_content,
        "content_format": content_format,
        "inline_html_tags": inline_html_tags,
        "has_insecure_images": has_insecure_images,
        "word_count": word_count,
        "reading_minutes": reading_minutes,
        "source_path": rel_path,
    }


def load_all_posts() -> list[dict]:
    files = sorted(glob.glob(POSTS_GLOB, recursive=True))
    posts = [build_post_record(f) for f in files]
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def summarize(post: dict) -> dict:
    """summaries.json / search-index.json 用的輕量版本，不含 content 全文。"""
    light = dict(post)
    light.pop("content", None)
    return light


def sha256_16(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:16]


def write_json(path: Path, data) -> tuple[int, str]:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(data, ensure_ascii=False, indent=1) + "\n"
    payload = text.encode("utf-8")
    path.write_bytes(payload)
    return len(payload), sha256_16(payload)


# posts.json 分頁門檻。規格書寫的是「單檔超過 1 MB 才分頁」，這裡抓
# 900_000 bytes 當實際切分依據，留一點安全邊界，避免切完某一頁又剛好
# 卡在 1 MB 附近（分頁數量由內容量自動決定，不是寫死頁數）。
PAGINATION_THRESHOLD_BYTES = 1_000_000
PAGINATION_TARGET_BYTES = 900_000


def write_posts_endpoint(lang: str, posts: list[dict]) -> dict:
    """寫 {lang}/posts.json；超過門檻才切成 {lang}/posts-N.json 分頁。

    回傳要塞進 index.json `endpoints["{lang}/posts.json"]` 的 metadata。
    非分頁時是一般的 {path,count,latest,bytes,hash} 形狀；分頁時額外多
    `paginated: true` 與 `pages` 陣列，每一頁各自有自己的 bytes/hash，
    這樣 app 之後只有某一頁內容變動時，可以只重抓那一頁，不用整包重下載。
    """
    full_path = API_DIR / lang / "posts.json"
    size, digest = write_json(full_path, posts)
    latest = max((p["date"] for p in posts), default=None)

    if size <= PAGINATION_THRESHOLD_BYTES:
        return {
            "path": f"/api/v1/{lang}/posts.json",
            "paginated": False,
            "count": len(posts),
            "latest": latest,
            "bytes": size,
            "hash": digest,
        }

    # 超過門檻：先移除剛剛寫好的單一大檔（分頁後就不該再對外提供這個檔案，
    # 避免內容重複、也避免 app 誤抓到過大的整包檔案）。
    full_path.unlink()

    # 文章長度差異很大（老文章很短、Agent Build Log 系列很長，而且排序
    # 是按日期新到舊，同類型文章常常會排在一起），如果單純「篇數平分」，
    # 分到的那一頁仍然可能超過門檻。改成照「每篇的實際序列化位元組數」
    # 累加，滿了就切下一頁，才能確保每一頁都在門檻以內。
    chunks: list[list[dict]] = []
    current: list[dict] = []
    current_bytes = 0
    for post in posts:
        post_bytes = len(json.dumps(post, ensure_ascii=False).encode("utf-8"))
        if current and current_bytes + post_bytes > PAGINATION_TARGET_BYTES:
            chunks.append(current)
            current, current_bytes = [], 0
        current.append(post)
        current_bytes += post_bytes
    if current:
        chunks.append(current)

    pages = []
    for chunk in chunks:
        page_no = len(pages) + 1
        page_path = API_DIR / lang / f"posts-{page_no}.json"
        p_size, p_digest = write_json(page_path, chunk)
        pages.append(
            {
                "path": f"/api/v1/{lang}/posts-{page_no}.json",
                "count": len(chunk),
                "latest": max((p["date"] for p in chunk), default=None),
                "bytes": p_size,
                "hash": p_digest,
            }
        )

    return {
        "paginated": True,
        "page_count": len(pages),
        "pages": pages,
        "count": len(posts),
        "latest": latest,
        "bytes": sum(p["bytes"] for p in pages),
        "hash": sha256_16("|".join(p["hash"] for p in pages).encode("utf-8")),
    }


def build_categories_json(posts: list[dict]) -> list[dict]:
    # 分類的中英文標題/描述/網址，取自既有的分類列表頁 front matter
    # （life.markdown / en/life.md 等），這裡直接寫死對照表：這些頁面本來
    # 就是給人看的靜態文案，不會頻繁變動，比另外寫檔案解析更省事也更穩定。
    meta = {
        "life": {
            "title_zh": "生活記事",
            "title_en": "Life Stories",
            "url_zh": f"{SITE_URL}/life/",
            "url_en": f"{SITE_URL}/en/life/",
        },
        "programming": {
            "title_zh": "程式開發文章",
            "title_en": "Programming Articles",
            "url_zh": f"{SITE_URL}/programming/",
            "url_en": f"{SITE_URL}/en/programming/",
        },
        "swift": {
            "title_zh": "Swift 開發文章",
            "title_en": "Swift Articles",
            "url_zh": f"{SITE_URL}/swift/",
            "url_en": f"{SITE_URL}/en/swift/",
        },
        "finance": {
            "title_zh": "財經新聞與投資筆記",
            "title_en": None,
            "url_zh": f"{SITE_URL}/finance/",
            "url_en": None,
        },
        "unitTesting": {
            "title_zh": "單元測試 Unit Testing 系列文章",
            "title_en": "Unit Testing Series",
            "url_zh": f"{SITE_URL}/unitTesting/",
            "url_en": f"{SITE_URL}/en/unitTesting/",
        },
    }
    result = []
    for slug, info in meta.items():
        count_zh = sum(1 for p in posts if p["category"] == slug and p["lang"] == "zh")
        count_en = sum(1 for p in posts if p["category"] == slug and p["lang"] == "en")
        result.append(
            {
                "slug": slug,
                "title_zh": info["title_zh"],
                "title_en": info["title_en"],
                "url_zh": info["url_zh"],
                "url_en": info["url_en"],
                "count_zh": count_zh,
                "count_en": count_en,
            }
        )
    return result


def build_videos_json() -> dict:
    if not YOUTUBE_DATA.exists():
        return {"generated_at": None, "videos": [], "shorts": []}
    raw = json.loads(YOUTUBE_DATA.read_text(encoding="utf-8"))

    def reshape(items: list[dict]) -> list[dict]:
        out = []
        for it in items:
            out.append(
                {
                    "id": it.get("id"),
                    "title": it.get("title"),
                    "published": it.get("published"),
                    "thumbnail": it.get("thumbnail"),
                    "description": it.get("description"),
                    "url": f"https://youtu.be/{it.get('id')}" if it.get("id") else None,
                }
            )
        return out

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "videos": reshape(raw.get("videos", [])),
        "shorts": reshape(raw.get("shorts", [])),
    }


_EPISODE_RE = re.compile(r"^agent-build-log-episode-(\d+)$")


def build_series_agent_build_log(posts: list[dict]) -> dict:
    by_episode: dict[int, dict] = {}
    for p in posts:
        m = _EPISODE_RE.match(p["slug"])
        if not m:
            continue
        ep_num = int(m.group(1))
        entry = by_episode.setdefault(
            ep_num, {"episode": ep_num, "slug": p["slug"], "zh": None, "en": None}
        )
        entry[p["lang"]] = p
    episodes = [by_episode[k] for k in sorted(by_episode)]
    return {
        "slug": "agent-build-log",
        "title_zh": "Agent Build Log",
        "title_en": "Agent Build Log",
        "episode_count": len(episodes),
        "episodes": episodes,
    }


def build_search_index(posts: list[dict]) -> list[dict]:
    """輕量、雙語合併的離線搜尋索引（metadata only，不含全文）。

    設計理由見 api/README.md：完整全文已經在 posts.json 裡，
    search-index.json 的價值是「一個檔案就能拿到全站雙語的可搜尋欄位」，
    不用先分別抓 zh/en 兩份 posts.json 才能做關鍵字比對/自動完成。
    """
    fields = (
        "slug",
        "lang",
        "title",
        "category",
        "tags",
        "summary",
        "url",
        "date",
        "word_count",
    )
    return [{k: p[k] for k in fields} for p in posts]


def main() -> None:
    posts = load_all_posts()

    zh_posts = [p for p in posts if p["lang"] == "zh"]
    en_posts = [p for p in posts if p["lang"] == "en"]

    endpoints_data: dict[str, object] = {
        "zh/summaries.json": [summarize(p) for p in zh_posts],
        "en/summaries.json": [summarize(p) for p in en_posts],
        "categories.json": build_categories_json(posts),
        "videos.json": build_videos_json(),
        "series/agent-build-log.json": build_series_agent_build_log(posts),
        "search-index.json": build_search_index(posts),
    }

    endpoints_meta = {}
    for rel, data in endpoints_data.items():
        path = API_DIR / rel
        size, digest = write_json(path, data)
        if isinstance(data, list):
            count = len(data)
            latest = max((p.get("date") for p in data if isinstance(p, dict) and "date" in p), default=None)
        else:
            count = None
            latest = None
        endpoints_meta[rel] = {
            "path": f"/api/v1/{rel}",
            "count": count,
            "latest": latest,
            "bytes": size,
            "hash": digest,
        }

    # posts.json 可能會超過 1MB 而分頁，跟其他固定形狀的 endpoint 分開處理
    endpoints_meta["zh/posts.json"] = write_posts_endpoint("zh", zh_posts)
    endpoints_meta["en/posts.json"] = write_posts_endpoint("en", en_posts)

    index_payload = {
        "api_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "build_id": hashlib.sha256(
            "|".join(sorted(m["hash"] for m in endpoints_meta.values())).encode("utf-8")
        ).hexdigest()[:16],
        "site": {"url": SITE_URL, "title": SITE_TITLE, "languages": LANGUAGES},
        "endpoints": endpoints_meta,
    }
    write_json(API_DIR / "index.json", index_payload)

    print(f"posts: total={len(posts)} zh={len(zh_posts)} en={len(en_posts)}")
    for rel, meta in endpoints_meta.items():
        print(f"  {rel}: {meta['bytes']} bytes, hash={meta['hash']}, count={meta['count']}")


if __name__ == "__main__":
    main()
