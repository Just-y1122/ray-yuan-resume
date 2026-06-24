from pathlib import Path

root = Path('/mnt/data/ray-yuan-resume')
site = root / 'site'
assets = site / 'assets'
assets.mkdir(parents=True, exist_ok=True)

styles = r'''/* Ray Yuan Resume — pink cat-inspired portfolio */
:root {
  --pink-50: #fff7fa;
  --pink-100: #fff0f6;
  --pink-200: #ffd9e8;
  --pink-300: #ffb8d3;
  --pink-400: #f58db6;
  --pink-500: #ec6fa2;
  --pink-600: #d94d89;
  --rose: #e85d93;
  --ink: #4c3b43;
  --muted: #7e6872;
  --white: #ffffff;
  --line: rgba(236, 111, 162, 0.18);
  --shadow: 0 18px 50px rgba(217, 77, 137, 0.14);
  --shadow-soft: 0 10px 30px rgba(217, 77, 137, 0.1);
  --radius-xl: 32px;
  --radius-lg: 24px;
  --radius-md: 18px;
  --header-h: 76px;
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  min-height: 100vh;
  color: var(--ink);
  background:
    radial-gradient(circle at 10% 0%, rgba(255, 184, 211, .32), transparent 33%),
    radial-gradient(circle at 100% 20%, rgba(245, 141, 182, .22), transparent 28%),
    linear-gradient(180deg, #fff 0%, var(--pink-50) 100%);
  font-family: "FangSong", "STFangsong", "仿宋", "Noto Serif SC", serif;
  overflow-x: hidden;
}

::selection { background: var(--pink-300); color: var(--ink); }
a { color: inherit; text-decoration: none; }
button, input, textarea { font: inherit; }
button { color: inherit; }
img { max-width: 100%; display: block; }

#top-progress {
  position: fixed; inset: 0 auto auto 0; z-index: 9999;
  height: 4px; width: 0;
  background: linear-gradient(90deg, var(--pink-400), var(--rose));
  box-shadow: 0 0 16px var(--pink-400);
}

.page-wipe {
  position: fixed; inset: 0; z-index: 9998; pointer-events: none;
  background: var(--pink-100);
  transform: translateY(-101%);
}
.page-wipe.is-leaving { animation: wipeIn .42s ease forwards; }
@keyframes wipeIn { to { transform: translateY(0); } }

.site-header {
  position: sticky; top: 0; z-index: 1000;
  height: var(--header-h);
  display: flex; align-items: center; gap: 22px;
  width: min(1180px, calc(100% - 32px));
  margin: 12px auto 0;
  padding: 0 18px;
  border: 1px solid rgba(255,255,255,.86);
  background: rgba(255,255,255,.78);
  backdrop-filter: blur(20px);
  box-shadow: var(--shadow-soft);
  border-radius: 999px;
}
.brand { display: inline-flex; align-items: center; gap: 10px; font-weight: 700; white-space: nowrap; }
.brand-name { font-size: 1.05rem; letter-spacing: .04em; }

.cat-mark {
  position: relative; width: 44px; height: 36px; flex: 0 0 auto;
  border: 2px solid var(--pink-400); border-radius: 48% 48% 46% 46%;
  background: #fff;
  box-shadow: inset 0 -5px 0 var(--pink-100);
}
.cat-mark::before, .cat-mark::after {
  content: ""; position: absolute; top: -7px; width: 15px; height: 16px;
  background: #fff; border: 2px solid var(--pink-400); z-index: -1;
}
.cat-mark::before { left: 3px; transform: rotate(-20deg); border-radius: 4px 10px 0 10px; }
.cat-mark::after { right: 3px; transform: rotate(20deg); border-radius: 10px 4px 10px 0; }
.cat-eye { position: absolute; top: 15px; width: 3px; height: 5px; background: var(--ink); border-radius: 50%; }
.cat-eye.left { left: 12px; } .cat-eye.right { right: 12px; }
.cat-nose { position: absolute; left: 50%; top: 18px; width: 5px; height: 4px; border-radius: 50%; background: #f4b645; transform: translateX(-50%); }
.cat-whisker { position: absolute; top: 19px; width: 10px; height: 1px; background: var(--pink-400); }
.cat-whisker.w1 { left: -7px; transform: rotate(8deg); }
.cat-whisker.w2 { left: -7px; top: 24px; transform: rotate(-8deg); }
.cat-whisker.w3 { right: -7px; transform: rotate(-8deg); }
.cat-whisker.w4 { right: -7px; top: 24px; transform: rotate(8deg); }
.mini-bow { position: absolute; right: -6px; top: -7px; width: 20px; height: 14px; }
.mini-bow::before, .mini-bow::after { content: ""; position: absolute; top: 2px; width: 10px; height: 10px; background: var(--rose); border-radius: 60% 35% 60% 35%; }
.mini-bow::before { left: 0; transform: rotate(25deg); }
.mini-bow::after { right: 0; transform: scaleX(-1) rotate(25deg); }
.mini-bow i { position: absolute; left: 7px; top: 4px; width: 7px; height: 7px; background: var(--pink-300); border-radius: 50%; z-index: 2; }

.main-nav { margin-left: auto; }
.main-nav ul { display: flex; gap: 4px; list-style: none; margin: 0; padding: 0; }
.main-nav a {
  position: relative; display: block; padding: 10px 12px; border-radius: 999px;
  color: var(--muted); font-size: .92rem; transition: .25s ease;
}
.main-nav a:hover, .main-nav a[aria-current="page"] { color: var(--rose); background: var(--pink-100); transform: translateY(-1px); }
.header-actions { display: flex; align-items: center; gap: 8px; }
.lang-toggle, .nav-toggle {
  border: 1px solid var(--line); background: #fff; border-radius: 999px;
  cursor: pointer; box-shadow: 0 5px 18px rgba(217,77,137,.08);
}
.lang-toggle { min-width: 52px; padding: 9px 13px; font-weight: 700; color: var(--rose); transition: .25s ease; }
.lang-toggle:hover { transform: translateY(-2px) rotate(-2deg); box-shadow: 0 9px 24px rgba(217,77,137,.16); }
.nav-toggle { display: none; width: 42px; height: 42px; place-items: center; padding: 0; }
.nav-toggle span, .nav-toggle::before, .nav-toggle::after { content: ""; display: block; width: 18px; height: 2px; background: var(--rose); border-radius: 2px; transition: .25s; }
.nav-toggle::before { transform: translateY(-5px); } .nav-toggle::after { transform: translateY(5px); }
.nav-toggle[aria-expanded="true"] span { opacity: 0; }
.nav-toggle[aria-expanded="true"]::before { transform: translateY(2px) rotate(45deg); }
.nav-toggle[aria-expanded="true"]::after { transform: translateY(-2px) rotate(-45deg); }

main { min-height: calc(100vh - var(--header-h)); }
.container { width: min(1120px, calc(100% - 40px)); margin: 0 auto; }
.section { padding: 84px 0; }
.section-tight { padding: 48px 0; }

.hero {
  position: relative; min-height: calc(100vh - 88px);
  display: grid; grid-template-columns: 1.08fr .92fr; align-items: center; gap: 60px;
  width: min(1120px, calc(100% - 40px)); margin: 0 auto; padding: 72px 0 92px;
}
.eyebrow { display: inline-flex; align-items: center; gap: 9px; margin: 0 0 18px; padding: 8px 13px; border-radius: 999px; background: #fff; border: 1px solid var(--line); color: var(--rose); box-shadow: var(--shadow-soft); font-weight: 700; }
.pulse-dot { width: 9px; height: 9px; border-radius: 50%; background: var(--pink-500); box-shadow: 0 0 0 0 rgba(236,111,162,.5); animation: pulse 1.7s infinite; }
@keyframes pulse { 70% { box-shadow: 0 0 0 9px rgba(236,111,162,0); } 100% { box-shadow: 0 0 0 0 rgba(236,111,162,0); } }
.hero h1 { margin: 0; font-size: clamp(3.3rem, 7vw, 6.5rem); line-height: .98; letter-spacing: -.04em; }
.gradient-text { color: var(--rose); background: linear-gradient(135deg, var(--rose), var(--pink-400)); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; }
.wave { display: inline-block; margin-left: .12em; font-size: .62em; transform-origin: 70% 70%; animation: wave 2.4s ease-in-out infinite; }
@keyframes wave { 0%,60%,100%{transform:rotate(0)} 10%{transform:rotate(14deg)} 20%{transform:rotate(-8deg)} 30%{transform:rotate(14deg)} 40%{transform:rotate(-4deg)} 50%{transform:rotate(10deg)} }
.hero-lead { max-width: 650px; margin: 24px 0 0; font-size: clamp(1.08rem, 2vw, 1.3rem); line-height: 1.9; color: var(--muted); }
.hero-actions { display: flex; flex-wrap: wrap; gap: 14px; margin-top: 32px; }
.btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 9px;
  min-height: 48px; padding: 0 22px; border: 1px solid transparent; border-radius: 999px;
  font-weight: 700; cursor: pointer; transition: transform .25s ease, box-shadow .25s ease, background .25s ease;
}
.btn-primary { color: #fff; background: linear-gradient(135deg, var(--pink-500), var(--rose)); box-shadow: 0 12px 28px rgba(232,93,147,.28); }
.btn-primary:hover { transform: translateY(-3px); box-shadow: 0 18px 36px rgba(232,93,147,.34); }
.btn-secondary { background: #fff; border-color: var(--line); color: var(--rose); box-shadow: var(--shadow-soft); }
.btn-secondary:hover { transform: translateY(-3px); background: var(--pink-100); }
.btn-ghost { background: transparent; border-color: var(--line); color: var(--muted); }
.btn svg { width: 18px; height: 18px; }
.hero-stats { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 30px; }
.stat-chip { padding: 10px 14px; border-radius: 14px; background: rgba(255,255,255,.86); border: 1px dashed var(--pink-300); color: var(--muted); box-shadow: 0 7px 20px rgba(217,77,137,.07); }
.stat-chip strong { color: var(--rose); margin-right: 5px; }

.hero-visual { position: relative; min-height: 580px; display: grid; place-items: center; }
.avatar-stage { position: relative; width: min(440px, 88vw); aspect-ratio: 1/1.14; display: grid; place-items: center; }
.avatar-halo { position: absolute; inset: 8% 4% 4%; border-radius: 46% 54% 52% 48% / 48% 45% 55% 52%; background: linear-gradient(145deg, var(--pink-100), #fff); border: 2px dashed var(--pink-300); animation: morph 9s ease-in-out infinite; box-shadow: var(--shadow); }
@keyframes morph { 0%,100%{border-radius:46% 54% 52% 48%/48% 45% 55% 52%} 50%{border-radius:55% 45% 43% 57%/54% 55% 45% 46%} }
.avatar-img { position: relative; z-index: 2; width: 88%; height: 92%; object-fit: contain; object-position: center bottom; filter: drop-shadow(0 22px 24px rgba(111,74,89,.15)); animation: float 4.6s ease-in-out infinite; }
@keyframes float { 0%,100%{transform:translateY(0) rotate(-.5deg)} 50%{transform:translateY(-14px) rotate(.7deg)} }
.orbit { position: absolute; inset: 0; z-index: 1; border: 1px solid rgba(245,141,182,.35); border-radius: 50%; animation: spin 18s linear infinite; }
.orbit::before, .orbit::after { content:""; position:absolute; width:18px; height:18px; background:var(--pink-400); transform:rotate(45deg); border-radius: 5px 12px 5px 12px; }
.orbit::before { left: 8%; top: 18%; } .orbit::after { right: 5%; bottom: 24%; background: var(--pink-300); }
@keyframes spin { to{transform:rotate(360deg)} }
.floating-card { position: absolute; z-index: 3; padding: 12px 16px; border-radius: 16px; background: rgba(255,255,255,.9); border: 1px solid var(--line); box-shadow: var(--shadow-soft); color: var(--rose); font-weight: 700; backdrop-filter: blur(10px); animation: bob 4s ease-in-out infinite; }
.floating-card.one { left: -6%; top: 22%; transform: rotate(-5deg); }
.floating-card.two { right: -4%; bottom: 18%; transform: rotate(5deg); animation-delay: -1.7s; }
@keyframes bob { 0%,100%{translate:0 0} 50%{translate:0 -9px} }

.scroll-cue { position:absolute; left:50%; bottom:22px; transform:translateX(-50%); display:flex; flex-direction:column; align-items:center; gap:6px; color:var(--muted); font-size:.84rem; }
.mouse { width:24px; height:38px; border:2px solid var(--pink-300); border-radius:16px; padding-top:6px; display:flex; justify-content:center; }
.mouse::after { content:""; width:3px; height:7px; background:var(--pink-500); border-radius:2px; animation:scrollDot 1.5s infinite; }
@keyframes scrollDot { from{transform:translateY(0);opacity:1} to{transform:translateY(12px);opacity:0} }

.page-hero { padding: 88px 0 48px; text-align: center; }
.page-kicker { display:inline-flex; align-items:center; gap:8px; padding:8px 14px; border-radius:999px; background:#fff; border:1px solid var(--line); color:var(--rose); box-shadow:var(--shadow-soft); }
.page-hero h1 { margin:20px 0 12px; font-size:clamp(2.8rem,6vw,5.2rem); line-height:1.06; }
.page-hero p { max-width:720px; margin:0 auto; font-size:1.12rem; line-height:1.85; color:var(--muted); }

.grid { display:grid; gap:22px; }
.grid-2 { grid-template-columns:repeat(2,minmax(0,1fr)); }
.grid-3 { grid-template-columns:repeat(3,minmax(0,1fr)); }
.card {
  position:relative; overflow:hidden; padding:28px; border-radius:var(--radius-lg);
  background:rgba(255,255,255,.86); border:1px solid rgba(245,141,182,.24); box-shadow:var(--shadow-soft);
  transition:transform .25s ease, box-shadow .25s ease;
}
.card::after { content:""; position:absolute; width:90px; height:90px; right:-35px; top:-35px; border-radius:50%; background:radial-gradient(circle,var(--pink-200),transparent 70%); opacity:.6; }
.card:hover { box-shadow:var(--shadow); }
.card-icon { width:54px; height:54px; display:grid; place-items:center; border-radius:18px; background:var(--pink-100); color:var(--rose); font-size:1.6rem; margin-bottom:18px; }
.card h2, .card h3 { margin:0 0 10px; }
.card p { margin:0; color:var(--muted); line-height:1.8; }
.card-link { display:flex; flex-direction:column; min-height:240px; }
.card-link .arrow { margin-top:auto; padding-top:22px; color:var(--rose); font-weight:700; }

.section-heading { display:flex; justify-content:space-between; align-items:end; gap:24px; margin-bottom:30px; }
.section-heading h2 { margin:0; font-size:clamp(2rem,4vw,3.2rem); }
.section-heading p { max-width:560px; margin:0; color:var(--muted); line-height:1.7; }

.profile-panel { display:grid; grid-template-columns:.72fr 1.28fr; gap:26px; align-items:stretch; }
.profile-visual { position:relative; min-height:430px; display:grid; place-items:center; background:linear-gradient(145deg,var(--pink-100),#fff); }
.profile-visual img { width:78%; height:380px; object-fit:contain; filter:drop-shadow(0 18px 20px rgba(217,77,137,.12)); }
.profile-copy h2 { font-size:clamp(2rem,4vw,3rem); margin:0 0 18px; }
.profile-copy p { font-size:1.08rem; line-height:2; }
.tag-list { display:flex; flex-wrap:wrap; gap:10px; margin-top:22px; }
.tag { padding:9px 13px; border-radius:999px; background:var(--pink-100); color:var(--rose); border:1px solid var(--line); }

.timeline { position:relative; max-width:980px; margin:0 auto; }
.timeline::before { content:""; position:absolute; left:19px; top:0; bottom:0; width:2px; background:linear-gradient(var(--pink-300),var(--pink-100)); }
.timeline-item { position:relative; padding-left:66px; margin-bottom:28px; }
.timeline-dot { position:absolute; left:6px; top:30px; width:28px; height:28px; border:7px solid #fff; border-radius:50%; background:var(--pink-500); box-shadow:0 0 0 2px var(--pink-300),0 8px 20px rgba(217,77,137,.2); }
.timeline-card { padding:30px; }
.timeline-meta { display:flex; flex-wrap:wrap; gap:10px 18px; align-items:center; color:var(--muted); margin-bottom:12px; }
.timeline-meta time { color:var(--rose); font-weight:700; }
.timeline-card h2 { font-size:1.55rem; margin:0 0 6px; }
.timeline-card h3 { font-size:1.02rem; color:var(--rose); margin:0 0 18px; font-weight:700; }
.bullet-list { margin:0; padding:0; list-style:none; display:grid; gap:13px; }
.bullet-list li { position:relative; padding-left:24px; color:var(--muted); line-height:1.8; }
.bullet-list li::before { content:"♥"; position:absolute; left:0; top:1px; color:var(--pink-400); font-size:.84rem; }
.metric-row { display:flex; flex-wrap:wrap; gap:10px; margin-top:20px; }
.metric { padding:8px 12px; border-radius:12px; background:var(--pink-100); color:var(--rose); font-weight:700; font-size:.92rem; }

.course-cloud { display:flex; flex-wrap:wrap; gap:12px; }
.course-chip { position:relative; padding:12px 16px 12px 38px; border-radius:14px; background:#fff; border:1px solid var(--line); box-shadow:0 7px 20px rgba(217,77,137,.07); transition:.25s; }
.course-chip::before { content:"✦"; position:absolute; left:15px; color:var(--pink-500); }
.course-chip:hover { transform:translateY(-4px) rotate(-1deg); border-color:var(--pink-300); }

.project-card { display:flex; flex-direction:column; min-height:440px; }
.project-top { display:flex; align-items:center; justify-content:space-between; gap:14px; }
.project-number { font-size:3.8rem; line-height:1; color:var(--pink-200); font-weight:900; }
.project-badge { padding:7px 11px; border-radius:999px; background:var(--pink-100); color:var(--rose); font-size:.9rem; }
.project-card h2 { margin:18px 0 6px; font-size:1.55rem; }
.project-card h3 { margin:0 0 18px; color:var(--rose); font-size:1rem; }
.project-card .bullet-list { margin-bottom:22px; }
.project-card .metric-row { margin-top:auto; }

.skill-toolbar { display:flex; flex-wrap:wrap; gap:10px; justify-content:center; margin-bottom:28px; }
.filter-btn { border:1px solid var(--line); background:#fff; color:var(--muted); padding:10px 16px; border-radius:999px; cursor:pointer; transition:.2s; }
.filter-btn:hover, .filter-btn.is-active { background:var(--pink-500); color:#fff; box-shadow:0 8px 22px rgba(236,111,162,.25); }
.skill-card { min-height:210px; }
.skill-card[hidden] { display:none; }
.skill-meter { height:9px; background:var(--pink-100); border-radius:999px; overflow:hidden; margin-top:18px; }
.skill-meter span { display:block; height:100%; width:var(--level); background:linear-gradient(90deg,var(--pink-300),var(--rose)); border-radius:inherit; transform:scaleX(0); transform-origin:left; transition:transform 1.1s cubic-bezier(.2,.8,.2,1); }
.skill-card.is-visible .skill-meter span { transform:scaleX(1); }

.contact-wrap { display:grid; grid-template-columns:.9fr 1.1fr; gap:26px; }
.contact-visual { min-height:520px; display:grid; place-items:center; text-align:center; background:linear-gradient(160deg,var(--pink-100),#fff); }
.mail-cat { position:relative; width:220px; height:165px; margin:0 auto 24px; animation:float 4.6s ease-in-out infinite; }
.envelope { position:absolute; left:10px; right:10px; bottom:0; height:120px; background:#fff; border:3px solid var(--pink-300); border-radius:20px; box-shadow:var(--shadow); }
.envelope::before { content:""; position:absolute; inset:0; background:linear-gradient(145deg,transparent 49%,var(--pink-100) 50%); clip-path:polygon(0 0,100% 0,50% 65%); }
.mail-cat .cat-mark { position:absolute; left:50%; top:4px; transform:translateX(-50%) scale(2.25); z-index:2; }
.contact-list { display:grid; gap:14px; margin-top:24px; }
.contact-item { display:flex; align-items:center; gap:15px; padding:16px; border-radius:18px; background:var(--pink-50); border:1px solid var(--line); }
.contact-item .icon { width:44px; height:44px; display:grid; place-items:center; border-radius:14px; background:#fff; color:var(--rose); box-shadow:0 6px 18px rgba(217,77,137,.1); }
.contact-item strong { display:block; margin-bottom:3px; }
.contact-item span { color:var(--muted); word-break:break-all; }
.contact-actions { display:flex; flex-wrap:wrap; gap:12px; margin-top:24px; }
.toast { position:fixed; left:50%; bottom:28px; z-index:9999; transform:translate(-50%,30px); opacity:0; pointer-events:none; padding:12px 18px; border-radius:999px; background:var(--ink); color:#fff; box-shadow:var(--shadow); transition:.3s; }
.toast.show { opacity:1; transform:translate(-50%,0); }

.site-footer { padding:34px 20px 44px; text-align:center; color:var(--muted); }
.footer-bow { display:inline-block; margin-bottom:10px; color:var(--pink-500); animation:bob 3s ease-in-out infinite; }
.back-top { position:fixed; right:22px; bottom:22px; z-index:900; width:46px; height:46px; border:1px solid var(--line); border-radius:50%; background:#fff; color:var(--rose); box-shadow:var(--shadow-soft); cursor:pointer; opacity:0; transform:translateY(15px); pointer-events:none; transition:.25s; }
.back-top.show { opacity:1; transform:translateY(0); pointer-events:auto; }
.back-top:hover { transform:translateY(-3px) rotate(-8deg); }

.decor-layer { position:fixed; inset:0; pointer-events:none; z-index:-1; overflow:hidden; }
.decor { position:absolute; opacity:.32; animation:drift var(--duration) ease-in-out infinite alternate; }
.decor.heart { width:16px; height:16px; background:var(--pink-300); transform:rotate(45deg); border-radius:4px 9px 4px 9px; }
.decor.star { color:var(--pink-400); font-size:20px; }
@keyframes drift { from{translate:0 -8px; rotate:-4deg} to{translate:10px 20px; rotate:8deg} }
.trail-heart { position:fixed; z-index:9997; pointer-events:none; color:var(--pink-500); animation:trail .9s ease-out forwards; }
@keyframes trail { to { transform:translateY(-28px) scale(.2) rotate(25deg); opacity:0; } }
.reveal { opacity:0; transform:translateY(22px); transition:opacity .75s ease, transform .75s ease; }
.reveal.is-visible { opacity:1; transform:none; }

.not-found { min-height:calc(100vh - 150px); display:grid; place-items:center; text-align:center; padding:60px 20px; }
.not-found h1 { font-size:clamp(6rem,20vw,13rem); line-height:.75; margin:0; color:var(--pink-200); text-shadow:0 10px 0 #fff; }
.not-found h2 { font-size:clamp(2rem,5vw,3.8rem); margin:28px 0 14px; }
.not-found p { color:var(--muted); margin:0 0 28px; }

@media (max-width: 1000px) {
  .site-header { gap:10px; }
  .main-nav a { padding:9px 8px; font-size:.85rem; }
  .hero { grid-template-columns:1fr; text-align:center; padding-top:66px; }
  .hero-copy { order:1; }
  .hero-visual { order:2; min-height:500px; }
  .hero-lead { margin-left:auto; margin-right:auto; }
  .hero-actions,.hero-stats { justify-content:center; }
  .scroll-cue { display:none; }
  .profile-panel,.contact-wrap { grid-template-columns:1fr; }
}

@media (max-width: 820px) {
  :root { --header-h:68px; }
  .site-header { width:calc(100% - 24px); height:64px; margin-top:8px; padding:0 12px 0 15px; }
  .brand-name { display:none; }
  .nav-toggle { display:grid; }
  .main-nav { position:fixed; left:12px; right:12px; top:80px; margin:0; padding:14px; border:1px solid var(--line); border-radius:24px; background:rgba(255,255,255,.96); box-shadow:var(--shadow); opacity:0; transform:translateY(-10px) scale(.98); pointer-events:none; transition:.25s; }
  .main-nav.is-open { opacity:1; transform:none; pointer-events:auto; }
  .main-nav ul { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:8px; }
  .main-nav a { padding:12px; text-align:center; background:var(--pink-50); }
  .grid-3 { grid-template-columns:1fr 1fr; }
  .section-heading { align-items:start; flex-direction:column; }
}

@media (max-width: 620px) {
  .container,.hero { width:min(100% - 28px,1120px); }
  .section { padding:64px 0; }
  .hero { min-height:auto; padding:62px 0 74px; gap:28px; }
  .hero h1 { font-size:clamp(3.1rem,17vw,4.8rem); }
  .hero-lead { font-size:1.02rem; line-height:1.75; }
  .hero-visual { min-height:410px; }
  .avatar-stage { width:min(340px,92vw); }
  .floating-card { font-size:.85rem; padding:9px 12px; }
  .floating-card.one { left:0; } .floating-card.two { right:0; }
  .grid-2,.grid-3 { grid-template-columns:1fr; }
  .card { padding:23px; border-radius:20px; }
  .page-hero { padding:66px 0 34px; }
  .timeline::before { left:12px; }
  .timeline-item { padding-left:42px; }
  .timeline-dot { left:0; width:24px; height:24px; border-width:6px; }
  .timeline-card { padding:22px; }
  .profile-visual { min-height:350px; }
  .profile-visual img { height:310px; }
  .contact-visual { min-height:390px; }
  .back-top { right:14px; bottom:14px; }
  .main-nav ul { grid-template-columns:1fr; }
}

@media (prefers-reduced-motion: reduce) {
  *,*::before,*::after { animation-duration:.01ms !important; animation-iteration-count:1 !important; scroll-behavior:auto !important; transition-duration:.01ms !important; }
  .trail-heart,.decor-layer { display:none !important; }
}
'''

