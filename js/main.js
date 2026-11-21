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

  // arriving with #something: land on that heading/form once layout has settled (images shift things)
  if (window.location.hash && window.location.hash.length > 1) {
    var target = document.getElementById(window.location.hash.slice(1));
    var goTo = function () { if (target) target.scrollIntoView({ behavior: 'auto', block: 'start' }); };
    setTimeout(goTo, 150);
    window.addEventListener('load', function () { setTimeout(goTo, 250); });
  }

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

  // enquiry form: sends from the page (formsubmit.co → hello@marketia.uk); offers email if that fails
  var form = $('#enquiry');
  if (form) {
    // pre-tick the service when arriving from a service button (?service=...)
    var svc = new URLSearchParams(window.location.search).get('service');
    var pre = { management: 'social media management', content: 'content shoot (half / full day)', creator: 'creator content' }[svc];
    if (pre) {
      var box = form.querySelector('input[name="support"][value="' + pre + '"]');
      if (box) box.checked = true;
    }
    var note = $('#form-note');
    var v = function (id) { return (document.getElementById(id).value || '').trim(); };
    var clean = function (t) { return t.replace(/[<>&"]/g, ''); };

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

    // sent: thank them by name and show "what happens next" right there
    var showSuccess = function () {
      form.classList.add('sent');
      note.textContent = 'Thank you! Your enquiry is on its way and I’ll be in touch by email soon.';
      note.classList.add('ok');
      var steps = $('#next-steps');
      var panel = document.createElement('div');
      panel.className = 'form-success';
      var first = clean(v('f-name').split(' ')[0]);
      panel.innerHTML = '<h3 class="h-m">thank you' + (first ? ', ' + first : '') + '.</h3>' +
        '<p class="muted">Your enquiry has been sent. Here’s what happens next:</p>' +
        (steps ? steps.innerHTML.replace('<p class="label">what happens next</p>', '') : '') +
        '<a class="textlink" href="work.html">have a look at the work while you wait</a>';
      form.appendChild(panel);
      if (steps) steps.style.display = 'none';
      panel.scrollIntoView({ behavior: 'smooth', block: 'center' });
    };

    // not sent: say so and offer the email route as a button (never jump away on them)
    var offerEmail = function (why) {
      form.querySelector('button[type="submit"]').disabled = false;
      note.textContent = why;
      note.classList.add('err');
      if (!$('#alt-email')) {
        var a = document.createElement('button');
        a.type = 'button'; a.id = 'alt-email'; a.className = 'textlink alt';
        a.textContent = 'open my email app with this filled in';
        a.addEventListener('click', mailtoFallback);
        note.parentNode.appendChild(a);
      }
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
          if (res.ok && String(res.j.success) === 'true') { showSuccess(); return; }
          var msg = String((res.j && res.j.message) || '');
          if (/activat/i.test(msg)) {
            offerEmail('The form is still being connected on my side, sorry! Please email hello@marketia.uk, or use the button below.');
          } else {
            throw new Error(msg || 'send failed');
          }
        })
        .catch(function () {
          offerEmail('That didn’t send. Please email hello@marketia.uk, or use the button below so nothing is lost.');
        });
    });
  }
})();
