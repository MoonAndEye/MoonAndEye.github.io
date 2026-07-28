---
layout: single
title: "Agent Build Log — Episode 015"
date: 2026-07-28 23:36:15 +0800
category: programming
author: Marvin Lin
tags: [agent]
lang: en
image: /assets/programming/agent-build-log/agent-build-log-episode-015.png
summary: "I traced a packaged Desktop App OAuth failure through the Electron bundle, duplicate pi-ai modules, a stale process, and credential lifecycle handling."
description: "I traced a packaged Desktop App OAuth failure through the Electron bundle, duplicate pi-ai modules, a stale process, and credential lifecycle handling."
---

Today, I enabled OAuth, and the Desktop App immediately broke.

![Agent Build Log Episode 015: tracing the Desktop App OAuth failure](/assets/programming/agent-build-log/agent-build-log-episode-015.png)

The screen only showed:

> Desktop agent did not produce an answer

At first, I thought the login had failed. It could also have been a problem with the token, the model, or the account.

But the real error happened much earlier.

Pi failed while preparing the OAuth auth for the model request, and the token usage was 0. That meant the prompt had never even been sent to the model.

The first problem was in the packaged Desktop App.

The OAuth flow that loaded correctly in the development environment could not find the corresponding file inside the Electron production bundle. The entire process stopped before OAuth could obtain the request auth.

I added an OAuth loader, and the source-level test passed.

But the packaged app was still broken.

Later, I discovered that the workspace actually contained two copies of the pi-ai module.

I registered the loader in one copy, but the Pi ModelRuntime that actually ran the model was using the other one.

Their loader registries were not shared.

So it looked like I had fixed the problem, but the runtime actually executing the model never received that fix.

I fixed the module identity and bundle issues, packaged the app again, and ran another test.

The screen still showed the same error.

This time, the real cause was even more absurd: the Mac was still running an old Desktop process that had been launched before the fix.

The App on disk had been updated, but the old process in memory would not automatically turn into the new version.

So what I was seeing was not “the new fix still fails.” It was “the old program is still running.”

While working through these problems, I found another risk.

The CLI and Desktop share the same OAuth credential, but once the Desktop worker starts, it keeps the auth in memory.

If the CLI logs in again or refreshes the token, the already-running Desktop may not immediately load the new credential.

So I also added credential lifecycle handling.

Before sending a prompt, Desktop now checks the auth again. When the auth file changes, the Mac resumes from sleep, or the worker becomes stale, it rebuilds the worker before the next operation and reloads the credential and DKS connection.

I also changed the UI error message.

From now on, it will no longer collapse every problem into the same Desktop agent did not produce an answer message. It will prioritize the actual OAuth error returned by Pi.

Finally, the packaged Desktop App successfully received a pong response.
