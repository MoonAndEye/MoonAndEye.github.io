# marvinswift.com App API (v1)

給 Flutter app 消費用的靜態 JSON API。這裡的內容全部是**原始 Markdown**
（不是 rendered HTML，也不是結構化 blocks），read path 完全走 GitHub Pages
的靜態 CDN——這一版沒有任何 Cloudflare Worker。

- Base URL：`https://www.marvinswift.com/api/v1/`
- 產生方式：`.github/scripts/build_app_api.py`（Python 3 標準庫，沒有任何
  第三方套件依賴）在 GitHub Actions 裡讀 `_posts/**/*.md` 的原始檔案，
  輸出成這裡的 JSON。由 `.github/workflows/app-api.yml` 在 `_posts/**`、
  `_data/youtube.json` 或這支腳本本身變動、push 到 `main` 時自動跑，
  也可以手動 `workflow_dispatch`。
- **非破壞性**：這個 generator 只讀 `_posts/`，只寫 `api/v1/`，絕對不會
  修改任何一篇原始文章。`_posts/**/*.md` 永遠是唯一真相來源；這裡的
  JSON 是從它 derive 出來的產物，重新跑一次 generator 永遠可以重現。

## 建議的同步流程

1. 先拉 `index.json`（只有幾 KB）。
2. 跟本機存的上一次 `index.json` 比對每個 endpoint 的 `hash`
   （sha256 前 16 碼，比 `count`/`latest` 更可靠——內容改了但篇數、
   最新日期都沒變的情況，hash 一定會變，count/latest 不一定會變）。
3. 只有 hash 不同的 endpoint 才需要重抓；沒變的直接跳過，不用發任何請求。
4. 實際發 GET 請求時帶上本機存的 `ETag`（`If-None-Match`），讓沒有更新的
   請求可以拿到 304，不用重新下載 body。GitHub Pages 本身就會對靜態檔案
   回傳 `ETag`，這一步不需要額外設定。
5. `posts.json` 可能會分頁（見下方「分頁規則」），分頁後每一頁也各自有
   自己的 `hash`，可以只重抓真的變動的那一頁。

因為全站 raw markdown 只有大約 1.5 MB（gzip 後約 400–500 KB），這個同步
流程的終點是「整包抓回來存進本機 SQLite，離線可用」，不是每次都做增量
API 呼叫；`index.json` 的 hash 比對只是用來決定「要不要整包重抓」。

## Endpoint 一覽

| Endpoint | 內容 | 大小量級 |
|---|---|---|
| `index.json` | manifest，列出所有 endpoint 的 count/latest/bytes/hash | 幾 KB |
| `zh/summaries.json` | 中文文章列表，不含全文 | 數百 KB |
| `en/summaries.json` | 英文文章列表，不含全文 | 數十 KB |
| `zh/posts.json`（可能分頁） | 全部中文文章，含完整 Markdown | 約 1.5 MB，已分頁 |
| `en/posts.json` | 全部英文文章，含完整 Markdown | 數百 KB |
| `categories.json` | 五個分類的雙語 metadata | 幾 KB |
| `videos.json` | YouTube 影片/Shorts（轉自 `_data/youtube.json`） | 約 10 KB |
| `series/agent-build-log.json` | Agent Build Log 連載，中英文成對收錄 | 約 100 KB |
| `search-index.json` | 雙語合併的輕量離線搜尋索引 | 約 170 KB |

## index.json

