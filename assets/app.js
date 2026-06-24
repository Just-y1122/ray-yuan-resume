(() => {
  const body = document.body;
  const nav = document.querySelector('.main-nav');
  const navToggle = document.querySelector('.nav-toggle');
  const langBtn = document.querySelector('.lang-toggle');
  const wipe = document.querySelector('.page-wipe');
  const toast = document.querySelector('.toast');
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const currentPage = body.dataset.page || 'home';
  document.querySelectorAll('.main-nav a').forEach(link => {
    if (link.dataset.page === currentPage) link.setAttribute('aria-current', 'page');
  });

  const setLanguage = (lang) => {
    document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';
    localStorage.setItem('ray-lang', lang);
    document.querySelectorAll('[data-zh][data-en]').forEach(el => {
      const value = el.dataset[lang];
      if (value !== undefined) el.textContent = value;
    });
    document.querySelectorAll('[data-html-zh][data-html-en]').forEach(el => {
      const value = el.dataset[`html${lang === 'zh' ? 'Zh' : 'En'}`];
      if (value !== undefined) el.innerHTML = value;
    });
    document.querySelectorAll('[data-aria-zh][data-aria-en]').forEach(el => {
      el.setAttribute('aria-label', lang === 'zh' ? el.dataset.ariaZh : el.dataset.ariaEn);
    });
    if (langBtn) langBtn.textContent = lang === 'zh' ? 'EN' : '中文';
    const title = lang === 'zh' ? body.dataset.titleZh : body.dataset.titleEn;
    if (title) document.title = title;
    body.dataset.lang = lang;
  };

  setLanguage(localStorage.getItem('ray-lang') || 'zh');
  langBtn?.addEventListener('click', () => setLanguage(body.dataset.lang === 'zh' ? 'en' : 'zh'));

  navToggle?.addEventListener('click', () => {
    const open = navToggle.getAttribute('aria-expanded') === 'true';
    navToggle.setAttribute('aria-expanded', String(!open));
    nav?.classList.toggle('is-open', !open);
  });
  document.addEventListener('click', (e) => {
    if (nav && navToggle && !nav.contains(e.target) && !navToggle.contains(e.target)) {
      nav.classList.remove('is-open'); navToggle.setAttribute('aria-expanded', 'false');
    }
  });

  document.querySelectorAll('a[href$=".html"], a[href^="mailto:"], a[href^="tel:"]').forEach(link => {
    if (link.href.startsWith('mailto:') || link.href.startsWith('tel:')) return;
    link.addEventListener('click', e => {
      if (e.ctrlKey || e.metaKey || e.shiftKey || e.altKey || link.target === '_blank') return;
      e.preventDefault();
      wipe?.classList.add('is-leaving');
      setTimeout(() => { window.location.href = link.href; }, reduced ? 0 : 360);
    });
  });

  const revealObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: .13 });
  document.querySelectorAll('.reveal, .skill-card').forEach(el => revealObserver.observe(el));

  const progress = document.getElementById('top-progress');
  const backTop = document.querySelector('.back-top');
  const onScroll = () => {
    const max = document.documentElement.scrollHeight - innerHeight;
    const ratio = max > 0 ? scrollY / max : 0;
    if (progress) progress.style.width = `${ratio * 100}%`;
    backTop?.classList.toggle('show', scrollY > 420);
  };
  addEventListener('scroll', onScroll, { passive:true }); onScroll();
  backTop?.addEventListener('click', () => scrollTo({ top:0, behavior: reduced ? 'auto' : 'smooth' }));

  // Gentle 3D tilt for cards on pointer devices.
  if (matchMedia('(hover:hover)').matches && !reduced) {
    document.querySelectorAll('[data-tilt]').forEach(card => {
      card.addEventListener('pointermove', e => {
        const r = card.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width - .5;
        const y = (e.clientY - r.top) / r.height - .5;
        card.style.transform = `perspective(800px) rotateX(${y * -5}deg) rotateY(${x * 6}deg) translateY(-4px)`;
      });
      card.addEventListener('pointerleave', () => card.style.transform = '');
    });

    let last = 0;
    addEventListener('pointermove', e => {
      const now = performance.now();
      if (now - last < 80) return;
      last = now;
      const heart = document.createElement('span');
      heart.className = 'trail-heart'; heart.textContent = Math.random() > .5 ? '♥' : '✦';
      heart.style.left = `${e.clientX + 6}px`; heart.style.top = `${e.clientY + 5}px`;
      heart.style.fontSize = `${10 + Math.random() * 7}px`;
      document.body.appendChild(heart);
      setTimeout(() => heart.remove(), 950);
    });
  }

  // Floating background decorations.
  const layer = document.querySelector('.decor-layer');
  if (layer && !reduced) {
    for (let i = 0; i < 18; i++) {
      const d = document.createElement('span');
      d.className = `decor ${i % 3 ? 'star' : 'heart'}`;
      if (i % 3) d.textContent = i % 2 ? '✦' : '♡';
      d.style.left = `${Math.random() * 100}%`;
      d.style.top = `${Math.random() * 100}%`;
      d.style.setProperty('--duration', `${4 + Math.random() * 6}s`);
      d.style.animationDelay = `${-Math.random() * 5}s`;
      layer.appendChild(d);
    }
  }

  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('is-active'));
      btn.classList.add('is-active');
      const filter = btn.dataset.filter;
      document.querySelectorAll('.skill-card').forEach(card => {
        card.hidden = filter !== 'all' && card.dataset.category !== filter;
        if (!card.hidden) requestAnimationFrame(() => card.classList.add('is-visible'));
      });
    });
  });

  const showToast = (zh, en) => {
    if (!toast) return;
    toast.textContent = body.dataset.lang === 'zh' ? zh : en;
    toast.classList.add('show');
    clearTimeout(showToast.timer);
    showToast.timer = setTimeout(() => toast.classList.remove('show'), 1800);
  };
  document.querySelector('[data-copy-email]')?.addEventListener('click', async () => {
    const email = '1521718888@qq.com';
    try { await navigator.clipboard.writeText(email); showToast('邮箱已复制 ♥', 'Email copied ♥'); }
    catch { showToast('复制失败，请手动复制', 'Copy failed, please copy manually'); }
  });
})();
