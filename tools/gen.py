import os
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IG = "https://www.instagram.com/markettiaa/"
IG_PERSONAL = "https://www.instagram.com/tiaevaans/"
POSTS = {
  "welcome": "https://www.instagram.com/p/Df5Pmn0oMep/",
  "tease":   "https://www.instagram.com/p/DfpyFEXxtR0/",
  "together":"https://www.instagram.com/p/DfnRIOOKD3a/",
  "coming":  "https://www.instagram.com/p/DfkvcrPK76U/",
}
# tia's personal posts for "the personal collection" (about page)
PERSONAL = [
  ("https://www.instagram.com/p/De9-5POCrI-/", "post-cotswolds.jpg", "a greengrocer’s display in the Cotswolds", "the cotswolds"),
  ("https://www.instagram.com/p/DX49EO8ikml/", "post-carbone.jpg",   "Tia in a white blazer on the steps outside Carbone, London", "carbone, london"),
  ("https://www.instagram.com/p/DXxJn5-DFqM/", "post-nonotes.jpg",   "a wall of records lit in red", "no notes"),
  ("https://www.instagram.com/p/DMKl6hURTDH/", "post-bondi.jpg",     "swimmers looking out over Bondi Beach", "bondi beach"),
  ("https://www.instagram.com/p/DS5hlqaCl_Y/", "post-2025.jpg",      "a collage of moments from 2025", "2025"),
]
NAV = [("index.html","home"),("about.html","about"),("services.html","services"),("work.html","work"),("contact.html","contact")]
LOGO = '<img src="assets/img/logo-dark.png" alt="marketia" width="693" height="160">'
FONTS = "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;1,9..40,400&display=swap"

def embed(url, text):
    return f'<blockquote class="instagram-media" data-instgrm-permalink="{url}" data-instgrm-version="14"><a href="{url}" target="_blank" rel="noopener">{text}</a></blockquote>'

def img(cls, file, alt, pos="", lazy=True, inner=""):
    st = f' style="object-position:{pos}"' if pos else ''
    lz = ' loading="lazy"' if lazy else ''
    return f'<div class="img {cls}"><img src="assets/img/{file}" alt="{alt}"{lz}{st}>{inner}</div>'

def phone(embeds):
    """an iphone-style frame with the instagram embed(s) scrolling inside"""
    return f'''<div class="phone" data-reveal>
          <div class="phone-notch"></div>
          <div class="screen">{"".join(embeds)}</div>
          <div class="phone-bar"></div>
        </div>'''

def shell(page, title, desc, body):
    CUR = ' aria-current="page"'
    links = "".join(f'<a href="{h}"{CUR if h==page else ""}>{t}</a>' for h,t in NAV)
    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://marketia.uk/assets/og-image.jpg">
  <meta name="theme-color" content="#f7f4ef">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link id="fonts" href="{FONTS}" rel="stylesheet">
  <script>document.documentElement.classList.add("js");try{{var f=new URLSearchParams(location.search).get("fonts")||localStorage.getItem("fonts");if(f)document.documentElement.setAttribute("data-fonts",f)}}catch(e){{}}</script>
  <link rel="stylesheet" href="css/style.css">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' fill='%23f7f4ef'/%3E%3Ctext x='32' y='44' text-anchor='middle' font-family='Georgia,serif' font-size='36' fill='%23493127'%3Em%3C/text%3E%3C/svg%3E">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<header class="site-header">
  <div class="wrap nav-row">
    <a class="wordmark" href="index.html" aria-label="marketia home">{LOGO}</a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav"><span></span><span></span><span class="visually-hidden">Menu</span></button>
    <nav id="site-nav" class="site-nav">
      {links}
      <a class="btn" href="contact.html#enquiry">enquire</a>
    </nav>
  </div>
</header>

<main id="main">
{body}
</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="wordmark" href="index.html">{LOGO}</a>
        <p class="footer-tag">behind the content, behind the brands.</p>
      </div>
      <div>
        <p class="label">explore</p>
        <ul>
          <li><a href="about.html">about</a></li>
          <li><a href="services.html">services</a></li>
          <li><a href="work.html">work</a></li>
          <li><a href="contact.html">contact</a></li>
        </ul>
      </div>
      <div>
        <p class="label">say hello</p>
        <ul>
          <li><a href="mailto:hello@marketia.uk">hello@marketia.uk</a></li>
          <li><a href="tel:+447538963391">07538 963391</a></li>
          <li><a href="{IG}" target="_blank" rel="noopener">@markettiaa</a></li>
        </ul>
      </div>
      <div>
        <p class="label">based</p>
        <ul>
          <li>Dorset, UK</li>
          <li>available across the UK</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="year"></span> marketia</span>
      <span>social media management · content creation · photography · videography</span>
    </div>
  </div>