appjs = r'''(() => {
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
'''

favicon = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="18" fill="#fff0f6"/>
<path d="M14 25 18 11l12 8h4l12-8 4 14v18c0 8-8 14-18 14S14 51 14 43Z" fill="#fff" stroke="#ec6fa2" stroke-width="3"/>
<ellipse cx="25" cy="34" rx="2" ry="3" fill="#4c3b43"/><ellipse cx="39" cy="34" rx="2" ry="3" fill="#4c3b43"/>
<ellipse cx="32" cy="39" rx="3" ry="2" fill="#f4b645"/>
<path d="M46 17c-7-7-12 0-7 5 5 5 12 0 7-5Z" fill="#e85d93"/><circle cx="42" cy="20" r="3" fill="#ffb8d3"/>
</svg>'''

header = '''<div id="top-progress"></div><div class="page-wipe"></div><div class="decor-layer"></div>
<header class="site-header">
  <a class="brand" href="index.html" data-aria-zh="返回首页" data-aria-en="Back to home">
    <span class="cat-mark" aria-hidden="true"><span class="cat-eye left"></span><span class="cat-eye right"></span><span class="cat-nose"></span><span class="cat-whisker w1"></span><span class="cat-whisker w2"></span><span class="cat-whisker w3"></span><span class="cat-whisker w4"></span><span class="mini-bow"><i></i></span></span>
    <span class="brand-name" data-zh="媛媛的简历屋" data-en="Ray's Resume Room">媛媛的简历屋</span>
  </a>
  <nav class="main-nav" aria-label="Main navigation">
    <ul>
      <li><a href="index.html" data-page="home" data-zh="首页" data-en="Home">首页</a></li>
      <li><a href="about.html" data-page="about" data-zh="关于我" data-en="About">关于我</a></li>
      <li><a href="education.html" data-page="education" data-zh="教育" data-en="Education">教育</a></li>
      <li><a href="experience.html" data-page="experience" data-zh="实习" data-en="Experience">实习</a></li>
      <li><a href="projects.html" data-page="projects" data-zh="项目" data-en="Projects">项目</a></li>
      <li><a href="skills.html" data-page="skills" data-zh="技能" data-en="Skills">技能</a></li>
      <li><a href="contact.html" data-page="contact" data-zh="联系" data-en="Contact">联系</a></li>
    </ul>
  </nav>
  <div class="header-actions">
    <button class="lang-toggle" type="button" aria-label="Switch language">EN</button>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-label="Toggle navigation"><span></span></button>
  </div>
