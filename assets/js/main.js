/* ============================================================
   رواد الليزر — Ruwwad Laser  |  site interactions
   ============================================================ */
(function () {
  'use strict';

  /* ---- CONFIG: العميل يعدّل هذه القيم | client edits these ---- */
  window.RUWWAD = window.RUWWAD || {
    whatsapp: '966543225519',                 // رقم واتساب بصيغة دولية بدون +
    phoneDisplay: '0543225519',
    email: 'info@rowadlaser.com',
    city: { ar: 'جدة، المملكة العربية السعودية', en: 'Jeddah, Saudi Arabia' }
  };

  /* ---------------- Language ---------------- */
  var STORE_KEY = 'ruwwad-lang';
  function currentLang() {
    return localStorage.getItem(STORE_KEY) || document.documentElement.getAttribute('data-default-lang') || 'ar';
  }
  function applyLang(lang) {
    var html = document.documentElement;
    html.lang = lang;
    html.dir = (lang === 'ar') ? 'rtl' : 'ltr';

    document.querySelectorAll('[data-ar]').forEach(function (el) {
      var v = el.getAttribute('data-' + lang);
      if (v !== null) el.textContent = v;
    });
    document.querySelectorAll('[data-ar-html]').forEach(function (el) {
      var v = el.getAttribute('data-' + lang + '-html');
      if (v !== null) el.innerHTML = v;
    });
    document.querySelectorAll('[data-ar-ph]').forEach(function (el) {
      var v = el.getAttribute('data-' + lang + '-ph');
      if (v !== null) el.setAttribute('placeholder', v);
    });
    document.querySelectorAll('[data-ar-aria]').forEach(function (el) {
      var v = el.getAttribute('data-' + lang + '-aria');
      if (v !== null) el.setAttribute('aria-label', v);
    });
    // toggle button label shows the OTHER language
    document.querySelectorAll('.lang-label').forEach(function (el) {
      el.textContent = (lang === 'ar') ? 'EN' : 'ع';
    });
    localStorage.setItem(STORE_KEY, lang);
  }
  window.__setLang = function (lang) { applyLang(lang); };

  /* apply saved language ASAP */
  applyLang(currentLang());

  document.addEventListener('DOMContentLoaded', function () {
    /* language toggles */
    document.querySelectorAll('[data-lang-toggle]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        applyLang(currentLang() === 'ar' ? 'en' : 'ar');
      });
    });

    /* header shadow on scroll */
    var header = document.querySelector('.site-header');
    if (header) {
      var onScroll = function () { header.classList.toggle('scrolled', window.scrollY > 8); };
      onScroll(); window.addEventListener('scroll', onScroll, { passive: true });
    }

    /* mobile menu */
    var menu = document.querySelector('.mobile-menu');
    var openBtn = document.querySelector('.menu-btn');
    var closeBtn = document.querySelector('.mm-close');
    function setMenu(open) {
      if (!menu) return;
      menu.classList.toggle('open', open);
      document.body.style.overflow = open ? 'hidden' : '';
    }
    if (openBtn) openBtn.addEventListener('click', function () { setMenu(true); });
    if (closeBtn) closeBtn.addEventListener('click', function () { setMenu(false); });
    if (menu) menu.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });

    /* reveal on scroll */
    var io = ('IntersectionObserver' in window)
      ? new IntersectionObserver(function (entries) {
          entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
        }, { threshold: 0.12 })
      : null;
    document.querySelectorAll('.reveal').forEach(function (el) {
      if (io) io.observe(el); else el.classList.add('in');
    });

    /* FAQ accordion */
    document.querySelectorAll('.faq-q').forEach(function (q) {
      q.addEventListener('click', function () {
        var item = q.closest('.faq-item');
        var a = item.querySelector('.faq-a');
        var open = item.classList.toggle('open');
        a.style.maxHeight = open ? (a.scrollHeight + 'px') : '0';
      });
    });

    /* wire contact / quote links to WhatsApp + tel + mail */
    var wa = window.RUWWAD.whatsapp;
    document.querySelectorAll('[data-wa]').forEach(function (a) {
      var msg = a.getAttribute('data-wa') || (currentLang() === 'ar'
        ? 'مرحباً رواد الليزر، أرغب في طلب عرض سعر.'
        : 'Hello Ruwwad Laser, I would like to request a quote.');
      a.href = 'https://wa.me/' + wa + '?text=' + encodeURIComponent(msg);
      a.target = '_blank'; a.rel = 'noopener';
    });
    document.querySelectorAll('[data-tel]').forEach(function (a) { a.href = 'tel:+' + wa; });
    document.querySelectorAll('[data-mail]').forEach(function (a) { a.href = 'mailto:' + window.RUWWAD.email; });
    document.querySelectorAll('[data-phone-text]').forEach(function (el) {
      el.textContent = window.RUWWAD.phoneDisplay;
      el.setAttribute('dir', 'ltr');                 // منع انعكاس الرقم في الوضع RTL
      el.style.unicodeBidi = 'isolate';
      el.style.display = 'inline-block';
    });
    document.querySelectorAll('[data-mail-text]').forEach(function (el) { el.textContent = window.RUWWAD.email; });

    /* contact form → compose WhatsApp message (works without a backend) */
    var form = document.querySelector('#quote-form');
    if (form) {
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var lang = currentLang();
        var d = new FormData(form);
        var lines = lang === 'ar'
          ? ['طلب عرض سعر — رواد الليزر', '',
             'الاسم: ' + (d.get('name') || ''),
             'الجوال: ' + (d.get('phone') || ''),
             'الخدمة: ' + (d.get('service') || ''),
             'التفاصيل: ' + (d.get('message') || '')]
          : ['Quote request — Ruwwad Laser', '',
             'Name: ' + (d.get('name') || ''),
             'Phone: ' + (d.get('phone') || ''),
             'Service: ' + (d.get('service') || ''),
             'Details: ' + (d.get('message') || '')];
        var url = 'https://wa.me/' + wa + '?text=' + encodeURIComponent(lines.join('\n'));
        window.open(url, '_blank', 'noopener');
        var ok = form.querySelector('.form-ok');
        if (ok) ok.hidden = false;
        form.reset();
      });
    }

    /* testimonials carousel — swipe + prev/next (RTL-aware, no library) */
    document.querySelectorAll('[data-carousel]').forEach(function (c) {
      var track = c.querySelector('.carousel-track');
      if (!track) return;
      function step(dir) {
        var card = track.querySelector('.quote');
        var styles = getComputedStyle(track);
        var gap = parseInt(styles.columnGap || styles.gap, 10) || 24;
        var amount = (card ? card.getBoundingClientRect().width : 320) + gap;
        var rtl = document.documentElement.dir === 'rtl';
        track.scrollBy({ left: dir * amount * (rtl ? -1 : 1), behavior: 'smooth' });
      }
      var prev = c.querySelector('[data-car-prev]');
      var next = c.querySelector('[data-car-next]');
      if (prev) prev.addEventListener('click', function () { step(-1); });
      if (next) next.addEventListener('click', function () { step(1); });
    });

    /* footer year */
    var yr = String(new Date().getFullYear());
    document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = yr; });
  });
})();
