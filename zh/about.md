---
layout: archive
title: 關於我
author_profile: true
lang: zh
---

{% if page.locale == "zh" %}
<h2>這不是英文界面 是中文界面 = zh</h2>
{% else %}
<h2>這是英文界面 locale = en</h2>
{% endif %}
<!-- 統一使用 about-content.md -->
{% include zh/about-content.md %}