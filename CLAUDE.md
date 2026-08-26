# CLAUDE.md

Jekyll + GitHub Pages 個人 blog，線上位址 <https://www.marvinswift.com>。
建置與客製化說明見 `README.md`，以下只記會踩雷的地方。

## 內容是雙語成對的

`_includes/zh/*.md` 與 `_includes/en/*.md` 一一對應，改一邊就要改另一邊。

中文是預設語言，所以產出路徑會反直覺：中文頁在 `_site/about/`，`_site/zh/about/` 只是轉址頁，
英文在 `_site/en/about/`。驗證 build 結果時別看錯檔案。

## build 前要有 UTF-8 locale

`_sass/minimal-mistakes.scss` 有中文註解。若 shell 沒設 `LANG`，Ruby 會以 US-ASCII 讀檔，
SCSS 編譯就會失敗（`Invalid US-ASCII character "\xE9"`）。加前綴即可：

```bash
LANG=en_US.UTF-8 bundle exec jekyll build
```

終端機通常會自己設好 locale，所以這是 agent 環境才需要，跟原始碼無關。

## 關於頁的外部連結會失效

引用或改動前先確認：`curl -sS -o /dev/null -w "%{http_code}\n" -L "<url>"`。
目前 Apple 開發者憑證已到期，所有 `apps.apple.com` 連結皆 404，已從關於頁移除；續訂後要補回。
