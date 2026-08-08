{%- assign app = site.data.apps[include.app] -%}
*生效日期：{{ app.effective | date: "%Y 年 %-m 月 %-d 日" }} · 適用於 **{{ app.name }}**（`{{ app.bundle_id }}`{% if app.platforms %}，{{ app.platforms | join: "、" }}{% endif %}）*

English version: [{{ app.name }} Privacy Policy]({{ include.en_url }})

## 一句話版本

{{ app.name }} 沒有帳號機制，也不會跟你要任何個人資料。{% if app.local_data %}收藏與閱讀紀錄只存在你的手機裡，我沒有任何管道看得到。{% endif %}app 會把匿名的使用統計與當機報告送給 Google Firebase，讓我知道哪些文章有人讀、哪裡壞了要修。{% if app.ads == false %}沒有廣告{% if app.purchases == false %}，也沒有任何付費項目{% endif %}。{% endif %}我不販售資料，也不會跨到其他公司的 app 或網站追蹤你。

## 誰負責

{{ app.name }} 由位於台灣的獨立開發者 **Marvin Lin** 開發與維運。本政策的任何問題，請來信 [{{ site.email }}](mailto:{{ site.email }})。

{% if app.local_data %}## 只留在你裝置上的資料

以下資料完全不會離開你的手機，存放在 app 的私有儲存空間，我讀不到，而且**移除 app 就會一併刪除**：

{% for item in app.local_data.zh %}- {{ item }}
{% endfor %}
{% endif %}
## 會送出裝置的資料

{% for key in app.services %}{% assign svc = site.data.privacy_services[key] %}### {{ svc.zh.name }}

{{ svc.zh.data }}

*用途：*{{ svc.zh.purpose }}
*處理者：*{{ svc.provider }} — 見其[隱私權說明]({{ svc.provider_policy }})。

{% endfor %}{% if app.ad_id %}在 Android 上，上述收集可能包含 Google 廣告 ID。我不用它來投放或鎖定廣告，它是標準分析套件內建帶進來的。你可以隨時到裝置的**設定 → 隱私權 → 廣告**重設或刪除它。

{% endif %}{% if app.content_api %}### 從我自己網站下載的內容

app 會從 `{{ app.content_api }}` 下載文章、圖片與影片清單。這些都是不需登入的公開檔案。該請求不包含任何關於你的資訊，只有任何網路請求本來就會有的部分（例如你的 IP 位址，由我的主機服務商用來回傳檔案）。

{% endif %}{% if app.embeds %}## app 內的第三方內容

{% for key in app.embeds %}{% assign svc = site.data.privacy_services[key] %}**{{ svc.zh.name }}。**{{ svc.zh.data }}該行為適用 {{ svc.provider }} 自己的[隱私權政策]({{ svc.provider_policy }})。

{% endfor %}{% endif %}## app 不會做的事

- {% if app.account == false %}沒有註冊、沒有登入、沒有使用者帳號。{% else %}帳號相關說明見上方。{% endif %}
- 不會跟你要姓名、電子郵件、電話或付款資訊。
- 不會索取位置、通訊錄、相片、相機、麥克風或檔案的存取權限。
- 不販售也不出租資料給任何人，不含任何第三方廣告 SDK。
- 不會跨到其他公司的 app 或網站追蹤你。

## 兒童

{{ app.name }} 並非以 13 歲以下兒童為對象，我也不會在知情的情況下收集他們的資料。

## 資料保存多久、怎麼刪掉

- **你裝置上的資料：**移除 app，本機存的東西就一起消失。
- **Google 端的分析與當機資料：**依 Firebase 的保存設定（目前為預設期間）保留，且以匿名形式存放。
- **想提早刪除？**來信 [{{ site.email }}](mailto:{{ site.email }})，我會刪除可被指認的部分。由於分析資料並未綁定你的姓名或帳號，請一併提供大約的日期與裝置型號，才有辦法定位。

依你所在地區的法規，你可能享有查閱、更正、刪除個人資料或反對處理的權利，同樣寫信到上述信箱即可行使。

## 政策變更

如果 app 開始收集新的東西，這一頁會在該版本上架前先更新，最上方的生效日期也會跟著改。重大變更也會寫在 app 的更新說明裡。

## 聯絡方式

Marvin Lin — [{{ site.email }}](mailto:{{ site.email }})
{% if app.stores.play %}
[在 Google Play 上的 {{ app.name }}]({{ app.stores.play }})
{%- endif %}

---

*本政策以英文版為準；中文版為便利提供的翻譯，若有歧異，以[英文版]({{ include.en_url }})為準。*