</footer>

<script async src="https://www.instagram.com/embed.js"></script>
<script src="js/main.js"></script>
</body>
</html>
'''

def cta(h, p, label="start an enquiry", href="contact.html#enquiry"):
    return f'''
  <section class="section choc">
    <div class="wrap cta-band" data-reveal>
      <div>
        <p class="label">let’s talk</p>
        <h2 class="h-l">{h}</h2>
        <p>{p}</p>
      </div>
      <div class="actions"><a class="btn light" href="{href}">{label}</a></div>
    </div>
  </section>'''

def ig_section(num, keys, cream=False):
    return f'''
  <section class="section{" cream" if cream else ""}">
    <div class="wrap">
      <div class="ig-head" data-reveal>
        <div>
          <p class="label num" data-num="{num}">latest on instagram</p>
          <h2 class="h-l" style="margin:0">@markettiaa</h2>
        </div>
        <a class="textlink" href="{IG}" target="_blank" rel="noopener">follow along</a>
      </div>
      <div class="phone-wrap">
        {phone([embed(POSTS[k], t) for k,t in keys])}
        <div class="phone-aside" data-reveal>
          <p class="lede">A little look at what’s happening over on Instagram. Behind the scenes, new work and the people I get to work with.</p>
          <a class="btn" href="{IG}" target="_blank" rel="noopener">open instagram</a>
        </div>
      </div>
    </div>
  </section>'''

# ------------------------------------------------------------------ HOME
home = f'''
  <section class="hero">
    <div class="wrap hero-grid">
      <div>
        <p class="label">social media management · content creation</p>
        <h1 class="h-xl hero-title">behind the content,<span class="l2">behind the brands.</span></h1>
        <p class="lede">iPhone‑led content for businesses, brands and creators. The moments, details and stories behind what you do, captured through a creative lens.</p>
        <div class="hero-actions">
          <a class="btn solid" href="contact.html#enquiry">work with me</a>
          <a class="textlink" href="work.html">see the work</a>
        </div>
      </div>
      <div class="hero-art">
        {img("r45","hero-desk.jpg","Tia at her desk in the marketia studio",lazy=False)}
        <div class="side">
          {img("r34","lucas-drink.jpg","an iced pink drink from Luca’s held up in the sun")}
          {img("r11","rw-decks.jpg","DJ decks set up on the terrace at Rockwater Village","center 60%")}
        </div>
      </div>
    </div>
    <div class="wrap hero-foot">
      <span>est. 2026 · dorset</span>
      <span><a href="{IG}" target="_blank" rel="noopener" style="text-decoration:none;color:inherit">@markettiaa</a></span>
    </div>
  </section>

  <section class="section tight">
    <div class="wrap">
      <div class="notes" data-stagger>
        <div class="note">
          <h3>shot on iphone, on purpose.</h3>
          <p>Content that feels current and real, made the way people actually watch it. From behind‑the‑scenes moments on a busy set to the little details that bring a brand to life, it’s all about capturing things from a different perspective.</p>
        </div>
        <div class="note">
          <h3>the people behind the brand.</h3>
          <p>Every business has its own personality, and that’s what I want the content to show. The people, the atmosphere, the little details and everything that makes a brand what it is.</p>
        </div>
        <div class="note">
          <h3>from the first idea to the final edit.</h3>
          <p>Whether I’m managing your socials or coming in for a content shoot, I take care of the creative process. From planning and filming to editing and bringing everything together, so you have content that feels right for your brand and is ready to use.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <div>
          <p class="label num" data-num="01">selected work</p>
          <h2 class="h-l">a few <em>highlights</em>.</h2>
        </div>
        <p class="muted">A selection of brands, projects and moments I’ve had the pleasure of working on. From ongoing social media management and content creation to events, campaigns and one‑off shoots. A little look at the work, the people and the ideas behind it.</p>
      </div>
      <div class="edit-grid" data-stagger>
        <a class="work-link zoom span5" href="work.html#rockwater">{img("r45","rw-terrace.jpg","the beachfront dining terrace at Rockwater Village")}<figcaption>rockwater village · <em>events</em></figcaption></a>
        <a class="work-link zoom span3 down" href="work.html#bellagio">{img("r34","bellagio-dining.jpg","two guests with pizza and pasta at Bellagio Pizzeria")}<figcaption>bellagio pizzeria · <em>management</em></figcaption></a>
        <a class="work-link zoom span4" href="work.html#lucas">{img("r11","lucas-beach.jpg","a customer biting into a sandwich on the beach","center 20%")}<figcaption>luca’s takeaway café · <em>management</em></figcaption></a>
        <a class="work-link zoom span4 down" href="work.html#rockwater">{img("r34","rw-breakfast.jpg","a sunlit breakfast table at Rockwater Village")}<figcaption>rockwater village · <em>content</em></figcaption></a>
        <a class="work-link zoom span4" href="services.html#creators">{img("r45","cr-robes.jpg","four friends in robes on a boat deck","center 40%")}<figcaption>creator content · <em>days out</em></figcaption></a>
        <a class="work-link zoom span4 down" href="work.html#lifestyle">{img("r11","life-pool.jpg","swimmers in the sea pool at Bondi")}<figcaption>lifestyle · <em>sydney</em></figcaption></a>
      </div>
      <p style="margin-top:3rem"><a class="textlink" href="work.html">view the full portfolio</a></p>
    </div>
  </section>

  <section class="section cream">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <div>
          <p class="label num" data-num="02">services</p>
          <h2 class="h-l">two ways to <em>work together</em>.</h2>
        </div>
        <p class="muted">Ongoing social media support or a one‑off content day. Two ways to bring fresh ideas and great content to your brand.</p>
      </div>
      <div class="grid-2" data-stagger>
        <div>
          {img("r32","svc-ongoing.jpg","the team behind the counter at Luca’s takeaway café","center 40%")}
          <h3 class="h-m" style="margin-top:1.4rem">social media management</h3>
          <p class="muted measure">I take care of your social media from the initial content planning through to filming, editing and publishing. Whether you need support with Instagram, Facebook, TikTok or a combination of platforms, we can tailor the management to suit your brand and what you want to achieve.</p>
          <a class="textlink" href="services.html#management">about management</a>
        </div>
        <div>
          {img("r32","svc-oneoff.jpg","a blue display of Summer Fridays magazines at a pop‑up","center 50%")}
          <h3 class="h-m" style="margin-top:1.4rem">content creation</h3>
          <p class="muted measure">From half or full‑day shoots to campaigns, events and brand experiences. I capture and edit a collection of photo and video content tailored to your business, ready to use across your social channels. Perfect for a one‑off refresh or regular content days throughout the year.</p>
          <a class="textlink" href="services.html#content">about content days</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <div>
          <p class="label num" data-num="03">results</p>
          <h2 class="h-l">content that <em>gets seen</em>.</h2>
        </div>
        <p class="muted">A look at the impact of ongoing social media management across two very different brands. From reaching new audiences to building engaged communities, here’s a snapshot of what’s happening behind the content.</p>
      </div>
      <div class="stats" data-stagger>
        <div class="stat"><b>226.8k</b><span>views in 90 days</span><small>Luca’s</small></div>
        <div class="stat"><b>114k</b><span>reel views in 90 days</span><small>Luca’s</small></div>
        <div class="stat"><b>62.1%</b><span>views from non‑followers</span><small>Bellagio</small></div>
        <div class="stat"><b>+385</b><span>net new followers in 90 days</span><small>Luca’s</small></div>
      </div>
    </div>
  </section>

  {ig_section("04", [("welcome","welcome to marketia — view on instagram"),("tease","one final tease — view on instagram"),("together","it’s all coming together — view on instagram")])}

  {cta("got something worth <em>capturing</em>?","Tell me more about what you are looking for…")}
