# marketia.uk

Static one‑page site for marketia (Tia) — social media management & content creation, Dorset.

- `index.html` — the page
- `css/style.css`, `js/main.js` — styling and small enhancements (mobile nav, mailto contact form)
- `assets/` — drop Tia's logo and photos here (see `assets/README.md`)
- `BRIEF.md` — everything collated from @markettiaa that informed the copy and design

## Run locally
```bash
python3 -m http.server 8765
```
then open http://localhost:8765

## Hosting

Hosted on **GitHub Pages** from the `main` branch of
https://github.com/ngibbons-boudig/marketia-site (root folder, `CNAME` = marketia.uk).
Every push to `main` redeploys within a minute or two.

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

The form currently opens the visitor's email app addressed to hello@marketia.uk, so it works without a backend.
To receive submissions directly instead, point the form at a service such as Formspree and remove the mailto handler in `js/main.js`.
