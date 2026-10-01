---
layout: single
title: "[IT 鐵人賽] Vibe Coding：30 個開發實用技巧｜找到好用的 skill，裝進你的 agent：Skills hub 與 skill installer - Tip 19"
date: 2026-10-01 13:00 +0800
category: programming
author: Marvin Lin
tags:
  - IT鐵人賽
  - 2026鐵人賽
  - Vibe Coding
  - Vibe Coding 技巧
  - Skills
  - Codex
  - Claude Code
  - Agent
summary: "我整理了用 Skills hub 尋找 skill、以 Codex skill-installer、skills.sh CLI 或 Claude Code plugin 安裝的流程，並說明如何確認安裝範圍與 agent 實際載入。"
description: "我整理了用 Skills hub 尋找 skill、以 Codex skill-installer、skills.sh CLI 或 Claude Code plugin 安裝的流程，並說明如何確認安裝範圍與 agent 實際載入。"
---
本篇也同步刊登於 [iT 鐵人賽文章](https://ithelp.ithome.com.tw/articles/10419620)。

想讓 agent 用一套現成做法，我會先找 skill。找到合適的，再裝到需要用它的專案或個人環境裡。Skills hub 是找來源的地方，skill installer 則可以幫我完成安裝。

## 為什麼

skill 通常是一個資料夾，裡面用 `SKILL.md` 寫什麼時候用、怎麼做。別人已經整理好的做法，可以先拿來試；找到之後，還要確認裝給哪個 agent、放在哪裡，他才讀得到。

## 我怎麼做

**先找來源。** skills.sh 可以找公開的 skill；anthropics/skills 有 Anthropic 的範例，Codex 的新範例看 openai/plugins；舊的 openai/skills 已標示 deprecated，裡面仍保留 skill-installer 的說明。先讀 description，確認它處理的是我要做的事，再看 `SKILL.md` 內文。

**選一種安裝方式。** 這幾個入口不用全部跑一遍：

| 入口 | 怎麼用 |
| --- | --- |
| Codex 的 `$skill-installer` | 告訴他 skill 名稱或 GitHub 目錄網址，讓他安裝 |
| skills.sh 的 CLI | 用 `npx skills add` 安裝，依提示選 skill 與目標 agent |
| Claude Code plugin | 先加入 marketplace，再安裝其中的 plugin，取得包在裡面的 skills |

skill installer 是「裝 skill 的 skill」。我把安裝需求交給他，他依說明找來源、處理目錄。像這樣：

```text
用 skill-installer 幫我安裝這個 GitHub 目錄裡的 skill：<skill 的網址>。
裝完告訴我來源、安裝路徑，以及怎麼讓目前的 agent 載入它。
同名的已經存在時，先列出差異。
```

想直接用 CLI，先找、再選要裝的內容：

```bash
npx skills find typescript
npx skills add vercel-labs/agent-skills
npx skills list
```

這支 CLI 預設裝到專案範圍；加 `-g` 是個人範圍，跨專案使用。互動安裝可以選 symlink 或 copy，實際位置依目標 agent 而定。裝完看清楚輸出的路徑。

Claude Code 透過 plugin 安裝的例子：

```text
/plugin marketplace add anthropics/skills
/plugin install example-skills@anthropic-agent-skills
```

Plugin 怎麼把多個元件包在一起，後面另有一篇。這裡先把想用的 skill 裝好。

**最後確認能用。** 看安裝結果裡的路徑與載入說明，再給他一個符合 description 的小任務，確認他有使用這份 skill。指令跑完只是安裝這一步完成。

## 坑

裝進來的 skill 是給 agent 的指示。來源要看清楚，同名的先處理；只給這個專案用的，就留在專案範圍。需要重新載入或重開 session 時，照目前工具的安裝結果做。

裝好了他卻沒用上，多半是那一行 description 跟你講話的方式對不上，他判斷用不到。這種時候直接打 `/` 加上 skill 的名字叫它，先確認這份 skill 本身有效；要他以後自己判斷得出來，就回頭把 description 改準。

## 小結

找來源、選安裝方式、確認路徑，再試一次。現成的 skill 能用起來，之後才知道哪些地方需要改成自己的做法。

明天講 skill creator，把自己常用的做法寫成 skill。

參考：
- skills.sh https://skills.sh
- vercel-labs/skills https://github.com/vercel-labs/skills
- anthropics/skills https://github.com/anthropics/skills
- openai/skills https://github.com/openai/skills
- openai/plugins https://github.com/openai/plugins
