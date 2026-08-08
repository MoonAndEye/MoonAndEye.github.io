---
layout: single
title: Privacy Policy
description: "Privacy policies for Marvin Lin's mobile apps and for the Marvin Builds tools on marvinswift.com, covering the TikTok publishing workflow, OAuth tokens, analytics, and contact details."
permalink: /privacy/
lang: en
author_profile: true
share: false
comments: false
toc: false
last_modified_at: 2026-08-08
---

Everything I publish — the apps and this website — is built and operated by me, Marvin Lin, an individual developer in Taiwan. Each app has its own policy below, because each one collects different things. Questions about any of them: [{{ site.email }}](mailto:{{ site.email }}).

## App privacy policies

{% for entry in site.data.apps %}{% assign app = entry[1] %}- **{{ app.name }}**{% if app.platforms %} ({{ app.platforms | join: ", " }}){% endif %} — [English](/privacy/{{ entry[0] }}/) · [繁體中文](/privacy/{{ entry[0] }}/zh/)
{% endfor %}

## Website and Marvin Builds tools

This Privacy Policy explains how Marvin Builds tools and integrations operated by Marvin Lin through marvinswift.com handle information, including the TikTok publishing workflow used for the MarvinBuildsAI account.

The TikTok integration is used by the account owner to authorize access and upload finished video content. It may process TikTok account authorization data, basic TikTok account information, video files, captions, and upload status information that are necessary to publish or manage the upload workflow.

OAuth tokens and upload metadata are used only to operate the publishing workflow for the authorized account. They are not sold or shared with advertisers. Video content and metadata submitted to TikTok are handled by TikTok according to TikTok's own terms and privacy policy.

This website may use standard analytics tools to understand site traffic and improve content. Analytics data is used in aggregate and is not used to identify individual visitors.

If you want to ask about privacy or request removal of information related to this workflow, contact Marvin Lin at atimis19@gmail.com.