```jsonc
{
  "api_version": 1,
  "generated_at": "2026-08-07T18:11:51.843130+00:00", // ISO8601 UTC，這次 generator 執行時間
  "build_id": "733f31ded444a6a7",                       // 所有 endpoint hash 再取 hash，一個字串代表「這整包 API 的版本」
  "site": {
    "url": "https://www.marvinswift.com",
    "title": "Marv[in]sight",
    "languages": ["zh", "en"]
  },
  "endpoints": {
    "zh/summaries.json": {
      "path": "/api/v1/zh/summaries.json",
      "count": 193,
      "latest": "2026-08-06T23:36:25+08:00", // 這個 endpoint 裡最新一篇文章的 date，null 表示不適用（如 categories.json）
      "bytes": 465961,
      "hash": "5177a797e24f5132"              // sha256(檔案內容) 取前 16 碼
    },
    "zh/posts.json": {
      // 分頁時沒有單一 path，見下方「分頁規則」
      "paginated": true,
      "page_count": 2,
      "pages": [
        { "path": "/api/v1/zh/posts-1.json", "count": 184, "latest": "...", "bytes": 908359, "hash": "..." },
        { "path": "/api/v1/zh/posts-2.json", "count": 9,   "latest": "...", "bytes": 640733, "hash": "..." }
      ],
      "count": 193,     // 全部分頁加總
      "latest": "...",
      "bytes": 1549092, // 全部分頁加總
      "hash": "..."     // 各分頁 hash 再串接起來取 hash，代表「整個 zh/posts.json 邏輯上的版本」
    },
    "en/posts.json": {
      "path": "/api/v1/en/posts.json",
      "paginated": false,
      "count": 87,
      "latest": "...",
      "bytes": 383137,
      "hash": "..."
    }
  }
}
```

### 分頁規則

規格是「單一 `{lang}/posts.json` 序列化後超過 1 MB 才分頁」。目前只有
`zh/posts.json`（約 1.48 MB）超過門檻，切成 `zh/posts-1.json` +
`zh/posts-2.json`；`en/posts.json`（約 383 KB）沒有超過，維持單一檔案。

分頁不是照篇數平分，是照**每篇文章實際序列化後的位元組數**累加著切，
確保每一頁都在門檻以內（文章長度差異很大，Agent Build Log 系列很長、
2013 年代的老文章通常很短，單純均分篇數沒辦法保證每頁都在 1 MB 以內）。

app 端判斷邏輯：讀 `index.json.endpoints["{lang}/posts.json"]`，如果有
`paginated: true`，就照 `pages` 陣列依序抓每一頁再合併成完整文章陣列；
如果是 `paginated: false`，直接用 `path` 抓單一檔案。**未來哪天英文文章
也超過 1 MB，會自動變成分頁格式**——app 端不應該假設任何一個語言永遠是
單檔或永遠是分頁，一律先看 `index.json` 裡的 `paginated` 欄位。

## 文章物件 schema

`zh/posts.json` / `en/posts.json`（分頁後每一頁陣列裡的元素）、
`zh/summaries.json` / `en/summaries.json`（拿掉 `content` 欄位的輕量版）
共用同一個文章物件形狀：

| 欄位 | 型別 | 可為 null | 說明 |
|---|---|---|---|
| `slug` | string | 否 | 從檔名去掉日期前綴、去掉副檔名。**注意**：極少數舊文件名不小心打成兩層 `.md.md`，這裡會如實保留成 slug 裡帶 `.md`（例如 `data-intensive-applications.md`），因為正式網站上的網址本來就長這樣，見下方「已知限制」 |
| `title` | string | 否 | 沒有 front matter title 時，退回用 slug 轉 Title Case |
| `lang` | string | 否 | `"zh"` 或 `"en"` |
| `date` | string | 否 | ISO8601，含 timezone offset |
| `category` | string | **是** | 五個分類之一：`life`/`swift`/`programming`/`finance`/`unitTesting`；極少數壞資料清理後仍取不到值時為 `null`（目前沒有這種案例，但 app 端要防呆） |
| `tags` | string[] | 否 | 可能是空陣列 |
| `summary` | string | 否 | 優先順序：front matter `summary` → `description` → 從正文抽的前 N 字 |
| `url` | string | 否 | 絕對網址，跟正式網站的 permalink 完全一致（已用本機 Jekyll build 逐篇比對過，見交付說明） |
| `hero_image` | string | **是** | 正文裡第一張圖片的絕對 URL，抽不到給 `null` |
| `content` | string | 否 | 正規化後的 Markdown 全文（**只有 posts.json 有這個欄位，summaries.json 沒有**） |
| `content_format` | string | 否 | `"markdown"` 或 `"markdown+html"`，見下方說明 |
| `inline_html_tags` | string[] | 否 | `content_format` 是 `"markdown+html"` 時，列出正文裡殘留的 HTML tag 名稱（小寫）；乾淨的文章是空陣列 |
| `has_insecure_images` | boolean | 否 | 正文裡是否有 `http://`（非 https）的外部圖片 |
| `word_count` | number | 否 | 中文字元數 + 英文單字數的合計（見下方「字數估算方式」） |
| `reading_minutes` | number | 否 | 概略閱讀分鐘數，至少為 1 |
| `source_path` | string | 否 | 對應的 `_posts/` 原始檔相對路徑，方便除錯追溯，app 端通常用不到 |