'''

# ------------------------------------------------------------------ ABOUT
about = f'''
  <section class="page-intro">
    <div class="wrap">
      <p class="label">about</p>
      <div class="split">
        <h1 class="h-xl">the one behind <em>the camera</em>.</h1>
        <p class="lede">I’m Tia, the founder of marketia. I capture the moments, details and stories behind businesses, brands and creators.</p>
      </div>
    </div>
  </section>

  <section class="section tight">
    <div class="wrap collage" data-stagger>
      {img("r34","hero-desk.jpg","Tia at her desk in the studio")}
      {img("r34","tia-steps.jpg","Tia sitting on a doorstep in a white blazer","center 30%")}
      {img("r34","about-standing.jpg","Tia standing with her laptop in the studio","center 85%")}
    </div>
  </section>

  <section class="section">
    <div class="wrap story">
      <div data-reveal>
        <p class="label num" data-num="01">the story</p>
        <h2 class="h-l">how marketia <em>came to be</em>.</h2>
      </div>
      <div class="copy" data-reveal>
        <p>I’ve always been the friend who documents absolutely everything. The one making everyone redo their cheers for the perfect shot, forever running out of storage at dinner and getting chased for the photos the morning after. I’ve always loved capturing the little details, the atmosphere and the moments you want to remember.</p>
        <p>Living in Sydney for two years was a huge part of my journey. It’s where I really fell in love with content creation, made friends for life working in the creative industry and found myself surrounded by people who continue to inspire, motivate and support me, even from the other side of the world. I also started sharing more of my own life online, documenting my Australian adventure and growing my personal brand along the way. It made me realise that something I’d always loved could become something much more.</p>
        <p>In December 2025, I moved back home to Dorset with a new perspective and a real desire to turn that passion into a career of my own. Since then, I’ve had the chance to work with some incredible local businesses, creators and brands. Whether it’s ongoing social media management, a one‑off content shoot or bringing a campaign to life, no two projects are quite the same.</p>
        <p>Marketia is my own creative brand and a place to bring all of my work together. A little look at the brands I work with, the content I create, the projects I’m part of and everything that happens behind the scenes. It’s where I share what I do, how I do it and the people I get to do it with.</p>
        <div class="then-now" data-stagger>
          {img("","me-friends.jpg","Tia and friends on a sunny morning in Sydney","center 30%")}
          {img("","me-queenstown.jpg","Tia on a balcony above the lake in Queenstown","center 40%")}
          {img("","me-opera.jpg","Tia walking past the Sydney Opera House","center 30%")}
          {img("","me-sea.jpg","swimmers in turquoise water seen from above")}
        </div>
      </div>
    </div>
  </section>

  <section class="section cream">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <div>
          <p class="label num" data-num="02">off duty</p>
          <h2 class="h-l">the personal <em>collection</em>.</h2>
        </div>
        <div>
          <p class="muted">A glimpse into my own Instagram, where I share the places I go, the things I love and the moments I can’t help but capture. A little more of my personal style, creative eye and the inspiration behind the content I create.</p>
          <a class="textlink" href="{IG_PERSONAL}" target="_blank" rel="noopener">@tiaevaans</a>
        </div>
      </div>
      <div class="posts" data-stagger>
        {"".join(f'<a class="post zoom" href="{u}" target="_blank" rel="noopener" aria-label="open this post on instagram">{img("r45",f,a)}<figcaption><em>{c}</em><span>view post</span></figcaption></a>' for u,f,a,c in PERSONAL)}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="ig-head" data-reveal>
        <div>
          <p class="label num" data-num="03">from the feed</p>
          <h2 class="h-l" style="margin:0">welcome to <em>marketia</em></h2>
        </div>
        <a class="textlink" href="{IG}" target="_blank" rel="noopener">@markettiaa</a>
      </div>
      <div class="phone-wrap">
        {phone([embed(POSTS["welcome"],"welcome to marketia — view on instagram")])}
        <div class="phone-aside" data-reveal>
          <p class="lede">The post that started it all. Follow along for new work, behind the scenes and the odd very good coffee.</p>
          <a class="btn" href="{IG}" target="_blank" rel="noopener">follow @markettiaa</a>
        </div>
      </div>
    </div>
  </section>

  {cta("i’d love to hear <em>your story</em>.","Tell me about your business, campaign or event and we’ll work out the best way to capture it.")}
