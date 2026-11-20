# marketia.uk

Static site for marketia (Tia) — social media management & content creation, Dorset.

- `index.html` home · `about.html` · `services.html` · `work.html` · `contact.html`
- `css/style.css`, `js/main.js` — styling, scroll reveals, mobile nav, reels, the enquiry form, the font preview switch
- `assets/` — drop Tia's photos here; `assets/README.md` lists every image slot by name
- `BRIEF.md` — what was collated from @markettiaa plus Tia's own brief
- `FEEDBACK.md` — Tia's round‑1 feedback, what was done and what's still waiting on her

Header and footer are repeated in each page, so a nav change means editing all five files.
Service buttons link to `contact.html?service=management|content|creator#enquiry`, which pre‑ticks the matching box and scrolls to the form.

**Font preview:** add `?fonts=bodoni` or `?fonts=playfair` to any page URL to try the alternative pairings (default is Cormorant Garamond + DM Sans). A small switcher appears bottom‑left; `?fonts=off` clears it. The five pages are generated from `tools/gen.py` (all copy and image placements live there): edit it, run `python3 tools/gen.py`, commit the HTML it writes.

## Run locally
```bash
python3 -m http.server 8765
```
then open http://localhost:8765

## Hosting

Hosted on **GitHub Pages** from the `main` branch of
https://github.com/ngibbons-boudig/marketia-site (root folder, `CNAME` = marketia.uk).
Every push to `main` redeploys within a minute or two.

**Preview (until DNS is done):** https://ngibbons-boudig.github.io/marketia-site/
The `CNAME` file is removed for now so this preview URL works. Once GoDaddy DNS points at GitHub Pages,
restore it with `echo marketia.uk > CNAME`, commit and push; the preview URL will then redirect to marketia.uk.

## DNS at GoDaddy (one‑off)

The domain's nameservers are GoDaddy's (`ns25/ns26.domaincontrol.com`). In GoDaddy → My Products → marketia.uk → **DNS**:

1. Delete the existing parking records: the `A` record for `@` (currently 76.223.67.189 / 13.248.213.45) and any **Forwarding** rule for the domain.
2. Add four `A` records, name `@`, TTL 600:
   - `185.199.108.153`
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`
3. Add a `CNAME` record, name `www`, value `ngibbons-boudig.github.io`.
4. (Optional, IPv6) `AAAA` records for `@`: `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`.

Then in the repo → Settings → Pages, wait for the DNS check to pass and tick **Enforce HTTPS** (the certificate is issued automatically, usually within an hour).

## Contact form

The form posts from the page to **formsubmit.co**, which emails each enquiry to hello@marketia.uk (no account needed).
**First‑time activation:** the first submission triggers an email to hello@marketia.uk with an "Activate" link; click it once
and every later enquiry arrives straight away. If the send ever fails, the page opens the visitor's email app with everything
filled in, so nothing is lost. To change the destination address, edit the form's `action` in `contact.html` (via the generator).
