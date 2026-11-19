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

## Deploy
Any static host works (Netlify, Vercel, Cloudflare Pages, GitHub Pages). Upload the folder as‑is and point marketia.uk at it.
If using Netlify, the contact form can be switched to Netlify Forms by adding `data-netlify="true"` to the `<form>` and removing the mailto handler in `js/main.js`.