'''

# ------------------------------------------------------------------ SERVICES
services = f'''
  <section class="page-intro">
    <div class="wrap">
      <p class="label">services</p>
      <div class="split">
        <h1 class="h-xl">two ways to <em>work together</em>.</h1>
        <p class="lede">Ongoing social media management, with everything taken care of from planning and content creation to editing, captions, scheduling and publishing. Or, book a dedicated content day and receive a collection of edited photos and videos, ready for you to use across your own channels.</p>
      </div>
    </div>
  </section>

  <section class="section tight">
    <div class="wrap">
      <article id="management" class="service-split">
        {img("r45","svc-ongoing.jpg","the team behind the counter at Luca’s takeaway café")}
        <div class="service-copy" data-reveal>
          <p class="label num" data-num="01">ongoing</p>
          <h2 class="h-l">social media <em>management</em></h2>
          <p>For businesses looking for someone to take care of their social media week in, week out. I plan, film, edit, write and publish across Instagram, Facebook and TikTok, so your channels stay consistent, current and engaging while you get on with running the business.</p>
          <ul class="includes">
            <li>Instagram, Facebook &amp; TikTok</li>
            <li>monthly content planning</li>
            <li>reels, feed posts &amp; stories</li>
            <li>filming &amp; editing</li>
            <li>personalised captions</li>
            <li>scheduling &amp; publishing</li>
            <li>community engagement</li>
            <li>keeping your brand consistent &amp; on‑brand</li>
          </ul>
          <div class="service-meta long">
            <div>working together<b>Minimum 3‑month commitment, followed by an ongoing monthly arrangement.</b></div>
            <div>good for<b>Cafés, restaurants, hospitality venues, lifestyle brands and independent businesses looking for consistent social media management and a stronger online presence.</b></div>
            <div>status<b>Currently taking on new clients.</b></div>
          </div>
          <div class="actions">
            <a class="btn solid" href="contact.html?service=management#enquiry">enquire about management</a>
            <a class="textlink" href="work.html#lucas">see the results</a>
          </div>
        </div>
      </article>

      <article id="content" class="service-split">
        {img("r45","svc-oneoff.jpg","a blue display of Summer Fridays magazines at a pop‑up")}
        <div class="service-copy" data-reveal>
          <p class="label num" data-num="02">one‑off or regular</p>
          <h2 class="h-l">content <em>creation</em></h2>
          <p>Hire me for a few hours or a full day. I come in, capture your business, campaign or event, and leave you with a selection of edited photo and video content ready to use across your socials.</p>
          <ul class="includes">
            <li>half‑day &amp; full‑day content shoots</li>
            <li>short‑form video &amp; reels, filmed and edited</li>
            <li>photography: product, space, team &amp; lifestyle</li>
            <li>bulk content banks for your socials</li>
            <li>behind‑the‑scenes for campaigns, launches &amp; events</li>
            <li>creator days: experiences, events &amp; everything between</li>
            <li>creative concepts &amp; content ideas</li>
            <li>delivered ready to post</li>
          </ul>
          <div class="service-meta">
            <div>format<b>half day · full day</b></div>
            <div>good for<b>businesses, brands &amp; creators</b></div>
            <div>delivery<b>edited &amp; ready to post</b></div>
          </div>
          <div class="actions">
            <a class="btn solid" href="contact.html?service=content#enquiry">enquire about a content day</a>
            <a class="textlink" href="work.html#rockwater">see a shoot day</a>
          </div>
        </div>
      </article>
    </div>
  </section>

  <section class="section cream">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <div>
          <p class="label num" data-num="03">how it works</p>
          <h2 class="h-l">from <em>hello</em> to handover.</h2>
        </div>
        <p class="muted">Every collaboration starts with understanding your business, what you’re looking for and how I can help. From there, we’ll put a plan together that works for you and your brand.</p>
      </div>
      <div class="steps" data-stagger>
        <div class="step">
          <h3>let’s talk</h3>
          <p>Send over an enquiry with a little about you and/or your business, what you have in mind and the support you’re looking for. We’ll arrange a call to talk through your ideas, goals and what you’d like to achieve.</p>
        </div>
        <div class="step">
          <h3>the plan</h3>
          <p>Once I’ve got a feel for what you’re looking for, I’ll put together a tailored proposal outlining the approach, services, pricing and creative direction. We’ll agree on the details, confirm everything and get things underway.</p>
        </div>
        <div class="step">
          <h3>let’s get creating</h3>
          <p>For ongoing management, we’ll work through onboarding, content planning, brand direction and the upcoming content calendar before getting started. For content days, we’ll agree on the shoot plan, timings and everything to be captured before the day itself. From there, I’ll take care of the content creation, editing and delivery, or manage your socials from planning through to publishing.</p>
        </div>
      </div>
      <div class="pricing" data-reveal>
        <p class="label">pricing</p>
        <p class="measure">Pricing is tailored to each business and what it needs. Management packages are based on the platforms, posting frequency and volume of content; shoot days are priced on the hours needed and the amount of content to be produced. Send an enquiry and I’ll put a simple quote together.</p>
      </div>
    </div>
  </section>

  <section id="creators" class="section">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <div>
          <p class="label num" data-num="04">creators</p>
          <h2 class="h-l">for creators, <em>too</em>.</h2>
        </div>
        <div>
          <p class="muted">Creator‑led content that brings your brand, experiences and everyday moments to life. From lifestyle and travel to events, collaborations and brand partnerships, I capture the details and experiences that make content feel natural, personal and immersive.</p>
          <a class="textlink" href="contact.html?service=creator#enquiry">enquire as a creator</a>
        </div>
      </div>
      <div class="grid-3" data-stagger>
        {img("r34","cr-sofa.jpg","a creator reclining on a red velvet sofa","center 40%")}
        {img("r34","cr-group.jpg","four friends dressed up on a red velvet sofa")}
        {img("r34","cr-door.jpg","a creator in cream standing in a grand doorway")}
        {img("r34","cr-detail.jpg","a detail of a cream outfit and a crochet bag")}
        {img("r34","cr-bag.jpg","a creator with a canvas holdall looking out to sea")}
        {img("r34","cr-robes.jpg","four friends in robes with champagne on a boat")}
      </div>
    </div>
  </section>
