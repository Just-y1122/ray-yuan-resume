(() => {
  const body = document.body;
  const nav = document.querySelector('.main-nav');
  const navToggle = document.querySelector('.nav-toggle');
  const langBtn = document.querySelector('.lang-toggle');
  const toast = document.querySelector('.toast');
  const currentPage = body.dataset.page || 'home';

  document.querySelectorAll('.main-nav a').forEach(link => {
    if (link.dataset.page === currentPage) link.setAttribute('aria-current', 'page');
  });

  const setLanguage = lang => {
    document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';
    localStorage.setItem('ray-lang-v3', lang);
    document.querySelectorAll('[data-zh][data-en]').forEach(el => {
      const value = el.dataset[lang];
      if (value !== undefined) el.textContent = value;
    });
    document.querySelectorAll('[data-html-zh][data-html-en]').forEach(el => {
      const key = lang === 'zh' ? 'htmlZh' : 'htmlEn';
      if (el.dataset[key] !== undefined) el.innerHTML = el.dataset[key];
    });
    document.querySelectorAll('[data-aria-zh][data-aria-en]').forEach(el => {
      el.setAttribute('aria-label', lang === 'zh' ? el.dataset.ariaZh : el.dataset.ariaEn);
    });
    if (langBtn) langBtn.textContent = lang === 'zh' ? 'EN' : '中文';
    const title = lang === 'zh' ? body.dataset.titleZh : body.dataset.titleEn;
    if (title) document.title = title;
    body.dataset.lang = lang;
  };
  setLanguage(localStorage.getItem('ray-lang-v3') || 'zh');
  langBtn?.addEventListener('click', () => setLanguage(body.dataset.lang === 'zh' ? 'en' : 'zh'));

  navToggle?.addEventListener('click', () => {
    const open = navToggle.getAttribute('aria-expanded') === 'true';
    navToggle.setAttribute('aria-expanded', String(!open));
    nav?.classList.toggle('is-open', !open);
  });
  document.addEventListener('click', event => {
    if (nav && navToggle && !nav.contains(event.target) && !navToggle.contains(event.target)) {
      nav.classList.remove('is-open');
      navToggle.setAttribute('aria-expanded', 'false');
    }
  });

  const progress = document.getElementById('top-progress');
  const backTop = document.querySelector('.back-top');
  const onScroll = () => {
    const max = document.documentElement.scrollHeight - innerHeight;
    if (progress) progress.style.width = `${max > 0 ? (scrollY / max) * 100 : 0}%`;
    backTop?.classList.toggle('show', scrollY > 500);
  };
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  backTop?.addEventListener('click', () => scrollTo({ top: 0, behavior: 'smooth' }));

  document.querySelectorAll('.filter-btn').forEach(button => {
    button.addEventListener('click', () => {
      document.querySelectorAll('.filter-btn').forEach(item => item.classList.remove('is-active'));
      button.classList.add('is-active');
      document.querySelectorAll('.skill-card').forEach(card => {
        card.hidden = button.dataset.filter !== 'all' && card.dataset.category !== button.dataset.filter;
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
    try {
      await navigator.clipboard.writeText('188888888@qq.com');
      showToast('邮箱已复制', 'Email copied');
    } catch {
      showToast('复制失败，请手动复制', 'Copy failed; please copy manually');
    }
  });
})();
