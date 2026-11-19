// marketia — small enhancements, no dependencies
(function () {
  // footer year
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  // mobile nav
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // scroll reveals
  var revealEls = document.querySelectorAll('[data-reveal]');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        el.classList.add('in');
        setTimeout(function () { el.classList.add('done'); }, 1400);
        io.unobserve(el);
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.12 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('in', 'done'); });
  }

  // header shadow once the page has scrolled
  var header = document.querySelector('.site-header');
  var onScroll = function () {
    header.classList.toggle('scrolled', window.scrollY > 24);
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // contact form → opens the visitor's email client with everything filled in.
  // Swap this for a form service (Formspree / Netlify Forms) once hosting is chosen.
  var form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = true;
      ['f-name', 'f-email', 'f-msg'].forEach(function (id) {
        var el = document.getElementById(id);
        var valid = el.value.trim() !== '' && (el.type !== 'email' || el.checkValidity());
        el.setAttribute('aria-invalid', valid ? 'false' : 'true');
        if (!valid) ok = false;
      });
      var note = document.getElementById('form-note');
      if (!ok) {
        note.textContent = 'please add your name, a valid email and a short message.';
        return;
      }
      var v = function (id) { return document.getElementById(id).value.trim(); };
      var subject = 'enquiry from ' + v('f-name') + (v('f-brand') ? ' — ' + v('f-brand') : '');
      var body =
        'name: ' + v('f-name') + '\n' +
        'email: ' + v('f-email') + '\n' +
        'brand: ' + (v('f-brand') || '-') + '\n' +
        'interested in: ' + v('f-type') + '\n\n' +
        v('f-msg');
      window.location.href = 'mailto:hello@marketia.uk?subject=' +
        encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      note.textContent = 'opening your email app… if nothing happens, email hello@marketia.uk directly.';
    });
  }
})();