'''

# ------------------------------------------------------------------ WORK

REELS = [
  ("boat-club-2", "The Boat Club"),
  ("boat-club-3", "The Boat Club"),
  ("lulas",       "Lula’s"),
  ("midas",       "Midas"),
  ("outlaw",      "Outlaw"),
]
def reel(slug, name):
    return f'''<figure class="reel">
          <div class="img"><video muted loop playsinline preload="none" poster="assets/video/{slug}.jpg"><source src="assets/video/{slug}.mp4" type="video/mp4"></video>
          <button class="sound" type="button" aria-pressed="false" aria-label="toggle sound for the {name} reel">sound</button></div>
          <figcaption><em>{name}</em></figcaption>
        </figure>'''

def case(id_, num, kind, handle, title, copy, stats, mosaic):
    stat_html = ""
    if stats:
        stat_html = '<div class="stats small" data-stagger>' + "".join(f'<div class="stat"><b>{b}</b><span>{s}</span><small>{t}</small></div>' for b,s,t in stats) + '</div>'
    return f'''
      <article id="{id_}" class="case">
        <div class="case-head" data-reveal>
          <div>
            <p class="label num" data-num="{num}">{kind}</p>
            <h2 class="h-l">{title}</h2>
          </div>
          <div>
            <p class="muted">{copy}</p>
            <a class="textlink" href="https://www.instagram.com/{handle}/" target="_blank" rel="noopener">@{handle}</a>
          </div>
        </div>
        {stat_html}
        <div class="mosaic" data-stagger>
          {mosaic}
        </div>
      </article>'''

# bellagio: a reel slot at the top of the mosaic, waiting for the file (assets/video/bellagio.mp4 + .jpg)
BELLAGIO_REEL = '''<figure class="reel m-a reel-slot">
            <div class="img"><video muted loop playsinline preload="metadata"><source src="assets/video/bellagio.mp4" type="video/mp4"></video>
            <button class="sound" type="button" aria-pressed="false" aria-label="toggle sound for the Bellagio reel">sound</button>
            <span class="slot-note"><em>bellagio</em>reel coming soon</span></div>
          </figure>'''

work = f'''
  <section class="page-intro">
    <div class="wrap">
      <p class="label">work</p>
      <div class="split">
        <h1 class="h-xl">the <em>portfolio</em>.</h1>
        <p class="lede">A collection of content, campaigns and creative collaborations across hospitality, lifestyle and local brands. From social media management and photography to reels, events and behind‑the‑scenes moments, each project brings its own ideas, personality and creative direction.</p>
      </div>
    </div>
  </section>

  <section id="reels" class="section tight cream">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <div>
          <p class="label num" data-num="01">reels</p>
          <h2 class="h-l">in <em>motion</em>.</h2>
        </div>
        <p class="muted">Short‑form video is at the heart of my creative work. From the initial idea and filming to editing, sound and final touches, I create reels that capture the personality of a brand, tell a story and bring its world to life.</p>
      </div>
      <div class="reels" data-stagger>
        {"".join(reel(*r) for r in REELS)}
      </div>
    </div>
  </section>

  <section class="section tight">
    <div class="wrap">
{case("rockwater","02","event photography &amp; content · collaboration","rockwatervillagepoole",
      "rockwater <em>village</em>",
      "I captured content across various events and experiences at Rockwater Village, from the atmosphere and guest experiences to food, drinks and the venues themselves. Selected photography and content were then shared across the brand’s social media channels.",
      None,
      img("r45 m-a","rw-terrace.jpg","the beachfront dining terrace at Rockwater Village") +
      img("r34 m-b","rw-spritz.jpg","two aperol spritzes being served at the bar") +
      img("r34 m-c","rw-overhead.jpg","plates of food shot from above") +
      img("r34 m-d","rw-breakfast.jpg","a sunlit breakfast table") +
      img("r34 m-e","rw-tequila.jpg","tequila bottles on ice") +
      img("r32 m-f","rw-table.jpg","a laid table in the restaurant") +
      img("r34 m-g","rw-event.jpg","guests at a talk on the terrace") +
      img("r34 m-h","rw-decks.jpg","DJ decks set up with a sea view")
)}
{case("lucas","03","social media management","lucastakeawaycafe",
      "luca’s takeaway <em>café</em>",
      "Ongoing social media management, from content planning and capturing footage to editing, creating and publishing reels, stories and posts. I manage the account week to week, bringing together creative content, consistency and a clear understanding of the brand.",
      [("65.3k","views in 30 days","total Instagram views"),("33k","reel views in 30 days","combined reel performance"),("+1,000","followers in 6 months","audience growth"),("1.3k","likes in 30 days","across reels, stories and posts")],
      img("r45 m-a","lucas-front.jpg","two of the team outside Luca’s takeaway café") +
      img("r34 m-b","lucas-cookies.jpg","iced cookies on a wooden board") +
      img("r34 m-c","lucas-drink.jpg","an iced pink drink held up in the sun") +
      img("r34 m-d","lucas-shop-autumn.jpg","the shopfront dressed with autumn flowers") +
      img("r34 m-e","lucas-baristas2.jpg","the team behind the counter") +
      img("r32 m-f","lucas-shop-wide.jpg","customers at the tables outside Luca’s") +
      img("r34 m-g","lucas-drinks.jpg","two iced drinks held up against a green t‑shirt") +
      img("r34 m-h","lucas-team.jpg","the team at the counter with balloons")
)}
{case("bellagio","04","social media management","bellagio_pizzeria",
      "bellagio <em>pizzeria</em>",
      "Ongoing social media management for a family‑run Italian restaurant. From planning content and capturing the atmosphere of the restaurant to editing reels, creating stories and posts, I manage the account week to week, bringing the food, people and personality behind Bellagio to life.",
      [("18k+","content views in 90 days","reels, stories and posts"),("+181","net followers in 90 days","audience growth"),("1,083","content interactions","likes, comments and shares"),("62.1%","views from non‑followers","reaching new people")],
      BELLAGIO_REEL +
      img("r34 m-b","bellagio-dining.jpg","two guests with pizza and pasta at the table") +
      img("r34 m-c","bellagio-pasta.jpg","pasta and wine on the table") +
      img("r34 m-d","bellagio-chef.jpg","the chef plating up in the kitchen") +
      img("r34 m-e","bellagio-oven.jpg","a pizza going into the wood‑fired oven")
)}
      <article id="lifestyle" class="case">
        <div class="case-head" data-reveal>
          <div>
            <p class="label num" data-num="05">personal</p>
            <h2 class="h-l">lifestyle <em>photography</em></h2>
          </div>
          <div>
            <p class="muted">A little collection of places, experiences and everyday moments. Coastal scenes, good food, beautiful interiors and the little details that make a moment worth capturing.</p>
          </div>
        </div>
        <div class="strip" data-stagger>
          {img("r34","life-pool.jpg","swimmers in the sea pool at Bondi")}
          {img("r34","life-surf.jpg","a wave breaking on the rocks")}
          {img("r34","life-table.jpg","breakfast plates on a checkered floor","center 40%")}
          {img("r34","life-cafe.jpg","a sunlit café table by the window")}
          {img("r34","life-street.jpg","a narrow sunlit street")}
          {img("r34","life-beach.jpg","a busy beach under a blue sky")}
          {img("r34","life-toast.jpg","avocado toast on a board")}
          {img("r34","life-gallery.jpg","a wall of framed prints in a gallery")}
          {img("r34","life-wave.jpg","a swimmer in turquoise water")}
          {img("r34","life-lounge.jpg","a warm‑lit lounge with bookshelves")}
        </div>
      </article>
    </div>
  </section>

  {ig_section("06", [("welcome","welcome to marketia — view on instagram"),("together","it’s all coming together — view on instagram"),("coming","something is coming — view on instagram")], cream=True)}

  {cta("want to work with <em>marketia</em>?","Submit an enquiry form today. I can’t wait to hear from you!")}
