# Custom domain setup: ai-survival-guide.forbunnies.com

This repo is configured to serve from `ai-survival-guide.forbunnies.com` (the `CNAME` file already contains it). You need to do two one-time things: point DNS at GitHub Pages, and confirm the settings in GitHub.

## 1. Add the DNS record at your domain provider

`ai-survival-guide` is a subdomain of `forbunnies.com`, so use a **CNAME record** (not an A record).

In your DNS provider's dashboard for `forbunnies.com`, add:

| Type  | Name (Host)          | Value / Target          | TTL     |
| ----- | -------------------- | ----------------------- | ------- |
| CNAME | `ai-survival-guide`  | `sunnykgupta.github.io` | Auto / 3600 |

Notes:
- Some providers want the full subdomain in "Name" (`ai-survival-guide.forbunnies.com`) and some want just `ai-survival-guide`. Use whatever your provider expects for a subdomain.
- The target is your GitHub Pages host: `sunnykgupta.github.io` (note: **no** repo path, **no** `https://`, and it ends with a dot in some UIs).
- Do not add a trailing `/AI-Survival-Guide`. GitHub maps the custom domain to this repo automatically because of the `CNAME` file.

If you ever want the apex domain `forbunnies.com` itself (you don't here), that would need A records instead. For this subdomain, a single CNAME is correct.

## 2. Confirm GitHub Pages settings

In the repo on GitHub: **Settings → Pages**

- **Source:** GitHub Actions (already used by the deploy workflow).
- **Custom domain:** `ai-survival-guide.forbunnies.com` (this auto-populates from the `CNAME` file after the first deploy; if it is blank, type it and click Save).
- **Enforce HTTPS:** check this box once the certificate is issued (can take a few minutes to an hour after DNS resolves).

## 3. Verify

After DNS propagates (usually minutes, sometimes up to a few hours):

```bash
dig +short ai-survival-guide.forbunnies.com
# should resolve toward sunnykgupta.github.io / GitHub Pages IPs
```

Then open https://ai-survival-guide.forbunnies.com and it should show the guide.

## Troubleshooting

- **"Domain does not resolve to the GitHub Pages server"**: DNS hasn't propagated yet, or the CNAME target is wrong. It must be `sunnykgupta.github.io`.
- **HTTPS unavailable / certificate error**: wait for the certificate to provision, then enable "Enforce HTTPS".
- **404 after deploy**: make sure the Pages source is "GitHub Actions" and the latest deploy workflow succeeded (Actions tab).
