---
layout: archive
title: About Me
author_profile: true
lang: en
---
{% if page.lang == "zh" %}
<h2>這不是英文界面 是中文界面 = zh</h2>
{% else %}
<h2>這是英文界面 locale = en</h2>
{% endif %}

<!-- 統一使用 about-content.md -->
{% include en/about-content.md %}