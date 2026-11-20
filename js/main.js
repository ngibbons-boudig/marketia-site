// marketia — small enhancements, no dependencies
(function () {
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  // footer year
  var y = $('#year');
  if (y) y.textContent = new Date().getFullYear();

  // mobile nav
  var toggle = $('.nav-toggle');
  var nav = $('#site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // header hairline once scrolled
  var header = $('.site-header');
  if (header) {
    var onScroll = function () { header.classList.toggle('scrolled', window.scrollY > 10); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // type previews for tia: ?fonts=cormorant | bodoni | playfair (remembered until ?fonts=off)
  (function () {
    var qs = new URLSearchParams(window.location.search).get('fonts');
    var saved = null;
    try { saved = localStorage.getItem('fonts'); } catch (e) {}
    if (qs === 'off') { try { localStorage.removeItem('fonts'); } catch (e) {} document.documentElement.removeAttribute('data-fonts'); return; }
    var current = qs || saved;
    if (!current) return;
    try { localStorage.setItem('fonts', current); } catch (e) {}
    document.documentElement.setAttribute('data-fonts', current);
    var extra = {
      bodoni: 'https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,500;1,6..96,400&display=swap',
      playfair: 'https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Manrope:wght@400;500&display=swap'
    };
    Object.keys(extra).forEach(function (k) {
      var l = document.createElement('link'); l.rel = 'stylesheet'; l.href = extra[k]; document.head.appendChild(l);
    });
    var bar = document.createElement('div');
    bar.className = 'type-switch';
    bar.setAttribute('aria-label', 'font preview');
    [['cormorant', 'cormorant + dm sans'], ['bodoni', 'bodoni + dm sans'], ['playfair', 'playfair + manrope']].forEach(function (o) {
      var b = document.createElement('button'); b.type = 'button'; b.textContent = o[1];
      b.setAttribute('aria-pressed', current === o[0] ? 'true' : 'false');
      b.addEventListener('click', function () {
        current = o[0];
        try { localStorage.setItem('fonts', current); } catch (e) {}
        document.documentElement.setAttribute('data-fonts', current);
        $$('button', bar).forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      });
      bar.appendChild(b);
    });
    var x = document.createElement('button'); x.type = 'button'; x.className = 'x'; x.textContent = 'hide';
    x.addEventListener('click', function () { try { localStorage.removeItem('fonts'); } catch (e) {} document.documentElement.removeAttribute('data-fonts'); bar.remove(); });
    bar.appendChild(x);
    document.body.appendChild(bar);
  })();

  // scroll reveals
  var targets = $$('[data-reveal], [data-stagger]');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        el.classList.add('in');
        setTimeout(function () { el.classList.add('done'); }, 1600);
        io.unobserve(el);
      });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.08 });
    targets.forEach(function (el) { io.observe(el); });
  } else {
    targets.forEach(function (el) { el.classList.add('in', 'done'); });
  }

  // reels: play while in view, muted; tap the sound button to unmute one at a time
  var reels = $$('.reel video');
  if (reels.length && 'IntersectionObserver' in window) {
    var vo = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var v = en.target;
        if (en.isIntersecting) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
        else { v.pause(); }
      });
    }, { threshold: 0.35 });
    reels.forEach(function (v) { vo.observe(v); });
  }
  // a reel slot whose file hasn't arrived yet keeps its "coming soon" note
  $$('.reel-slot video').forEach(function (v) {
    var slot = v.closest('.reel-slot');
    v.addEventListener('loadedmetadata', function () { slot.classList.add('has-video'); });
    v.addEventListener('error', function () { slot.classList.remove('has-video'); }, true);
  });
  $$('.reel .sound').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      var v = btn.parentNode.querySelector('video');
      var turnOn = v.muted;
      reels.forEach(function (o) { o.muted = true; });
      $$('.reel .sound').forEach(function (b) { b.setAttribute('aria-pressed', 'false'); b.textContent = 'sound'; });
      v.muted = !turnOn;
      btn.setAttribute('aria-pressed', turnOn ? 'true' : 'false');
      btn.textContent = turnOn ? 'mute' : 'sound';
      if (turnOn) { var p2 = v.play(); if (p2 && p2.catch) p2.catch(function () {}); }
    });
  });

  // enquiry form: sends from the page (formsubmit.co → hello@marketia.uk); falls back to email if that fails
  var form = $('#enquiry');
  if (form) {
    // pre-tick the service when arriving from a service button (?service=...)
    var svc = new URLSearchParams(window.location.search).get('service');
    var pre = { management: 'social media management', content: 'content shoot (half / full day)', creator: 'creator content' }[svc];
    if (pre) {
      var box = form.querySelector('input[name="support"][value="' + pre + '"]');
      if (box) box.checked = true;
    }
    // arriving at #enquiry: make sure the form, not the page top, is in view once layout settles
    if (window.location.hash === '#enquiry') {
      setTimeout(function () { form.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 150);
    }

    var note = $('#form-note');
    var v = function (id) { return (document.getElementById(id).value || '').trim(); };
    var mailtoFallback = function () {
      var needs = $$('input[name="support"]:checked', form).map(function (c) { return c.value; }).join(', ');
      var subject = 'enquiry from ' + v('f-name') + (v('f-business') ? ' — ' + v('f-business') : '');
      var lines = [
        'name: ' + v('f-name'), 'email: ' + v('f-email'), 'business: ' + (v('f-business') || '-'), 'instagram: ' + (v('f-ig') || '-'), '',
        'what they would like to achieve:', v('f-achieve'), '', 'anything else:', v('f-else') || '-', '',
        'support needed: ' + (needs || '-'), 'start: ' + (v('f-start') || '-'), 'heard about marketia via: ' + (v('f-heard') || '-'), '',
        'upcoming projects / events:', v('f-projects') || '-'
      ];
      window.location.href = 'mailto:hello@marketia.uk?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n'));
    };

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = true;
      ['f-name', 'f-email', 'f-achieve'].forEach(function (id) {
        var el = document.getElementById(id);
        var valid = el.value.trim() !== '' && (el.type !== 'email' || el.checkValidity());
        el.setAttribute('aria-invalid', valid ? 'false' : 'true');
        if (!valid) ok = false;
      });
      note.className = 'form-note';
      if (!ok) {
        note.textContent = 'Please add your name, a valid email and a few words about what you’d like to achieve.';
        note.classList.add('err');
        return;
      }
      var btn = form.querySelector('button[type="submit"]');
      btn.disabled = true; note.textContent = 'Sending…';
      var data = new FormData(form);
      data.set('_replyto', v('f-email'));
      var endpoint = form.getAttribute('action').replace('formsubmit.co/', 'formsubmit.co/ajax/');
      fetch(endpoint, { method: 'POST', headers: { 'Accept': 'application/json' }, body: data })
        .then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (!res.ok || String(res.j.success) !== 'true') throw new Error(res.j.message || 'send failed');
          form.classList.add('sent');
          note.textContent = 'Thank you! Your enquiry is on its way. I’ll be in touch by email soon.';
          note.classList.add('ok');
        })
        .catch(function () {
          btn.disabled = false;
          note.textContent = 'That didn’t send. Opening your email app instead so nothing is lost…';
          note.classList.add('err');
          setTimeout(mailtoFallback, 800);
        });
    });
  }
})();
