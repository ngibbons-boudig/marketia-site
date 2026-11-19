# images

`img/` currently holds crops taken from Tia's Instagram carousel slides (small, roughly 200 to 900px) plus the wordmark
cut from her logo sheet (`logo-dark.png`, `logo-mid.png`, `logo-light.png`). They are fine for layout and the
smaller tiles but will look soft at hero and gallery size: swap each for the full-resolution original from the
Google Drive when it arrives, keeping the same filename so nothing in the HTML needs to change.

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
