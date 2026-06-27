// Highlight active sidebar nav link by scroll position.
(function () {
  const links = document.querySelectorAll('.side-nav a[href^="#"]');
  if (!links.length) return;
  const sections = Array.from(links)
    .map(a => document.querySelector(a.getAttribute('href')))
    .filter(Boolean);
  function onScroll() {
    let active = sections[0];
    for (const s of sections) {
      if (s.getBoundingClientRect().top - 100 <= 0) active = s;
    }
    links.forEach(l => l.classList.toggle('active', l.getAttribute('href') === '#' + active.id));
  }
  document.addEventListener('scroll', onScroll, { passive: true });
})();
