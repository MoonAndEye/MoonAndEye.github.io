---
layout: single
title: "Cloudflare Tunnel: Why I Now Use It Instead of ngrok"
date: 2026-04-27 10:05 +0800
category: programming
author: Marvin Lin
tags: [Cloudflare, Cloudflare Tunnel, ngrok, Webhook, AI Agent]
lang: en
summary: "If your domain already lives on Cloudflare, Cloudflare Tunnel makes your localhost entry point feel like part of the same development and deployment flow."
---

AI agent coding helps you build features quickly, but once you move into integration testing, you run into a very practical question: how can an external service reach your local environment?

Maybe you need to receive a webhook. Maybe you want a friend to try a version that is not deployed yet. Maybe a third-party service needs to call back into your development environment.

I used to use ngrok for this. It is well known, and it is genuinely convenient. Run `ngrok http 3000`, and you get a public URL that can reach your local service.

ngrok is still very good for temporary testing.

But if this is not a one-time thing, I now more often use Cloudflare Tunnel (`cloudflared`).

The reason is not that ngrok is bad. It is that I now put my domain, Pages, and Workers on Cloudflare. If the production entry point already lives on Cloudflare, putting the development entry point there too makes the whole flow more straightforward.

If you already followed my previous post, [AI Agent Coding - Why I Recommend Cloudflare]({% post_url /programming/en/2026-04-23-ai-agent-coding-cloudflare %}), and moved your domain to Cloudflare, then Cloudflare Tunnel is almost the next natural tool to use.

## The Advantage Is Keeping Domain, Deployment, and Dev Entry Points Together

ngrok and Cloudflare Tunnel solve the same type of problem: you have a local service running on `localhost:3000`, but an external service needs a public HTTPS URL to reach it.

ngrok can do this. Cloudflare Tunnel can do this too.

I choose Cloudflare Tunnel because it fits directly into my existing Cloudflare flow.

The domain is on Cloudflare. The frontend may be on Pages. The backend may be on Workers. Now the public entry point for local development can also be managed in the same place as `dev.example.com`.

Development and deployment start to feel like the same path, instead of one setup for code, another setup for production, and a separate temporary URL for testing.

## ngrok Is Good for Temporary Testing, Cloudflare Tunnel Fits the Workflow

ngrok's biggest advantage is speed.

You do not need to buy a domain, set up DNS, or care about Cloudflare. If your local service is running on `3000`, one command gives you a public URL.

For a one-time demo, or quickly letting a friend take a look, ngrok is a good fit.

But if this development entry point keeps coming back, I want it tied to my own domain.

For example, `dev.example.com` points to the local service, `app.example.com` is production, and `api.example.com` is the Workers API. These entry points all live under Cloudflare, and DNS, HTTPS, and routing are managed in the same place.

That is why Cloudflare Tunnel feels smooth to me. It is not just another temporary tool. It brings local development into the same product infrastructure.

## Setup Is Not Hard, but Point localhost Clearly

If you create the tunnel from the Cloudflare dashboard, the flow is roughly: create a tunnel, install and run the `cloudflared` command Cloudflare gives you, then add a published application that points `dev.example.com` to `http://localhost:3000`.

If you manage it with a local config, the concept looks like this:

```bash
brew install cloudflared
cloudflared tunnel login
cloudflared tunnel create my-dev
cloudflared tunnel route dns my-dev dev.example.com
```

Then connect the hostname to your local service in `~/.cloudflared/config.yml`:

```yaml
tunnel: <TUNNEL_ID>
credentials-file: /Users/you/.cloudflared/<TUNNEL_ID>.json

ingress:
  - hostname: dev.example.com
    service: http://localhost:3000
  - service: http_status:404
```

Finally, run the tunnel:

```bash
cloudflared tunnel run my-dev
```

After that, `https://dev.example.com` reaches the service running on your machine, and HTTPS is handled by Cloudflare.

## The Difference for AI Agent Coding

AI agent coding makes it faster to build something testable.

In the past, it might take days before you reached webhooks, OAuth callbacks, or third-party integrations. Now an AI agent can help you get the feature working earlier, which means you also need a way for external services to reach local development earlier.

The value of Cloudflare Tunnel here is not that it helps AI understand your context better. The value is that your development, testing, and deployment paths become more consistent.

You can naturally treat `https://dev.example.com` as the development entry point and `https://app.example.com` as the production entry point. Both live under the same domain and the same Cloudflare account.

The benefit is that when you test a webhook, test a callback, or let someone try the product, you do not need to switch to another service just to think about the public URL.

The development entry point is part of the product architecture too. When it lives together with your domain, Pages, and Workers, the path from side project to deployment becomes clearer.

In the next post, I want to write about Cloudflare Workers AI. It lets you test AI inference on the same platform. Combined with Tunnel, Pages, and Workers, the path from development to deployment for an AI side project becomes much shorter.
