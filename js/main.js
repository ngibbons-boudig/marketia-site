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

  // enquiry form
  var form = $('#enquiry');
  if (form) {
    // pre-tick the service when arriving from a service button (?service=...)
    var svc = new URLSearchParams(window.location.search).get('service');
    var pre = { management: 'social media management', content: 'content shoot (half / full day)', creator: 'creator content' }[svc];
    if (pre) {
      var box = form.querySelector('input[name="need"][value="' + pre + '"]');
      if (box) box.checked = true;
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var note = $('#form-note');
      var ok = true;
      ['f-name', 'f-email', 'f-help'].forEach(function (id) {
        var el = document.getElementById(id);
        var valid = el.value.trim() !== '' && (el.type !== 'email' || el.checkValidity());
        el.setAttribute('aria-invalid', valid ? 'false' : 'true');
        if (!valid) ok = false;
      });
      if (!ok) {
        note.textContent = 'please add your name, a valid email and a few words about what you need.';
        return;
      }
      var v = function (id) { return (document.getElementById(id).value || '').trim(); };
      var needs = $$('input[name="need"]:checked', form).map(function (c) { return c.value; }).join(', ');
      var subject = 'enquiry from ' + v('f-name') + (v('f-business') ? ' — ' + v('f-business') : '');
      var lines = [
        'name: ' + v('f-name'),
        'email: ' + v('f-email'),
        'business: ' + (v('f-business') || '-'),
        'instagram: ' + (v('f-ig') || '-'),
        '',
        'what the business does:',
        v('f-does') || '-',
        '',
        'what makes it special:',
        v('f-special') || '-',
        '',
        'support needed: ' + (needs || '-'),
        '',
        'more detail:',
        v('f-help'),
        '',
        'start: ' + (v('f-start') || '-'),
        'heard about marketia via: ' + (v('f-heard') || '-'),
        '',
        'upcoming projects / events:',
        v('f-projects') || '-'
      ];
      window.location.href = 'mailto:hello@marketia.uk?subject=' +
        encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n'));
      note.textContent = 'opening your email app… if nothing happens, email hello@marketia.uk directly.';
    });
  }
})();