</header>'''

footer = '''<footer class="site-footer"><div class="footer-bow">୨୧</div><div data-zh="用数据发现答案，也用可爱拥抱世界。" data-en="Finding answers with data, embracing the world with warmth.">用数据发现答案，也用可爱拥抱世界。</div><small>© 2026 Ray Yuan</small></footer>
<button class="back-top" type="button" data-aria-zh="返回顶部" data-aria-en="Back to top">↑</button>
<div class="toast" role="status" aria-live="polite"></div>'''

cat_mark = '''<span class="cat-mark" aria-hidden="true"><span class="cat-eye left"></span><span class="cat-eye right"></span><span class="cat-nose"></span><span class="cat-whisker w1"></span><span class="cat-whisker w2"></span><span class="cat-whisker w3"></span><span class="cat-whisker w4"></span><span class="mini-bow"><i></i></span></span>'''

def page(filename, page_id, title_zh, title_en, content, description):
    html = f'''<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#fff0f6">
  <meta name="description" content="{description}">
  <title>{title_zh}</title>
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="assets/styles.css">
  <script src="assets/app.js" defer></script>
</head>
<body data-page="{page_id}" data-title-zh="{title_zh}" data-title-en="{title_en}">
{header}
<main>
{content}
</main>
{footer}
</body>
</html>'''
    (site / filename).write_text(html, encoding='utf-8')

home = '''<section class="hero">
  <div class="hero-copy reveal">
    <p class="eyebrow"><span class="pulse-dot"></span><span data-zh="求职目标 · 数据分析" data-en="Career Goal · Data Analysis">求职目标 · 数据分析</span></p>
    <h1 data-html-zh="嗨，我是<span class='gradient-text'>媛媛</span><span class='wave'>👋</span>" data-html-en="Hi, I'm <span class='gradient-text'>Ray Yuan</span><span class='wave'>👋</span>">嗨，我是<span class="gradient-text">媛媛</span><span class="wave">👋</span></h1>
    <p class="hero-lead" data-zh="统计学本科生，热爱把复杂数据变成清晰洞察。熟悉 Excel、R、Python、Power BI 与 Tableau，期待用分析能力为业务决策创造真实价值。" data-en="A Statistics graduate who loves turning complex data into clear insights. Skilled in Excel, R, Python, Power BI and Tableau, I aim to create real business value through thoughtful analysis.">统计学本科生，热爱把复杂数据变成清晰洞察。熟悉 Excel、R、Python、Power BI 与 Tableau，期待用分析能力为业务决策创造真实价值。</p>
    <div class="hero-actions">
      <a class="btn btn-primary magnetic" href="experience.html"><span data-zh="查看我的经历" data-en="Explore My Experience">查看我的经历</span><span>→</span></a>
      <a class="btn btn-secondary" href="contact.html"><span data-zh="联系我" data-en="Contact Me">联系我</span><span>♡</span></a>
    </div>
    <div class="hero-stats">
      <span class="stat-chip"><strong>2</strong><span data-zh="段实习" data-en="Internships">段实习</span></span>
      <span class="stat-chip"><strong>3</strong><span data-zh="项校园项目" data-en="Campus Projects">项校园项目</span></span>
      <span class="stat-chip"><strong>6+</strong><span data-zh="项工具技能" data-en="Core Tools">项工具技能</span></span>
    </div>
  </div>
  <div class="hero-visual reveal">
    <div class="avatar-stage">
      <div class="avatar-halo"></div><div class="orbit"></div>
      <img class="avatar-img" src="assets/avatar.webp" alt="Ray Yuan anime avatar">
      <div class="floating-card one">Excel · Python · R</div>
      <div class="floating-card two" data-zh="数据 × 洞察 × 影响" data-en="Data × Insight × Impact">数据 × 洞察 × 影响</div>
    </div>
  </div>
  <a class="scroll-cue" href="#highlights"><span data-zh="向下探索" data-en="Scroll to explore">向下探索</span><span class="mouse"></span></a>