### `content_format` / `inline_html_tags` / `has_insecure_images` 這幾個旗標怎麼用

這個部落格有一批 2013–2015 年從 Blogspot / Medium 搬過來的舊文章，原始
Markdown 裡混了不少殘留的 inline HTML（YouTube/Twitter embed 用的
`<iframe>`/`<script>`、排版用的 `<div>`/`<p>`/`<h3>` 等等）。這些沒辦法
安全轉成純 Markdown（转了会丢内容或丢版面），所以**原樣保留在 `content`
字串裡**，用旗標讓 app 端自己決定怎麼處理：

- `content_format == "markdown"`：純 Markdown，用一般的 Markdown renderer
  渲染就好。
- `content_format == "markdown+html"`：內文裡混了 `inline_html_tags`
  列出的那些 HTML tag。建議：
  - 如果 app 的 Markdown renderer 有支援「行內 HTML passthrough」
    （例如 `flutter_markdown` 搭配自訂 `MarkdownElementBuilder`，或是
    `flutter_html` 之類支援度更完整的 renderer），直接吃這個字串通常
    可以正常顯示（`<iframe>` 可能還是需要額外處理才能真的播放內嵌影片，
    純顯示文字排版的 `<div>`/`<p>` 通常沒問題）。
  - 如果 renderer 不支援 inline HTML，可以先用 `inline_html_tags` 判斷
    風險等級：只有 `iframe`/`script` 通常代表「這裡有一段嵌入式內容
    App 端可能顯示不出來，但不影響其餘文字」；出現 `div`/`p`/`h3` 等
    版面用的 tag，代表這段落本身的排版就是用 HTML 寫的，降級處理時
    可以考慮至少把裡面的純文字抽出來顯示。
  - 不建議做「自動偵測完全準確」的假設：極少數老文章的正文裡會用純文字
    描述 `<img/>` 這種語法範例（不是真的要渲染的圖片），這種情況會被
    誤判成 `markdown+html`，見下方「已知限制」。

`has_insecure_images` 是給 iOS App Transport Security（ATS）／Android
cleartext traffic policy 用的：這批舊文章裡有一些圖片還連到
`http://` 的 Blogspot/Medium CDN（`bp.blogspot.com`、
`cdn-images-1.medium.com` 等），沒有 https 版本可用，所以**故意保留原始
URL，不會自作聰明改寫成 https**（外部 CDN 不一定支援 https，硬改會直接
變成破圖）。app 端看到這個旗標為 `true`，可以選擇：跳過該圖片改顯示
placeholder、或在 app 的 network security config / Info.plist 裡對這幾個
已知網域開白名單允許 cleartext。

### 字數估算方式

`word_count` = 中文字元數（CJK Unicode 範圍）+ 英文單字數（按空白斷詞）。
`reading_minutes` 用概略閱讀速度換算（中文抓 300 字/分鐘、英文抓 200
字/分鐘），無條件捨去後至少回傳 1。這是粗略估算，不是精確值。

## categories.json

```jsonc
[
  {
    "slug": "life",
    "title_zh": "生活記事", "title_en": "Life Stories",
    "url_zh": "https://www.marvinswift.com/life/",
    "url_en": "https://www.marvinswift.com/en/life/",
    "count_zh": 26, "count_en": 3
  },
  {
    "slug": "finance",
    "title_zh": "財經新聞與投資筆記", "title_en": null,
    "url_zh": "https://www.marvinswift.com/finance/", "url_en": null,
    "count_zh": 18, "count_en": 0
  }
  // ... life / programming / swift / finance / unitTesting
]
```

