---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

{% if page.locale == "zh" %}
<h2>這不是英文界面 是中文界面 = zh</h2>
{% elsif page.locale == "en" %}
<h2>這是英文界面 locale = en</h2>
{% else %}
<h2>這個 locale 沒設定</h2>
{% endif %}

{% include support-for-unit-testing.html %}
{% include coffee-button.html %}
{% include paginator.html %}