</section>
<section class="section" id="highlights">
  <div class="container">
    <div class="section-heading reveal"><div><p class="eyebrow"><span>୨୧</span><span data-zh="快速认识我" data-en="Quick Introduction">快速认识我</span></p><h2 data-zh="从学习到实践的成长轨迹" data-en="A Journey from Learning to Practice">从学习到实践的成长轨迹</h2></div><p data-zh="每一张卡片都可以点击，进入更完整的经历页面。" data-en="Every card is clickable and leads to a detailed page.">每一张卡片都可以点击，进入更完整的经历页面。</p></div>
    <div class="grid grid-3">
      <a class="card card-link reveal" data-tilt href="education.html"><div class="card-icon">🎓</div><h3 data-zh="统计学教育背景" data-en="Statistics Education">统计学教育背景</h3><p data-zh="系统学习多元统计、数据挖掘、时间序列与统计计算。" data-en="Coursework in multivariate statistics, data mining, time series and statistical computing.">系统学习多元统计、数据挖掘、时间序列与统计计算。</p><span class="arrow" data-zh="查看教育经历 →" data-en="View education →">查看教育经历 →</span></a>
      <a class="card card-link reveal" data-tilt href="experience.html"><div class="card-icon">📊</div><h3 data-zh="数据与运营实习" data-en="Data & Operations Internships">数据与运营实习</h3><p data-zh="参与公益平台项目与企业生产销售数据分析，兼具数据思维与项目落地经验。" data-en="Worked on a public-benefit platform and business data analytics across production and sales.">参与公益平台项目与企业生产销售数据分析，兼具数据思维与项目落地经验。</p><span class="arrow" data-zh="查看实习经历 →" data-en="View experience →">查看实习经历 →</span></a>
      <a class="card card-link reveal" data-tilt href="projects.html"><div class="card-icon">✨</div><h3 data-zh="建模与团队项目" data-en="Modeling & Team Projects">建模与团队项目</h3><p data-zh="担任队长完成数学建模和市场调查项目，并组织大型志愿活动。" data-en="Led mathematical modeling, market research and large volunteer initiatives.">担任队长完成数学建模和市场调查项目，并组织大型志愿活动。</p><span class="arrow" data-zh="查看项目经历 →" data-en="View projects →">查看项目经历 →</span></a>
    </div>
  </div>