`finance` 分類目前只有中文文章，`title_en`/`url_en` 為 `null`。

## videos.json

從 `_data/youtube.json`（既有的 `.github/workflows/youtube-data.yml`
維護）轉形狀而來：

```jsonc
{
  "generated_at": "2026-08-07T18:11:51+00:00",
  "videos": [
    { "id": "qualBRg758I", "title": "...", "published": "2026-07-13T17:00:09+00:00",
      "thumbnail": "https://...", "description": "...", "url": "https://youtu.be/qualBRg758I" }
  ],
  "shorts": [ /* 同樣形狀 */ ]
}
```

## series/agent-build-log.json

Marvin 的每日連載，中英文成對收錄（同一集的 zh/en 版本用同一個 slug 對應）：

```jsonc
{
  "slug": "agent-build-log",
  "title_zh": "Agent Build Log", "title_en": "Agent Build Log",
  "episode_count": 23,
  "episodes": [
    { "episode": 23, "slug": "agent-build-log-episode-023",
      "zh": { /* 完整文章物件，含 content */ },
      "en": { /* 完整文章物件，含 content */ } }
    // ... 按集數由小到大排序
  ]
}
```

如果某一集只有其中一個語言版本，另一個語言的欄位會是 `null`（目前
23 集全部都是中英雙語，這個情況現在不會發生，但 app 端要防呆）。

## search-index.json

雙語合併、只含 metadata 的輕量索引，欄位是文章物件的子集合：
`slug`、`lang`、`title`、`category`、`tags`、`summary`、`url`、`date`、
`word_count`。

設計理由：完整全文已經在 `posts.json` 裡了，這份索引的價值是「一個檔案
就能拿到全站雙語的可搜尋欄位」，不用為了做關鍵字比對/自動完成，就先分別
抓 `zh/posts.json`（可能還要處理分頁）跟 `en/posts.json` 兩份大檔。

**這不是全文檢索（full-text search）索引**，只有 title/summary/tags 這幾
個欄位。如果要做正文全文搜尋，建議 app 端把 `posts.json` 下載、存進本機
SQLite 之後，用 SQLite FTS5 對 `content` 欄位建索引，在裝置端做。

## Cloudflare Cache Rules 建議

GitHub Pages 對外回應的 `Cache-Control` 是固定的（`max-age=600`，
10 分鐘），**沒有辦法透過 `_config.yml` 或任何 repo 內設定去改**。如果
這個網域前面沒有額外的 CDN 快取層覆蓋這個行為，最壞情況會是：新文章
發布後，app 最久要等 10 分鐘快取才會過期，才抓得到新版 `index.json`；
反過來說，如果哪天想要更積極地快取大檔案省流量，GitHub Pages 這個固定
10 分鐘的上限也會擋住你。

這個網域本來就是掛在 Cloudflare 後面（`marvinswift.com` 的 DNS/CDN），
所以建議透過 **Cloudflare Cache Rules**（不是 Page Rules，Cache Rules
是比較新、可以用 Rulesets API 管理的功能）針對 `/api/v1/**` 覆蓋
origin 的 `Cache-Control`：

| 路徑 pattern | 建議設定 | 理由 |
|---|---|---|
| `/api/v1/index.json` | 短 TTL（例如 60 秒）或直接 bypass cache | 這是同步流程的入口，必須盡快反映最新內容，檔案本身只有幾 KB，就算 bypass 也不會有明顯流量成本 |
| `/api/v1/*/posts*.json`、`/api/v1/*/summaries.json`、`/api/v1/search-index.json` 等大檔 | 長 TTL（例如 1 天）+ `stale-while-revalidate`（例如再加 1 天） | 這些檔案的「有沒有更新」完全由 `index.json` 的 hash 決定，app 不會盲目直接打這些大檔案；設長 TTL 可以大幅降低 GitHub Pages origin 的流量與延遲，`stale-while-revalidate` 確保 edge cache 過期的瞬間仍然先回舊內容給使用者，背景再更新，避免所有請求同時打回 origin |
| `/api/v1/categories.json`、`/api/v1/videos.json` | 中等 TTL（例如 10–30 分鐘） | 更新頻率介於 index 跟大檔之間 |

