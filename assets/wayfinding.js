/* Wayfinding: small, optional behaviour. Every page reads and navigates completely without it:
   back-to-top and every link are plain HTML. */
(function () {
  var now = new Date();
  if (location.hash === '#grid') document.documentElement.classList.add('show-grid');

  /* The timeline: stations done, here, next. */
  var stops = document.querySelectorAll('#timeline li[data-d]'), here = -1;
  stops.forEach(function (li, i) { if (new Date(li.dataset.d + 'T00:00:00') <= now) here = i; });
  stops.forEach(function (li, i) {
    li.dataset.s = i < here ? 'done' : i === here ? 'now' : i === here + 1 ? 'next' : 'later';
    if (i === here) li.setAttribute('aria-current', 'step');
  });

  figures();

  /* The region chart: show one kind of line at a time. */
  document.querySelectorAll('.flow-show:not(.journey-here)').forEach(function (bar) {
    var wrap = bar.nextElementSibling, chips = bar.querySelectorAll('.chip');
    bar.hidden = false;
    var pick = function (k) {
      wrap.dataset.show = k;
      chips.forEach(function (c) { c.setAttribute('aria-pressed', c.dataset.show === k ? 'true' : 'false'); });
    };
    chips.forEach(function (c) { c.addEventListener('click', function () { pick(c.dataset.show); }); });
    pick('all');
  });

  /* Journey map: Where are you? A red ring on your step; your step and the next stay strong. */
  document.querySelectorAll('.journey-here').forEach(function (bar) {
    var wrap = bar.nextElementSibling, say = wrap.nextElementSibling, chips = bar.querySelectorAll('.chip');
    bar.hidden = false;
    var pick = function (k) {
      wrap.dataset.here = k;
      chips.forEach(function (c) { c.setAttribute('aria-pressed', c.dataset.here === k ? 'true' : 'false'); });
      var c = bar.querySelector('.chip[data-here="' + k + '"]');
      say.hidden = k === 'all';
      say.textContent = k === 'all' ? '' : c.dataset.say + ' ' + c.dataset.next;
    };
    chips.forEach(function (c) { c.addEventListener('click', function () { pick(c.dataset.here); }); });
    pick('all');
  });

  /* Blog carousel: reveal Previous and Next, scroll a card at a time. */
  document.querySelectorAll('.carousel').forEach(function (c) {
    var list = c.querySelector('.cards'), nav = c.querySelector('.carousel-nav');
    var prev = c.querySelector('.cprev'), next = c.querySelector('.cnext');
    if (!list || !nav) return;
    nav.hidden = false;
    var step = function () { var li = list.querySelector('li'); return li ? li.getBoundingClientRect().width + 24 : list.clientWidth; };
    var sync = function () {
      var fits = list.scrollWidth <= list.clientWidth + 4;
      prev.hidden = next.hidden = fits;
      prev.disabled = list.scrollLeft < 4;
      next.disabled = list.scrollLeft + list.clientWidth > list.scrollWidth - 4;
    };
    var smooth = matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth';
    prev.addEventListener('click', function () { list.scrollBy({ left: -step(), behavior: smooth }); });
    next.addEventListener('click', function () { list.scrollBy({ left: step(), behavior: smooth }); });
    list.addEventListener('scroll', sync, { passive: true });
    window.addEventListener('resize', sync);
    sync();
  });

  /* You are here: the bar names the section you're in and opens every stop. */
  var bar = document.querySelector('.herebar');
  var secs = Array.prototype.slice.call(document.querySelectorAll('main .sec'));
  var cover = document.querySelector('.cover');
  if (!bar || !secs.length || !cover || !('IntersectionObserver' in window)) return;

  var toggle = bar.querySelector('.here-toggle'), panel = document.getElementById('stops');
  var name = document.getElementById('here-name'), dots = document.getElementById('here-dots');
  var list = document.getElementById('stops-list');
  var titles = secs.map(function (s) { var h = s.querySelector('h2'); return h ? h.textContent : ''; });

  secs.forEach(function (s, i) {
    var d = document.createElement('li'); d.setAttribute('aria-hidden', 'true'); dots.appendChild(d);
    var li = document.createElement('li');
    li.innerHTML = '<span class="st" aria-hidden="true"></span><a class="t" href="#' + s.getAttribute('aria-labelledby') + '"></a><span class="here"><span class="t t-small">You are here</span></span>';
    li.querySelector('a').textContent = titles[i];
    list.appendChild(li);
  });
  var dotEls = dots.querySelectorAll('li'), listEls = list.querySelectorAll('li');

  var current = -1;
  function set(idx) {
    if (idx < 0 || idx === current) return; current = idx;
    name.textContent = titles[idx];
    dotEls.forEach(function (m, i) { m.className = i < idx ? 'past' : i === idx ? 'on' : ''; });
    listEls.forEach(function (li, i) {
      li.dataset.s = i < idx ? 'done' : i === idx ? 'now' : 'later';
      var a = li.querySelector('a');
      if (i === idx) a.setAttribute('aria-current', 'location'); else a.removeAttribute('aria-current');
    });
  }
  function open(v) {
    toggle.setAttribute('aria-expanded', v ? 'true' : 'false');
    panel.hidden = !v;
  }
  toggle.addEventListener('click', function () { open(panel.hidden); });
  list.addEventListener('click', function (e) { if (e.target.closest('a')) open(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !panel.hidden) { open(false); toggle.focus(); } });
  document.addEventListener('click', function (e) { if (!panel.hidden && !bar.contains(e.target)) open(false); });

  new IntersectionObserver(function (es) {
    es.forEach(function (e) { bar.classList.toggle('show', !e.isIntersecting); if (e.isIntersecting) open(false); });
  }, { threshold: 0 }).observe(cover);
  var vis = new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) set(secs.indexOf(e.target)); });
  }, { rootMargin: '-30% 0px -65% 0px' });
  secs.forEach(function (s) { vis.observe(s); });
  set(0);

  /* Diagrams play their change once, on first view. */
  function figures() {
    if (!('IntersectionObserver' in window) || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    var figs = document.querySelectorAll('figure.anim');
    figs.forEach(function (f) { f.classList.add('pre'); });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var f = e.target; io.unobserve(f);
        requestAnimationFrame(function () { f.classList.add('in'); f.classList.remove('pre'); });
      });
    }, { threshold: 0.4 });
    figs.forEach(function (f) { io.observe(f); });
  }
})();