</section>'''

about = '''<section class="page-hero container reveal"><span class="page-kicker">♡ <span data-zh="ABOUT ME" data-en="ABOUT ME">ABOUT ME</span></span><h1 data-zh="关于我" data-en="About Me">关于我</h1><p data-zh="理性的数据思维，加上一点细腻与好奇心，构成了现在的我。" data-en="Analytical thinking, curiosity and a thoughtful eye for detail — that is who I am.">理性的数据思维，加上一点细腻与好奇心，构成了现在的我。</p></section>
<section class="section-tight"><div class="container profile-panel">
  <div class="card profile-visual reveal" data-tilt><img src="assets/avatar.webp" alt="Ray Yuan anime avatar"><span class="floating-card two">Ray Yuan · 20</span></div>
  <div class="card profile-copy reveal"><p class="eyebrow"><span>✦</span><span data-zh="我的故事" data-en="My Story">我的故事</span></p><h2 data-zh="用数据发现问题，用行动推动落地" data-en="Finding Problems with Data, Driving Results with Action">用数据发现问题，用行动推动落地</h2><p data-zh="我毕业于杭州师范大学统计学专业，熟练使用 Excel、R、Python 等数据分析工具，具备数据清洗、分析建模与可视化能力。实习中，我参与过高危人群标签体系搭建、癌症风险模型调优，以及生产和销售数据分析。" data-en="I graduated from Hangzhou Normal University with a degree in Statistics. I am proficient in Excel, R and Python, with experience in data cleaning, modeling and visualization. During internships, I helped build a high-risk population tagging system, optimized a cancer-risk model, and analyzed production and sales data.">我毕业于杭州师范大学统计学专业，熟练使用 Excel、R、Python 等数据分析工具，具备数据清洗、分析建模与可视化能力。实习中，我参与过高危人群标签体系搭建、癌症风险模型调优，以及生产和销售数据分析。</p><p data-zh="我也具备项目管理和团队协作经验，能够合理规划进度、明确分工，并把需求转化为可执行的方案。希望未来在数据分析岗位上，持续用洞察支持决策。" data-en="I also bring project management and teamwork experience. I can organize timelines, clarify responsibilities and translate needs into actionable plans. My goal is to keep using data insights to support better decisions.">我也具备项目管理和团队协作经验，能够合理规划进度、明确分工，并把需求转化为可执行的方案。希望未来在数据分析岗位上，持续用洞察支持决策。</p><div class="tag-list"><span class="tag" data-zh="数据分析" data-en="Data Analysis">数据分析</span><span class="tag" data-zh="统计建模" data-en="Statistical Modeling">统计建模</span><span class="tag" data-zh="数据可视化" data-en="Data Visualization">数据可视化</span><span class="tag" data-zh="项目协作" data-en="Project Collaboration">项目协作</span></div></div>