'''

# ------------------------------------------------------------------ CONTACT
contact = f'''
  <section class="page-intro contact-intro">
    <div class="wrap">
      <p class="label">contact</p>
      <div class="split">
        <h1 class="h-xl">let’s work <em>together</em>.</h1>
        <p class="lede">Tell me everything, the big details and the small. I can’t wait to bring your vision to life!</p>
      </div>
    </div>
  </section>

  <section class="section tight contact-section">
    <div class="wrap contact-grid">
      <aside class="contact-side" data-reveal>
        <ul class="deets">
          <li><span class="label">email</span><a href="mailto:hello@marketia.uk">hello@marketia.uk</a></li>
          <li><span class="label">phone</span><a href="tel:+447538963391">07538 963391</a></li>
          <li><span class="label">instagram</span><a href="{IG}" target="_blank" rel="noopener">@markettiaa</a></li>
          <li><span class="label">based</span><span class="v">Dorset · across the UK</span></li>
        </ul>
        <p class="label">what happens next</p>
        <ul class="next-steps">
          <li><b>Let’s have a chat.</b> I’ll be in touch to arrange a quick discovery call so we can talk through your business, ideas, goals and what you’re looking for.</li>
          <li><b>A plan, made for you.</b> Following our chat, I’ll put together a tailored proposal outlining my recommendations, creative concepts, moodboard, suggested deliverables, pricing and next steps.</li>
          <li><b>Time to get started.</b> Once everything is agreed, we’ll go through onboarding, get to know your brand in more detail, organise content plans and calendars, and get everything in place for our first shoot or project.</li>
        </ul>
      </aside>

      <form class="form" id="enquiry" novalidate data-reveal action="https://formsubmit.co/hello@marketia.uk" method="POST">
        <input type="hidden" name="_subject" value="new enquiry from marketia.uk">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="_honey" class="visually-hidden" tabindex="-1" autocomplete="off" aria-hidden="true">
        <fieldset>
          <legend>about you</legend>
          <div class="row">
            <div class="field"><label for="f-name">your name</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
            <div class="field"><label for="f-email">your email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
          </div>
          <div class="row">
            <div class="field"><label for="f-business">business / brand name</label><input id="f-business" name="business" type="text" autocomplete="organization"></div>
            <div class="field"><label for="f-ig">instagram handle <small>optional</small></label><input id="f-ig" name="instagram" type="text" placeholder="@"></div>
          </div>
        </fieldset>

        <fieldset>
          <legend>about the business</legend>
          <div class="field"><label for="f-achieve">what would you like to achieve?</label><textarea id="f-achieve" name="goals" rows="4" required></textarea></div>
          <div class="field"><label for="f-else">anything else I should know? <small>optional</small></label><textarea id="f-else" name="anything else" rows="3"></textarea></div>
        </fieldset>

        <fieldset>
          <legend>what you’re looking for</legend>
          <div class="field">
            <label>what do you need support with? <small>tick any</small></label>
            <div class="checks">
              <label class="check"><input type="checkbox" name="support" value="social media management"> social media management</label>
              <label class="check"><input type="checkbox" name="support" value="content shoot (half / full day)"> a content shoot</label>
              <label class="check"><input type="checkbox" name="support" value="campaign, launch or event"> campaign, launch or event</label>
              <label class="check"><input type="checkbox" name="support" value="creator content"> creator content</label>
              <label class="check"><input type="checkbox" name="support" value="reels / video"> reels &amp; video</label>
              <label class="check"><input type="checkbox" name="support" value="not sure yet"> not sure yet</label>
            </div>
          </div>
          <div class="row">
            <div class="field">
              <label for="f-start">when would you like to start?</label>
              <select id="f-start" name="start">
                <option value="">choose one</option>
                <option>as soon as possible</option>
                <option>in the next month</option>
                <option>in the next few months</option>
                <option>just exploring for now</option>
              </select>
            </div>
            <div class="field">
              <label for="f-heard">how did you hear about marketia?</label>
              <select id="f-heard" name="heard about marketia via">
                <option value="">choose one</option>
                <option>Instagram</option>
                <option>word of mouth</option>
                <option>saw your work with another business</option>
                <option>Google</option>
                <option>other</option>
              </select>
            </div>
          </div>
          <div class="field"><label for="f-projects">any upcoming projects, launches or events? <small>optional</small></label><textarea id="f-projects" name="upcoming projects" rows="3"></textarea></div>
        </fieldset>

        <div class="form-foot">
          <button class="btn solid" type="submit">send enquiry</button>
          <p class="form-note" id="form-note" aria-live="polite">Your enquiry comes straight to me. I’ll reply by email.</p>
        </div>
      </form>
    </div>
  </section>
'''

pages = {
  "index.html":   ("marketia — social media management & content creation, Dorset",
                   "marketia is Tia’s creative brand: iPhone‑led social media management, content creation, photography and videography for businesses, brands and creators. Based in Dorset, available across the UK.", home),
  "about.html":   ("about — marketia", "Meet Tia, the founder of marketia, and the story behind the brand.", about),
  "services.html":("services — marketia", "Social media management and content creation days: what’s included, how pricing works and how to enquire.", services),
  "work.html":    ("work — marketia", "Reels, case studies and photography for Rockwater Village, Luca’s takeaway café and Bellagio Pizzeria, plus lifestyle work.", work),
  "contact.html": ("contact — marketia", "Start an enquiry with marketia about social media management or a content shoot.", contact),
}
for fn,(t,d,b) in pages.items():
    open(os.path.join(OUT,fn),"w").write(shell(fn,t,d,b))
    print("wrote",fn)
