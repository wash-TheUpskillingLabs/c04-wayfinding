/* Wayfinding: small, optional behaviour. Every page reads complete without it. */
(function () {
  var now = new Date();
  if (location.hash === '#grid') document.documentElement.classList.add('show-grid');

  /* The metro line: mark stations done, here, next. */
  var stops = document.querySelectorAll('#timeline li[data-d]'), here = -1;
  stops.forEach(function (li, i) { if (new Date(li.dataset.d + 'T00:00:00') <= now) here = i; });
  stops.forEach(function (li, i) {
    li.dataset.s = i < here ? 'done' : i === here ? 'now' : i === here + 1 ? 'next' : 'later';
    if (i === here) li.setAttribute('aria-current', 'step');
  });

  /* You are here bar (phones): names the section you're reading. */
  var bar = document.querySelector('.herebar');
  var secs = Array.prototype.slice.call(document.querySelectorAll('main .sec'));
  var cover = document.querySelector('.cover');
  if (bar && secs.length && 'IntersectionObserver' in window) {
    var name = document.getElementById('here-name'), dots = document.getElementById('here-dots');
    secs.forEach(function () { dots.appendChild(document.createElement('i')); });
    var marks = dots.querySelectorAll('i');
    var set = function (idx) {
      var h = secs[idx].querySelector('h2');
      name.textContent = h ? h.textContent : '';
      marks.forEach(function (m, i) { m.className = i < idx ? 'past' : i === idx ? 'on' : ''; });
    };
    new IntersectionObserver(function (es) {
      es.forEach(function (e) { bar.classList.toggle('show', !e.isIntersecting); });
    }, { threshold: 0 }).observe(cover);
    var vis = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) set(secs.indexOf(e.target)); });
    }, { rootMargin: '-45% 0px -50% 0px' });
    secs.forEach(function (s) { vis.observe(s); });
    set(0);
  }

  /* Diagrams play their change once, on first view. */
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
})();