實際請求量很小（單一使用者的個人 app，不是公開高流量服務），這組設定
主要是為了「發新文章後多久看得到」跟「省 GitHub Pages 流量」之間取一個
合理的平衡，不是為了扛流量尖峰。

## 老文章正規化：已知限制

這批從 Blogspot / Medium 搬過來的舊文章（主要集中在 2013–2015，以及少數
2018 年以前的文章）做了以下正規化，全部只作用在寫進 JSON 的字串上，
**絕對不會改動 `_posts/` 下的原始檔案**：

1. 巢狀圖片連結 `[![](inner)](outer)` 攤平成單純的 `![alt](url)`，保留原本
   的 alt text（如果有的話）。外層 URL 有兩種情況，取哪一個要分開判斷：
   - **外層也是圖片**（Blogspot 老文的標準格式：內層 `s320` 縮圖、外層
     `s1600` 原圖）→ 取外層，拿到解析度更好的版本。
   - **外層是網頁**（2023 年之後的文章常見，例如
     `[![截圖](/assets/foo.png)](https://example.com/)`）→ 取**內層**。
     判斷方式是看副檔名，再加上一份「不帶副檔名但確定回傳圖片」的 CDN
     白名單（Medium / Blogspot 圖床）；判斷不出來就當成不是圖片，讓內層
     那個確定是圖片的路徑勝出。
2. `/assets/...` 這種站內相對路徑的圖片，補上
   `https://www.marvinswift.com` 前綴變成絕對 URL。
3. `http://` 的外部圖片（Blogspot/Medium 圖床）**保留原始 URL 不做任何
   改寫**，用 `has_insecure_images` 旗標告知 app。
4. 獨立成一行的 `<hr>`/`<hr/>`/`<hr />` 轉成 Markdown 的 `---`。
5. `<br>`/`<br/>`/`<br />` 轉成真正的換行。
6. `<strong>`/`<b>` 轉成 `**粗體**`；`<em>`/`<i>` 轉成 `*斜體*`。
7. 上面 4–6 沒辦法涵蓋的 inline HTML（`<iframe>`、`<script>`、
   `<div>`、排版用的 `<p>`/`<h3>`/`<small>` 等等）**原樣保留**，靠
   `content_format`/`inline_html_tags` 讓 app 端自己決定怎麼處理。
8. 行尾雙空白（Markdown 的隱性硬換行）轉成明確的反斜線硬換行；純空白的
   排版用空行收斂成真正的空行。避免依賴「trailing whitespace 不會被
   trim 掉」這種脆弱假設（很多工具鏈、包括 git 本身的某些設定，都會把
   行尾空白吃掉）。

**已知限制 / 邊界案例**（誠實列出，不是每一項都有辦法在 regex-based
的正規化裡完美處理）：

- **兩篇文章檔名重複打成兩層副檔名**：
  `_posts/programming/en/2024-07-17-data-intensive-applications.md.md`
  與 `_posts/programming/en/2025-03-15-using-cursor-in-jira.md.md`。
  Jekyll 對這種檔名的實際行為是把中間那個 `.md` 也算進 slug 裡，所以
  正式網站上這兩篇的網址本來就長 `/en/programming/xxx.md/`
  這樣（多一段 `.md`）。這支 generator 刻意重現這個行為（而不是「修正」
  成看起來比較合理的網址），因為 `url` 欄位的第一原則是「必須跟正式
  網站一致」。如果 Marvin 想要修正，需要另外重新命名這兩個檔案（會改變
  正式網址，有 SEO 影響，建議另外評估，不在這次任務範圍內）。