</div></section>
<section class="section"><div class="container"><div class="section-heading reveal"><div><h2 data-zh="我的优势" data-en="My Strengths">我的优势</h2></div><p data-zh="既关注模型与数据，也关注结果能否真正被理解和使用。" data-en="I care not only about models and data, but also whether insights are understood and used.">既关注模型与数据，也关注结果能否真正被理解和使用。</p></div><div class="grid grid-3">
<div class="card reveal" data-tilt><div class="card-icon">🔎</div><h3 data-zh="洞察问题" data-en="Problem Discovery">洞察问题</h3><p data-zh="从数据缺失、异常与趋势中定位关键问题，形成清晰分析路径。" data-en="Identify key issues from missing data, anomalies and trends, then build a clear analysis path.">从数据缺失、异常与趋势中定位关键问题，形成清晰分析路径。</p></div>
<div class="card reveal" data-tilt><div class="card-icon">🧩</div><h3 data-zh="结构化表达" data-en="Structured Communication">结构化表达</h3><p data-zh="将复杂结论转化为报告、图表和可执行建议，服务团队决策。" data-en="Turn complex findings into reports, visuals and actionable recommendations.">将复杂结论转化为报告、图表和可执行建议，服务团队决策。</p></div>
<div class="card reveal" data-tilt><div class="card-icon">🤝</div><h3 data-zh="协作落地" data-en="Collaborative Execution">协作落地</h3><p data-zh="协调不同模块与成员，在明确时间节点内推动任务完成。" data-en="Coordinate teams and modules to deliver work within clear timelines.">协调不同模块与成员，在明确时间节点内推动任务完成。</p></div>
</div></div></section>'''

education = '''<section class="page-hero container reveal"><span class="page-kicker">🎓 <span data-zh="EDUCATION" data-en="EDUCATION">EDUCATION</span></span><h1 data-zh="教育经历" data-en="Education">教育经历</h1><p data-zh="以统计学为基础，建立数据分析、建模与计算能力。" data-en="A Statistics foundation built around analytics, modeling and computation.">以统计学为基础，建立数据分析、建模与计算能力。</p></section>
<section class="section-tight"><div class="container"><div class="timeline">
<div class="timeline-item reveal"><span class="timeline-dot"></span><article class="card timeline-card" data-tilt><div class="timeline-meta"><time>2021.09 — 2025.06</time><span data-zh="浙江 · 杭州" data-en="Hangzhou, Zhejiang">浙江 · 杭州</span></div><h2 data-zh="杭州师范大学" data-en="Hangzhou Normal University">杭州师范大学</h2><h3 data-zh="统计学 · 本科" data-en="B.S. in Statistics">统计学 · 本科</h3><p data-zh="本科阶段重点学习统计理论、机器学习基础、数据工程与统计计算，形成从数据采集、清洗、分析到可视化表达的完整认识。" data-en="Focused on statistical theory, machine-learning fundamentals, data engineering and statistical computing, building an end-to-end understanding from data collection to visualization.">本科阶段重点学习统计理论、机器学习基础、数据工程与统计计算，形成从数据采集、清洗、分析到可视化表达的完整认识。</p><div class="metric-row"><span class="metric" data-zh="文体活动单项奖学金" data-en="Arts & Sports Scholarship">文体活动单项奖学金</span><span class="metric" data-zh="数学建模队长" data-en="Modeling Team Leader">数学建模队长</span></div></article></div>
</div></div></section>
<section class="section"><div class="container"><div class="section-heading reveal"><div><h2 data-zh="主修课程" data-en="Core Courses">主修课程</h2></div><p data-zh="课程覆盖统计分析、算法建模、时间序列和大数据应用。" data-en="Coursework spans statistical analysis, modeling, time series and big-data applications.">课程覆盖统计分析、算法建模、时间序列和大数据应用。</p></div><div class="course-cloud reveal">
<span class="course-chip" data-zh="多元统计分析" data-en="Multivariate Statistics">多元统计分析</span><span class="course-chip" data-zh="数据挖掘" data-en="Data Mining">数据挖掘</span><span class="course-chip" data-zh="时间序列分析" data-en="Time Series Analysis">时间序列分析</span><span class="course-chip" data-zh="随机过程" data-en="Stochastic Processes">随机过程</span><span class="course-chip" data-zh="大数据应用开发" data-en="Big Data Application Development">大数据应用开发</span><span class="course-chip" data-zh="统计计算" data-en="Statistical Computing">统计计算</span>
</div></div></section>'''

experience = '''<section class="page-hero container reveal"><span class="page-kicker">📊 <span data-zh="EXPERIENCE" data-en="EXPERIENCE">EXPERIENCE</span></span><h1 data-zh="实习经历" data-en="Internship Experience">实习经历</h1><p data-zh="从公益项目到企业经营数据，把分析方法放进真实业务场景。" data-en="Applying analytical methods to real-world public-benefit and business scenarios.">从公益项目到企业经营数据，把分析方法放进真实业务场景。</p></section>
<section class="section-tight"><div class="container"><div class="timeline">
<div class="timeline-item reveal"><span class="timeline-dot"></span><article class="card timeline-card" data-tilt><div class="timeline-meta"><time>2023.12 — 2024.04</time><span data-zh="项目运营实习生" data-en="Project Operations Intern">项目运营实习生</span></div><h2 data-zh="字节跳动公益平台项目" data-en="ByteDance Public Welfare Platform Project">字节跳动公益平台项目</h2><h3 data-zh="数据体系 · 模型调优 · 公益共建" data-en="Data System · Model Tuning · Public Collaboration">数据体系 · 模型调优 · 公益共建</h3><ul class="bullet-list"><li data-zh="从0到1搭建高危人群标签体系，解决30%数据缺失问题，使检索与分析效率提升70%。" data-en="Built a high-risk population tagging system from scratch, addressed 30% missing data and improved retrieval and analysis efficiency by 70%.">从0到1搭建高危人群标签体系，解决30%数据缺失问题，使检索与分析效率提升70%。</li><li data-zh="基于 XGBoost 构建癌症风险分层模型，定位高危关键因子，支持医学团队制定筛查策略。" data-en="Built an XGBoost-based cancer risk stratification model to identify key high-risk factors and support screening strategies.">基于 XGBoost 构建癌症风险分层模型，定位高危关键因子，支持医学团队制定筛查策略。</li><li data-zh="参与北京微爱公益基金会防癌早筛公益帮扶计划，推动项目上线，并策划“一图一故事”传播框架。" data-en="Supported a cancer early-screening program with Beijing Weiai Public Welfare Foundation, helping launch the project and design a visual storytelling framework.">参与北京微爱公益基金会防癌早筛公益帮扶计划，推动项目上线，并策划“一图一故事”传播框架。</li></ul><div class="metric-row"><span class="metric">30% <span data-zh="缺失问题解决" data-en="Missing Data Addressed">缺失问题解决</span></span><span class="metric">70% <span data-zh="效率提升" data-en="Efficiency Gain">效率提升</span></span><span class="metric">5000+ <span data-zh="家庭帮扶" data-en="Families Supported">家庭帮扶</span></span></div></article></div>
<div class="timeline-item reveal"><span class="timeline-dot"></span><article class="card timeline-card" data-tilt><div class="timeline-meta"><time>2024.06 — 2024.09</time><span data-zh="数据分析实习生" data-en="Data Analyst Intern">数据分析实习生</span></div><h2 data-zh="广东立顺光学科技有限公司" data-en="Guangdong Lishun Optical Technology Co., Ltd.">广东立顺光学科技有限公司</h2><h3 data-zh="ETL · 分析建模 · 可视化 · 流程优化" data-en="ETL · Modeling · Visualization · Process Optimization">ETL · 分析建模 · 可视化 · 流程优化</h3><ul class="bullet-list"><li data-zh="运用 ETL 技术整合多个数据源中的生产与销售数据，保证数据完整性与准确性。" data-en="Used ETL techniques to integrate production and sales data from multiple sources while ensuring completeness and accuracy.">运用 ETL 技术整合多个数据源中的生产与销售数据，保证数据完整性与准确性。</li><li data-zh="使用 Excel 和 Python 进行数据清洗与分析，并运用机器学习算法挖掘业务问题与趋势。" data-en="Used Excel and Python for data cleaning and analysis, applying machine-learning methods to identify business issues and trends.">使用 Excel 和 Python 进行数据清洗与分析，并运用机器学习算法挖掘业务问题与趋势。</li><li data-zh="通过 Power BI、Tableau 输出可视化分析报告，为团队和管理层提供决策支持。" data-en="Created visual reports with Power BI and Tableau to support team and management decisions.">通过 Power BI、Tableau 输出可视化分析报告，为团队和管理层提供决策支持。</li><li data-zh="分析流程瓶颈并提出优化建议，参与制定改进流程，提高数据使用效率。" data-en="Analyzed process bottlenecks, proposed improvements and helped optimize data-use efficiency.">分析流程瓶颈并提出优化建议，参与制定改进流程，提高数据使用效率。</li></ul><div class="metric-row"><span class="metric">ETL</span><span class="metric">Excel + Python</span><span class="metric">Power BI + Tableau</span></div></article></div>
</div></div></section>'''

projects = '''<section class="page-hero container reveal"><span class="page-kicker">✨ <span data-zh="PROJECTS" data-en="PROJECTS">PROJECTS</span></span><h1 data-zh="项目与校园经历" data-en="Projects & Campus Experience">项目与校园经历</h1><p data-zh="在建模、调研和志愿活动中，锻炼组织、分析与协作能力。" data-en="Building leadership, analysis and collaboration through modeling, research and volunteering.">在建模、调研和志愿活动中，锻炼组织、分析与协作能力。</p></section>
<section class="section-tight"><div class="container grid grid-3">
<article class="card project-card reveal" data-tilt><div class="project-top"><span class="project-number">01</span><span class="project-badge" data-zh="实践部部长" data-en="Practice Department Lead">实践部部长</span></div><h2 data-zh="青年志愿者协会" data-en="Youth Volunteer Association">青年志愿者协会</h2><h3>2022.09 — 2023.06</h3><ul class="bullet-list"><li data-zh="主导年度志愿者动员大会，负责流程、物资和人员分工。" data-en="Led the annual volunteer mobilization event, managing program design, logistics and staffing.">主导年度志愿者动员大会，负责流程、物资和人员分工。</li><li data-zh="协调50+成员执行活动，覆盖全校1000+学生。" data-en="Coordinated 50+ members and reached 1,000+ students campus-wide.">协调50+成员执行活动，覆盖全校1000+学生。</li><li data-zh="吸引300+学生参与，新增志愿者120人。" data-en="Attracted 300+ participants and recruited 120 new volunteers.">吸引300+学生参与，新增志愿者120人。</li></ul><div class="metric-row"><span class="metric">50+ <span data-zh="成员" data-en="Members">成员</span></span><span class="metric">1000+ <span data-zh="覆盖" data-en="Reached">覆盖</span></span><span class="metric" data-zh="年度最佳实践项目" data-en="Best Practice Project">年度最佳实践项目</span></div></article>
<article class="card project-card reveal" data-tilt><div class="project-top"><span class="project-number">02</span><span class="project-badge" data-zh="队长" data-en="Team Leader">队长</span></div><h2 data-zh="美国大学生数学建模竞赛" data-en="MCM/ICM Mathematical Modeling Competition">美国大学生数学建模竞赛</h2><h3>2023.01 — 2023.03</h3><ul class="bullet-list"><li data-zh="围绕赛题核心问题设计建模框架并审核团队论文终稿。" data-en="Designed the modeling framework around the core problem and reviewed the final paper.">围绕赛题核心问题设计建模框架并审核团队论文终稿。</li><li data-zh="协调建模、编程和写作模块，在96小时内完成交付。" data-en="Coordinated modeling, coding and writing to complete the project within 96 hours.">协调建模、编程和写作模块，在96小时内完成交付。</li><li data-zh="使用 SVM、随机森林等方法形成最终解决方案。" data-en="Applied SVM and Random Forest methods to produce the final solution.">使用 SVM、随机森林等方法形成最终解决方案。</li></ul><div class="metric-row"><span class="metric">96h</span><span class="metric">SVM</span><span class="metric">Random Forest</span></div></article>
<article class="card project-card reveal" data-tilt><div class="project-top"><span class="project-number">03</span><span class="project-badge" data-zh="队长" data-en="Team Leader">队长</span></div><h2 data-zh="市场调查与分析大赛" data-en="Market Research & Analysis Competition">市场调查与分析大赛</h2><h3>2022.12 — 2023.03</h3><ul class="bullet-list"><li data-zh="带领团队调查浙江省公共空间，科学采集数据与现场照片。" data-en="Led field research on public spaces across Zhejiang, collecting structured data and photographs.">带领团队调查浙江省公共空间，科学采集数据与现场照片。</li><li data-zh="分析数智化无障碍设计与治理现状，识别提升空间。" data-en="Analyzed the state of digital-accessibility design and governance to identify opportunities for improvement.">分析数智化无障碍设计与治理现状，识别提升空间。</li><li data-zh="汇总调研结果，形成支持决策和优化的建议。" data-en="Synthesized findings into recommendations for decision-making and optimization.">汇总调研结果，形成支持决策和优化的建议。</li></ul><div class="metric-row"><span class="metric" data-zh="实地调研" data-en="Field Research">实地调研</span><span class="metric" data-zh="数据分析" data-en="Data Analysis">数据分析</span><span class="metric" data-zh="团队协作" data-en="Teamwork">团队协作</span></div></article>
</div></section>'''

skills = '''<section class="page-hero container reveal"><span class="page-kicker">🧰 <span data-zh="SKILLS" data-en="SKILLS">SKILLS</span></span><h1 data-zh="技能与荣誉" data-en="Skills & Honors">技能与荣誉</h1><p data-zh="点击分类按钮，查看不同方向的能力。" data-en="Use the filters to explore different skill groups.">点击分类按钮，查看不同方向的能力。</p></section>
<section class="section-tight"><div class="container">
<div class="skill-toolbar reveal"><button class="filter-btn is-active" data-filter="all" data-zh="全部" data-en="All">全部</button><button class="filter-btn" data-filter="analysis" data-zh="分析工具" data-en="Analytics">分析工具</button><button class="filter-btn" data-filter="visual" data-zh="可视化" data-en="Visualization">可视化</button><button class="filter-btn" data-filter="general" data-zh="通用能力" data-en="General">通用能力</button></div>
<div class="grid grid-3">
<article class="card skill-card" data-category="analysis" data-tilt><div class="card-icon">🐍</div><h3>Python</h3><p data-zh="数据清洗、分析建模与机器学习应用。" data-en="Data cleaning, analytical modeling and machine-learning applications.">数据清洗、分析建模与机器学习应用。</p><div class="skill-meter" style="--level:88%"><span></span></div></article>
<article class="card skill-card" data-category="analysis" data-tilt><div class="card-icon">📈</div><h3>R</h3><p data-zh="统计计算、数据处理与模型分析。" data-en="Statistical computing, data processing and model analysis.">统计计算、数据处理与模型分析。</p><div class="skill-meter" style="--level:84%"><span></span></div></article>
<article class="card skill-card" data-category="analysis" data-tilt><div class="card-icon">🧮</div><h3>Excel</h3><p data-zh="数据整理、函数分析、透视表与报告制作。" data-en="Data organization, formulas, pivot tables and reporting.">数据整理、函数分析、透视表与报告制作。</p><div class="skill-meter" style="--level:92%"><span></span></div></article>
<article class="card skill-card" data-category="visual" data-tilt><div class="card-icon">📊</div><h3>Power BI</h3><p data-zh="交互式看板、指标呈现与业务洞察。" data-en="Interactive dashboards, KPI presentation and business insights.">交互式看板、指标呈现与业务洞察。</p><div class="skill-meter" style="--level:82%"><span></span></div></article>
<article class="card skill-card" data-category="visual" data-tilt><div class="card-icon">🎨</div><h3>Tableau</h3><p data-zh="数据可视化、图表设计与故事化表达。" data-en="Data visualization, chart design and visual storytelling.">数据可视化、图表设计与故事化表达。</p><div class="skill-meter" style="--level:80%"><span></span></div></article>
<article class="card skill-card" data-category="general" data-tilt><div class="card-icon">🤍</div><h3 data-zh="项目管理" data-en="Project Management">项目管理</h3><p data-zh="进度规划、任务分工、跨角色协作与推动落地。" data-en="Planning, task allocation, cross-role collaboration and execution.">进度规划、任务分工、跨角色协作与推动落地。</p><div class="skill-meter" style="--level:86%"><span></span></div></article>
</div></div></section>
<section class="section"><div class="container"><div class="section-heading reveal"><div><h2 data-zh="证书与荣誉" data-en="Certificates & Honors">证书与荣誉</h2></div><p data-zh="持续学习，也认真记录每一次成长。" data-en="Continuously learning and celebrating each step of growth.">持续学习，也认真记录每一次成长。</p></div><div class="grid grid-2"><div class="card reveal"><div class="card-icon">🏅</div><h3 data-zh="个人荣誉" data-en="Personal Honor">个人荣誉</h3><p data-zh="2021—2022学年文体活动单项奖学金" data-en="2021–2022 Individual Scholarship for Arts and Sports Activities">2021—2022学年文体活动单项奖学金</p></div><div class="card reveal"><div class="card-icon">📜</div><h3 data-zh="技能证书" data-en="Certificates">技能证书</h3><div class="tag-list"><span class="tag" data-zh="英语四级" data-en="CET-4">英语四级</span><span class="tag" data-zh="英语六级" data-en="CET-6">英语六级</span><span class="tag" data-zh="Office计算机二级" data-en="National Computer Rank Exam Level 2">Office计算机二级</span><span class="tag" data-zh="普通话证书" data-en="Mandarin Certificate">普通话证书</span><span class="tag" data-zh="C2驾驶证" data-en="C2 Driver's License">C2驾驶证</span></div></div></div></div></section>'''

contact = f'''<section class="page-hero container reveal"><span class="page-kicker">💌 <span data-zh="CONTACT" data-en="CONTACT">CONTACT</span></span><h1 data-zh="联系我" data-en="Contact Me">联系我</h1><p data-zh="期待与重视数据、尊重洞察的团队相遇。" data-en="I look forward to meeting a team that values data and meaningful insights.">期待与重视数据、尊重洞察的团队相遇。</p></section>
<section class="section-tight"><div class="container contact-wrap">
<div class="card contact-visual reveal"><div><div class="mail-cat"><div class="envelope"></div>{cat_mark}</div><h2 data-zh="一起聊聊数据吧" data-en="Let's Talk Data">一起聊聊数据吧</h2><p data-zh="点击发送邮件，会打开你设备上的默认邮箱应用。" data-en="Click Send Email to open your device's default email app.">点击发送邮件，会打开你设备上的默认邮箱应用。</p></div></div>
<div class="card reveal"><p class="eyebrow"><span>♡</span><span data-zh="保持联系" data-en="Stay in Touch">保持联系</span></p><h2 data-zh="很高兴认识你" data-en="Nice to Meet You">很高兴认识你</h2><p data-zh="无论是数据分析岗位、项目合作，还是一次简单的交流，都欢迎通过以下方式联系。" data-en="Whether it is a data analyst opportunity, project collaboration or a simple conversation, feel free to reach out.">无论是数据分析岗位、项目合作，还是一次简单的交流，都欢迎通过以下方式联系。</p><div class="contact-list"><a class="contact-item" href="mailto:1521718888@qq.com"><span class="icon">✉</span><span><strong data-zh="电子邮箱" data-en="Email">电子邮箱</strong><span>1521718888@qq.com</span></span></a><a class="contact-item" href="tel:13088888888"><span class="icon">☎</span><span><strong data-zh="联系电话" data-en="Phone">联系电话</strong><span>13088888888</span></span></a><div class="contact-item"><span class="icon">⌖</span><span><strong data-zh="求职方向" data-en="Career Goal">求职方向</strong><span data-zh="数据分析" data-en="Data Analysis">数据分析</span></span></div></div><div class="contact-actions"><a class="btn btn-primary" href="mailto:1521718888@qq.com?subject=Hello%20Ray%20Yuan"><span data-zh="发送邮件" data-en="Send Email">发送邮件</span><span>→</span></a><button class="btn btn-secondary" type="button" data-copy-email><span data-zh="复制邮箱" data-en="Copy Email">复制邮箱</span><span>♡</span></button></div></div>
</div></section>'''

notfound = '''<section class="not-found"><div class="reveal is-visible"><h1>404</h1><h2 data-zh="小猫迷路啦" data-en="The Little Cat Got Lost">小猫迷路啦</h2><p data-zh="这个页面不存在，点击按钮返回媛媛的简历屋。" data-en="This page does not exist. Return to Ray's resume room.">这个页面不存在，点击按钮返回媛媛的简历屋。</p><a class="btn btn-primary" href="index.html"><span data-zh="返回首页" data-en="Back Home">返回首页</span><span>♡</span></a></div></section>'''

assets.joinpath('styles.css').write_text(styles, encoding='utf-8')
assets.joinpath('app.js').write_text(appjs, encoding='utf-8')
assets.joinpath('favicon.svg').write_text(favicon, encoding='utf-8')
page('index.html','home','嗨，我是媛媛｜Ray Yuan','Hi, I’m Ray Yuan',''.join(home),'Ray Yuan 的双语数据分析个人简历网站。')
page('about.html','about','关于我｜Ray Yuan','About Me | Ray Yuan',about,'了解 Ray Yuan 的数据分析背景与个人优势。')
page('education.html','education','教育经历｜Ray Yuan','Education | Ray Yuan',education,'Ray Yuan 的统计学教育背景与主修课程。')
page('experience.html','experience','实习经历｜Ray Yuan','Experience | Ray Yuan',experience,'Ray Yuan 的数据分析与项目运营实习经历。')
page('projects.html','projects','项目经历｜Ray Yuan','Projects | Ray Yuan',projects,'Ray Yuan 的数学建模、市场调研与校园项目经历。')
page('skills.html','skills','技能与荣誉｜Ray Yuan','Skills & Honors | Ray Yuan',skills,'Ray Yuan 的数据分析技能、证书与荣誉。')
page('contact.html','contact','联系我｜Ray Yuan','Contact | Ray Yuan',contact,'通过邮箱或电话联系 Ray Yuan。')
page('404.html','404','页面未找到｜Ray Yuan','Page Not Found | Ray Yuan',notfound,'页面未找到。')

readme = '''# Ray Yuan Resume Website

A bilingual, responsive personal resume website for Ray Yuan.

## Features

- Pink and white cat-inspired visual style
- Chinese / English language switch with local preference storage
- Seven fully navigable pages
- Responsive layout for desktop, tablet and mobile
- Scroll reveal, card tilt, cursor trail and floating decorative animations
- Accessible reduced-motion support
- Email, phone and copy-email interactions
- Automatic deployment to GitHub Pages

## Pages

- Home
- About
- Education
- Experience
- Projects
- Skills & Honors
- Contact

## GitHub Pages

The site is deployed automatically through GitHub Actions. The expected URL is:

`https://just-y1122.github.io/ray-yuan-resume/`
'''
root.joinpath('README.md').write_text(readme, encoding='utf-8')
workflow = '''name: Deploy resume website to GitHub Pages

on:
  push:
    branches: ["main"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: true

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Configure Pages
        uses: actions/configure-pages@v5
      - name: Upload static site
        uses: actions/upload-pages-artifact@v3
        with:
          path: site
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
'''
root.joinpath('.github/workflows/deploy.yml').write_text(workflow, encoding='utf-8')
root.joinpath('.gitignore').write_text('.DS_Store\nThumbs.db\n', encoding='utf-8')
