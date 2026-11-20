# images

`img/` holds:
- the wordmark cut from Tia's logo sheet (`logo-dark.png`, `logo-mid.png`, `logo-light.png`)
- Tia's Drive photos (Nov 2026), converted from HEIC/DNG to JPEG at ≤1600px: `rw-*` (Rockwater Images), `lucas-*` (Luca's Images),
  `cr-*` (Images for Creators), `me-*` (4 About Me Images), `svc-ongoing` / `svc-oneoff` (Ongoing vs One off), `hero-desk` (Front Page)
- `post-*` — the photo cropped from each of her five personal‑post screenshots; each links to the real post on @tiaevaans
- photos still from her portfolio PDF: `bellagio-*`, `life-*` (lifestyle), `tia-steps`, `lucas-beach`
- `about-standing` is still a small carousel crop; swap for an original with the same filename when she has one

Spare Drive photos not currently placed: `rw-cake`, `rw-lounge`, `rw-outside`, `rw-room`, `rw-vinyl`.

# video

`video/` holds the five reels from Tia's Drive, compressed to 540p MP4 with poster JPEGs of the same name
(`boat-club-2`, `boat-club-3`, `lulas`, `midas`, `outlaw`). They play muted when scrolled into view on the work page.
To add a reel: drop `name.mp4` + `name.jpg` here and add a line to `REELS` in the generator (or copy a `<figure class="reel">` block).
The Bellagio case study on the work page has a reel slot waiting for `bellagio.mp4` (540×960 like the others); it plays as soon as the file exists.

# image slots (what each file is used for)

Every placeholder on the site is a `<div class="img ph …" data-slot="…">`. To fill one, replace it with:

```html
<div class="img r45"><img src="assets/img/FILE.jpg" alt="describe the photo"></div>
```

Keep the ratio class from the placeholder (`r45`, `r34`, `r11`, `r32` or `r169`) so the layout holds. Put files in `assets/img/`.

| page / slot                         | suggested crop | what works here                                   |
|-------------------------------------|----------------|---------------------------------------------------|
| home · hero portrait                | 4:5            | tia at work, candid, lots of cream and brown      |
| home · detail                       | 3:4            | a close detail: hands, camera, product            |
| home · bts                          | 1:1            | behind the scenes on a shoot                      |
| home · service 01 / 02              | 3:2            | management: phone and planning; content: on set   |
| work · 01 to 09                     | mixed          | editorial mix: bts, finished, details, lifestyle  |
| reel · 01 to 04                     | 9:16 stills    | a frame from each reel; the link opens the reel   |
| about · portrait / on set / detail  | 3:4, 4:5, 3:4  | tia plus process                                  |
| services · management / content day | 4:5            | one for each service                              |
| services · creator 01 to 03         | 3:4            | creator days, experiences, events                 |
| og-image.jpg                        | 1200 by 630    | social share image at `assets/og-image.jpg`       |

Also wanted: `logo.svg` if Tia has a vector of the wordmark. The site currently sets "marketia" in Cormorant Garamond.