- **HTML tag 偵測是 regex-based，不是真的 HTML/Markdown parser**：
  已經排除了 fenced code block（`` ``` ``）跟 inline code（`` `...` ``）
  裡的內容，但抓不到「不在程式碼區塊裡、但只是用純文字描述 tag 語法」
  的案例。實測發現至少 2 篇文章會被誤判：
  - `_posts/swift/zh/2023-04-05-xcode143-released.md` 裡一句話提到
    `<img/>` 是在描述 Xcode release notes 的內容（不是真的圖片），
    這篇會被標成 `markdown+html`，`inline_html_tags` 會多出 `img`。
  - `_posts/swift/zh/2023-06-26-xcode15-beta2-release-notes.md` 裡
    `po <object-address>` 是在描述 LLDB 指令語法（`<object-address>`
    是佔位符，不是 HTML tag），會被誤判多出 `object`。
  這兩篇實際上都可以視為乾淨的 Markdown，只是自動化規則保守地把它們
  標成 `markdown+html`。影響很小（app 端頂多用比較保守的方式渲染這兩篇
  裡的這一句話），但誠實記錄在這裡，沒有嘗試用更複雜的啟發式規則去
  「修正」，避免過度工程化。
- **少數舊文章的 `category` 和實際所在資料夾對不上**（例如某幾篇放在
  `_posts/finance/` 資料夾但 front matter 寫 `category: programming`）。
  這是 2023 年 3 月那批早期文章的既有資料狀況，不是這支 generator 的
  bug——`category` 欄位刻意如實呈現 front matter 的值（跟正式網站的
  分類邏輯一致），只有在值本身明顯是壞資料時（例如整個中文標題被誤填進
  `category` 欄位，這在全站掃過一輪後只找到 1 篇）才會退回用資料夾位置
  當 fallback。完整的對照清單見這次任務的交付說明。
- **少數舊文章的 `permalink` 前綴跟 category 對不上**（例如 front matter
  寫死 `permalink: /finance/:title:output_ext`，但 category 其實是
  `programming`）。這些網址是正式網站上真實存在的網址，`url` 欄位如實
  呈現，跟 `category` 欄位是兩個獨立的資料來源，不會互相「修正」。
- **一篇最早期的文章（`_posts/2013-04-02-beer-market-at-singapore.md`）
  內嵌了一張 base64 data URI 圖片**（約 290 KB 的 base64 文字），佔了
  全站 1.5 MB raw markdown 預算裡不小的比例。這張圖片維持原樣保留在
  `content` 裡（data URI 本身就是自包含的，不需要、也不應該被「絕對化」
  處理）。
- **日期 timezone 的假設**：極少數舊文章的 `date` front matter 沒有帶
  UTC offset（例如 `date: 2013-07-18 14:20`，只有 34 篇）；這支 generator
  固定假設這種情況下是 `+08:00`（台北時間，跟這個部落格絕大多數文章
  明確標示的 offset一致），而不是用「執行 generator 那台機器的系統
  時區」（那樣會因為在本機 macOS 跑跟在 GitHub Actions runner 上跑而
  得到不同結果，破壞 `index.json` hash 的穩定性）。這個假設只影響 ISO
  字串裡標示的 offset，不影響 `url` 裡的年/月/日（Jekyll 的 permalink
  year/month/day 也是直接取字串上的數字，不受 offset 換算影響）。

## 這支腳本如何驗證跟正式網站一致

`url` 欄位是重新實作 Jekyll 的 permalink 解析邏輯算出來的（GitHub
Actions runner 上沒有裝 Ruby/Jekyll，沒辦法直接用 Jekyll 本身算）。這份
邏輯已經用本機 `bundle exec jekyll build` 實際產生的 280 篇文章真實 URL
（透過一個一次性的 Liquid 樣板列印每篇文章的 `post.url`，測試完就刪除，
沒有進到任何 commit 裡）逐篇比對過，**280 篇全部相符**，才確認可以信任
這份重新實作的邏輯。往後如果 `_config.yml` 的 permalink 規則有變動，
建議用同樣的方式重新驗證一次。
