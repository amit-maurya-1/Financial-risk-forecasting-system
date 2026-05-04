CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700;800;900&display=swap');

/* ── ANIMATIONS ── */
@keyframes fadeInUp { 0% { opacity:0; transform:translateY(30px); } 100% { opacity:1; transform:translateY(0); } }
@keyframes scaleIn { 0% { opacity:0; transform:scale(0.92); } 100% { opacity:1; transform:scale(1); } }
@keyframes slideInLeft { 0% { opacity:0; transform:translateX(-20px); } 100% { opacity:1; transform:translateX(0); } }
@keyframes float { 0%,100% { transform:translateY(0px); } 50% { transform:translateY(-12px); } }
@keyframes shimmer { 0% { background-position:-200% 0; } 100% { background-position:200% 0; } }
@keyframes pulse { 0%,100% { opacity:1; transform:scale(1); } 50% { opacity:.6; transform:scale(1.15); } }
@keyframes borderGlow { 0%,100% { border-color:rgba(59,130,246,0.2); } 50% { border-color:rgba(139,92,246,0.45); } }
@keyframes btnGlow { 0%,100% { background-position:0% 50%; } 50% { background-position:100% 50%; } }
@keyframes rotate { 0% { transform:rotate(0deg); } 100% { transform:rotate(360deg); } }
@keyframes orbFloat1 { 0%,100% { transform:translate(0,0) scale(1); } 33% { transform:translate(30px,-20px) scale(1.05); } 66% { transform:translate(-20px,15px) scale(0.95); } }
@keyframes orbFloat2 { 0%,100% { transform:translate(0,0) scale(1); } 33% { transform:translate(-25px,20px) scale(0.95); } 66% { transform:translate(15px,-25px) scale(1.08); } }
@keyframes auroraShift { 0%,100% { opacity:.12; transform:translateX(0); } 50% { opacity:.2; transform:translateX(5%); } }
@keyframes ripple { 0% { transform:scale(0); opacity:.5; } 100% { transform:scale(4); opacity:0; } }
@keyframes countUp { from { opacity:0; transform:translateY(8px); } to { opacity:1; transform:translateY(0); } }
@keyframes glowPulse { 0%,100% { box-shadow:0 0 5px rgba(59,130,246,0.3); } 50% { box-shadow:0 0 20px rgba(59,130,246,0.6),0 0 40px rgba(139,92,246,0.2); } }
@keyframes textGlow { 0%,100% { text-shadow:0 0 10px rgba(96,165,250,0.3); } 50% { text-shadow:0 0 20px rgba(96,165,250,0.6),0 0 40px rgba(167,139,250,0.3); } }
@keyframes cardShine { 0% { left:-100%; } 100% { left:200%; } }

/* ── BASE ── */
html, body, [class*="css"] { font-family:'Inter',sans-serif; }
h1,h2,h3,.page-title,.home-card-title,.sidebar-brand-name { font-family:'Outfit',sans-serif; }

/* ── ANIMATED BACKGROUND ── */
.stApp {
    background:#050b18;
    background-image:
        radial-gradient(ellipse 80% 50% at 50% -20%,rgba(56,100,220,0.15) 0%,transparent 70%),
        radial-gradient(ellipse 60% 40% at 80% 100%,rgba(139,92,246,0.1) 0%,transparent 60%);
    color:#e2e8f0;
    overflow-x:hidden;
}
.stApp::before {
    content:''; position:fixed; top:-30%; left:-10%; width:60%; height:60%;
    background:radial-gradient(circle,rgba(59,130,246,0.08) 0%,transparent 70%);
    animation:orbFloat1 20s ease-in-out infinite; pointer-events:none; z-index:0;
}
.stApp::after {
    content:''; position:fixed; bottom:-20%; right:-10%; width:50%; height:50%;
    background:radial-gradient(circle,rgba(139,92,246,0.06) 0%,transparent 70%);
    animation:orbFloat2 25s ease-in-out infinite; pointer-events:none; z-index:0;
}

/* ── COLUMN LAYOUT ── */
[data-testid="column"] > div { display:flex; flex-direction:column; height:100%; }
div.stButton { margin-top:auto !important; padding-top:12px; }
.home-card { margin-bottom:0; flex-grow:1; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background:linear-gradient(195deg,#060c1a 0%,#0a1224 40%,#0f1a32 100%) !important;
    border-right:1px solid rgba(99,130,190,0.1);
    box-shadow:4px 0 30px rgba(0,0,0,0.4);
}
[data-testid="stSidebar"] * { color:#c8d6e5 !important; }
[data-testid="stSidebar"] [data-testid="stRadio"] label {
    border-radius:12px; padding:10px 14px; margin:3px 0;
    transition:all 0.3s cubic-bezier(.25,.8,.25,1);
    border:1px solid transparent; position:relative; overflow:hidden;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background:rgba(59,130,246,0.08); border-color:rgba(59,130,246,0.15);
    transform:translateX(4px);
}
[data-testid="stSidebar"] [data-testid="stRadio"] label[data-checked="true"],
[data-testid="stSidebar"] [data-testid="stRadio"] [aria-checked="true"] {
    background:linear-gradient(135deg,rgba(59,130,246,0.12),rgba(139,92,246,0.08)) !important;
    border-color:rgba(59,130,246,0.25) !important;
}

/* ── GLASSMORPHISM CARDS ── */
.metric-card {
    background:linear-gradient(135deg,rgba(15,25,50,0.7),rgba(10,18,38,0.5));
    backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px);
    border:1px solid rgba(99,130,190,0.12);
    border-radius:20px; padding:24px 28px; margin:8px 0;
    transition:all 0.4s cubic-bezier(.25,.8,.25,1);
    position:relative; overflow:hidden;
    animation:fadeInUp 0.6s ease-out both;
}
.metric-card::before {
    content:''; position:absolute; top:0; left:0; right:0; height:1px;
    background:linear-gradient(90deg,transparent,rgba(255,255,255,0.1),transparent);
}
.metric-card::after {
    content:''; position:absolute; top:-50%; left:-50%; width:30%; height:200%;
    background:linear-gradient(90deg,transparent,rgba(255,255,255,0.03),transparent);
    transform:rotate(25deg); transition:left 0.8s ease;
}
.metric-card:hover::after { left:120%; }
.metric-card:hover {
    transform:translateY(-6px) scale(1.01);
    box-shadow:0 20px 50px rgba(0,0,0,0.4),0 0 30px rgba(59,130,246,0.08);
    border-color:rgba(99,130,190,0.3);
}

/* ── RESULT BADGES ── */
.result-approved {
    background:linear-gradient(135deg,rgba(6,78,59,0.8),rgba(4,120,87,0.5));
    backdrop-filter:blur(16px); border:1px solid rgba(16,185,129,0.4);
    border-radius:20px; padding:28px; text-align:center;
    font-size:1.4rem; font-weight:700; color:#d1fae5 !important;
    margin:16px 0; box-shadow:0 0 40px rgba(16,185,129,0.12);
    animation:scaleIn 0.5s ease-out both;
}
.result-rejected {
    background:linear-gradient(135deg,rgba(127,29,29,0.8),rgba(153,27,27,0.5));
    backdrop-filter:blur(16px); border:1px solid rgba(239,68,68,0.4);
    border-radius:20px; padding:28px; text-align:center;
    font-size:1.4rem; font-weight:700; color:#fee2e2 !important;
    margin:16px 0; box-shadow:0 0 40px rgba(239,68,68,0.12);
    animation:scaleIn 0.5s ease-out both, borderGlow 3s ease-in-out infinite;
}
.result-neutral {
    background:linear-gradient(135deg,rgba(30,58,95,0.8),rgba(30,64,175,0.4));
    backdrop-filter:blur(16px); border:1px solid rgba(59,130,246,0.35);
    border-radius:20px; padding:28px; text-align:center;
    font-size:1.3rem; font-weight:700; color:#dbeafe !important;
    margin:16px 0; box-shadow:0 0 40px rgba(59,130,246,0.1);
    animation:scaleIn 0.5s ease-out both;
}

/* ── SECTION HEADERS ── */
.section-header {
    background:linear-gradient(90deg,rgba(15,23,50,0.8),transparent);
    border-left:3px solid; border-image:linear-gradient(180deg,#3b82f6,#8b5cf6) 1;
    padding:13px 20px; border-radius:0 12px 12px 0;
    margin:28px 0 18px; font-size:1.05rem; font-weight:600;
    color:#93c5fd; letter-spacing:0.3px;
    animation:slideInLeft 0.5s ease-out both;
}

/* ── LABELS ── */
label { color:#8899b5 !important; font-size:0.85rem !important; font-weight:500 !important; }

/* ── BUTTONS ── */
.stButton > button {
    background:linear-gradient(135deg,#3b82f6 0%,#6366f1 50%,#8b5cf6 100%);
    background-size:200% 200%; animation:btnGlow 4s ease infinite;
    color:white !important; border:none; border-radius:14px;
    padding:14px 32px; font-size:0.95rem; font-weight:600;
    width:100%; transition:all 0.35s cubic-bezier(.25,.8,.25,1);
    letter-spacing:0.5px; box-shadow:0 4px 20px rgba(99,102,241,0.3);
    position:relative; overflow:hidden;
}
.stButton > button::after {
    content:''; position:absolute; top:50%; left:50%;
    width:0; height:0; border-radius:50%;
    background:rgba(255,255,255,0.2);
    transform:translate(-50%,-50%); transition:width 0.6s,height 0.6s;
}
.stButton > button:active::after { width:300px; height:300px; }
.stButton > button:hover {
    transform:translateY(-3px) scale(1.02);
    box-shadow:0 10px 30px rgba(99,102,241,0.45),0 0 50px rgba(59,130,246,0.15);
}
.stButton > button:active { transform:translateY(0) scale(0.98); }

/* ── INPUTS ── */
.stSlider > div > div > div { background:linear-gradient(90deg,#3b82f6,#8b5cf6) !important; }
[data-testid="stNumberInput"] input,
[data-testid="stTextInput"] input,
.stSelectbox select,
[data-testid="stTextArea"] textarea {
    background-color:rgba(10,18,38,0.9) !important; color:#e2e8f0 !important;
    border:1px solid rgba(99,130,190,0.15) !important; border-radius:12px !important;
    transition:border-color 0.3s,box-shadow 0.3s;
}
[data-testid="stNumberInput"] input:focus,
[data-testid="stTextInput"] input:focus,
[data-testid="stTextArea"] textarea:focus {
    border-color:rgba(59,130,246,0.5) !important;
    box-shadow:0 0 15px rgba(59,130,246,0.12),0 0 30px rgba(139,92,246,0.05) !important;
}

/* ── DIVIDERS ── */
hr { border-color:rgba(99,130,190,0.1) !important; }

/* ── INFO BOXES ── */
.info-box {
    background:rgba(59,130,246,0.05); border:1px solid rgba(59,130,246,0.15);
    border-radius:14px; padding:16px 20px; font-size:0.87rem;
    color:#7cb3f4; margin:10px 0; backdrop-filter:blur(10px);
    animation:fadeInUp 0.5s ease-out both;
}

/* ── PAGE TITLE ── */
.page-title {
    font-family:'Outfit',sans-serif; font-size:2.6rem; font-weight:800;
    background:linear-gradient(135deg,#60a5fa 0%,#a78bfa 40%,#c084fc 70%,#f0abfc 100%);
    background-size:200% auto; animation:shimmer 4s linear infinite;
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    margin-bottom:2px; letter-spacing:-0.5px;
}
.page-subtitle {
    color:#566a88; font-size:0.95rem; margin-bottom:30px;
    font-weight:400; letter-spacing:0.3px;
    animation:fadeInUp 0.5s 0.1s ease-out both;
}

/* ── HERO SECTION ── */
.hero-section {
    text-align:center; padding:48px 20px 36px;
    position:relative; overflow:hidden;
    animation:fadeInUp 0.6s ease-out both;
}
.hero-title {
    font-family:'Outfit',sans-serif; font-size:3.2rem; font-weight:900;
    background:linear-gradient(135deg,#60a5fa,#a78bfa,#c084fc,#60a5fa);
    background-size:300% auto; animation:shimmer 5s linear infinite;
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    letter-spacing:-1px; margin-bottom:10px; line-height:1.15;
}
.hero-subtitle {
    color:#566a88; font-size:1.1rem; max-width:600px;
    margin:0 auto 10px; letter-spacing:0.3px; line-height:1.6;
}
.hero-badge {
    display:inline-flex; align-items:center; gap:8px;
    background:rgba(59,130,246,0.08); border:1px solid rgba(59,130,246,0.2);
    border-radius:30px; padding:6px 18px; font-size:0.78rem;
    color:#93c5fd; margin-top:14px; animation:glowPulse 3s ease-in-out infinite;
}

/* ── HOME CARDS ── */
.home-card {
    background:linear-gradient(145deg,rgba(12,20,42,0.75),rgba(8,14,30,0.6));
    backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px);
    border:1px solid rgba(99,130,190,0.1); border-radius:22px;
    padding:34px 26px; text-align:center; min-height:240px;
    transition:all 0.45s cubic-bezier(.25,.8,.25,1);
    cursor:pointer; position:relative; overflow:hidden;
    animation:fadeInUp 0.6s ease-out both;
}
.home-card::before {
    content:''; position:absolute; top:0; left:0; right:0; height:1px;
    background:linear-gradient(90deg,transparent,rgba(255,255,255,0.08),transparent);
}
.home-card::after {
    content:''; position:absolute; top:-50%; left:-50%; width:30%; height:200%;
    background:linear-gradient(90deg,transparent,rgba(255,255,255,0.04),transparent);
    transform:rotate(25deg); animation:cardShine 6s ease-in-out infinite;
}
.home-card:hover {
    border-color:rgba(99,130,246,0.4);
    box-shadow:0 24px 60px rgba(0,0,0,0.35),0 0 50px rgba(59,130,246,0.1);
    transform:translateY(-8px) scale(1.02);
}
.home-card-icon {
    font-size:2.8rem; margin-bottom:16px;
    filter:drop-shadow(0 6px 16px rgba(0,0,0,0.4));
    animation:float 4s ease-in-out infinite;
}
.home-card:nth-child(1) .home-card-icon { animation-delay:0s; }
.home-card:nth-child(2) .home-card-icon { animation-delay:0.5s; }
.home-card:nth-child(3) .home-card-icon { animation-delay:1s; }
.home-card:nth-child(4) .home-card-icon { animation-delay:1.5s; }
.home-card-title {
    font-family:'Outfit',sans-serif; font-size:1.1rem; font-weight:700;
    color:#e2e8f0; margin-bottom:10px; letter-spacing:0.2px;
}
.home-card-desc { font-size:0.82rem; color:#5e7394; line-height:1.55; }

/* ── STEP CARDS ── */
.step-card {
    text-align:center; padding:28px 18px;
    background:linear-gradient(145deg,rgba(12,20,42,0.6),rgba(8,14,30,0.4));
    backdrop-filter:blur(14px); border-radius:18px;
    border:1px solid rgba(99,130,190,0.08);
    transition:all 0.35s cubic-bezier(.25,.8,.25,1);
    animation:fadeInUp 0.6s ease-out both;
}
.step-card:hover {
    border-color:rgba(99,130,190,0.3); transform:translateY(-5px);
    box-shadow:0 12px 30px rgba(0,0,0,0.25);
}

/* ── PLACEHOLDER PANELS ── */
.placeholder-panel {
    display:flex; align-items:center; justify-content:center;
    height:350px; background:linear-gradient(145deg,rgba(12,20,42,0.5),rgba(8,14,30,0.3));
    backdrop-filter:blur(14px); border-radius:20px;
    border:1px dashed rgba(99,130,190,0.12); transition:all 0.3s;
    animation:fadeInUp 0.5s ease-out both;
}
.placeholder-panel:hover { border-color:rgba(99,130,190,0.3); }
.placeholder-icon {
    font-size:3rem; animation:float 3s ease-in-out infinite;
    filter:drop-shadow(0 4px 12px rgba(0,0,0,0.3));
}

/* ── PULSE DOT ── */
.pulse-dot { animation:pulse 2s ease-in-out infinite; }

/* ── STREAMLIT METRICS ── */
[data-testid="stMetric"] {
    background:linear-gradient(145deg,rgba(12,20,42,0.6),rgba(8,14,30,0.4));
    backdrop-filter:blur(12px); border:1px solid rgba(99,130,190,0.1);
    border-radius:16px; padding:16px 20px;
    animation:fadeInUp 0.5s ease-out both;
}
[data-testid="stMetricLabel"] { color:#6b82a6 !important; font-size:0.82rem !important; }
[data-testid="stMetricValue"] { color:#e2e8f0 !important; font-weight:700 !important; }

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {
    gap:8px; background:rgba(12,20,42,0.5);
    border-radius:14px; padding:5px; border:1px solid rgba(99,130,190,0.08);
}
.stTabs [data-baseweb="tab"] {
    border-radius:12px; padding:10px 22px;
    color:#6b82a6 !important; font-weight:500;
    transition:all 0.3s ease;
}
.stTabs [aria-selected="true"] {
    background:linear-gradient(135deg,rgba(59,130,246,0.15),rgba(139,92,246,0.08)) !important;
    color:#93c5fd !important;
}

/* ── DATAFRAME ── */
[data-testid="stDataFrame"] {
    border-radius:16px; overflow:hidden;
    border:1px solid rgba(99,130,190,0.08);
}

/* ── FOOTER ── */
.app-footer {
    text-align:center; padding:36px 0 16px; margin-top:50px;
    border-top:1px solid rgba(99,130,190,0.06);
    animation:fadeInUp 0.5s ease-out both;
}
.footer-line {
    height:2px; margin:0 auto 24px; width:120px;
    background:linear-gradient(90deg,transparent,#3b82f6,#8b5cf6,transparent);
    border-radius:2px;
}
.footer-text { color:#3d4f6b; font-size:0.78rem; letter-spacing:0.5px; }
.footer-badge {
    display:inline-flex; align-items:center; gap:6px;
    background:rgba(59,130,246,0.06); border:1px solid rgba(59,130,246,0.1);
    border-radius:20px; padding:4px 14px; font-size:0.7rem;
    color:#4a6080; margin-top:10px;
}

/* ── SIDEBAR BRAND ── */
.sidebar-brand { text-align:center; padding:30px 16px 18px; animation:fadeInUp 0.5s ease-out both; }
.sidebar-brand-icon {
    width:56px; height:56px; margin:0 auto 14px;
    background:linear-gradient(135deg,#3b82f6,#8b5cf6);
    border-radius:16px; display:flex; align-items:center;
    justify-content:center; font-size:1.7rem;
    box-shadow:0 6px 25px rgba(99,102,241,0.35);
    animation:glowPulse 3s ease-in-out infinite;
}
.sidebar-brand-name {
    font-family:'Outfit',sans-serif; font-size:1.2rem; font-weight:800;
    letter-spacing:2px;
    background:linear-gradient(135deg,#60a5fa,#a78bfa);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    animation:textGlow 3s ease-in-out infinite;
}
.sidebar-brand-sub {
    font-size:0.7rem; color:#3d5074 !important; margin-top:5px;
    letter-spacing:2.5px; text-transform:uppercase;
}

/* ── MODEL STATUS ── */
.model-status {
    padding:16px 18px; margin-top:10px;
    background:rgba(59,130,246,0.03); border:1px solid rgba(99,130,190,0.06);
    border-radius:14px; font-size:0.76rem;
    animation:fadeInUp 0.5s 0.3s ease-out both;
}
.model-status-row {
    display:flex; align-items:center; gap:10px;
    padding:6px 0; color:#4a6080 !important;
    transition:all 0.3s ease;
}
.model-status-row:hover { color:#7cb3f4 !important; transform:translateX(4px); }
.model-status-dot {
    width:7px; height:7px; border-radius:50%;
    background:#10b981; display:inline-block;
    box-shadow:0 0 8px rgba(16,185,129,0.5);
    animation:pulse 2s ease-in-out infinite;
}

/* ── STAT CARDS ── */
.stat-card {
    background:linear-gradient(145deg,rgba(15,25,50,0.7),rgba(10,18,38,0.5));
    backdrop-filter:blur(20px); border:1px solid rgba(99,130,190,0.1);
    border-radius:20px; padding:24px; position:relative; overflow:hidden;
    transition:all 0.4s cubic-bezier(.25,.8,.25,1);
    animation:fadeInUp 0.6s ease-out both;
}
.stat-card:hover {
    transform:translateY(-6px); border-color:rgba(99,130,190,0.25);
    box-shadow:0 16px 40px rgba(0,0,0,0.3),0 0 20px rgba(59,130,246,0.06);
}
.stat-card::before {
    content:''; position:absolute; top:0; left:0; right:0; height:3px;
    border-radius:20px 20px 0 0;
}
.stat-icon {
    font-size:2rem; margin-bottom:12px;
    filter:drop-shadow(0 4px 10px rgba(0,0,0,0.3));
}
.stat-value {
    font-family:'Outfit',sans-serif; font-size:1rem; font-weight:700;
    color:#e2e8f0; margin-bottom:4px; animation:countUp 0.6s ease-out both;
}
.stat-label { font-size:0.78rem; color:#4a6080; }
.stat-badge {
    display:inline-flex; align-items:center; gap:4px;
    font-size:0.65rem; padding:3px 10px; border-radius:20px;
    font-weight:600; letter-spacing:0.5px; margin-top:10px;
}
.stat-active {
    display:flex; align-items:center; gap:6px;
    font-size:0.72rem; margin-top:12px;
}

/* ── ANIMATED STAGGER DELAYS ── */
.delay-1 { animation-delay:0.1s !important; }
.delay-2 { animation-delay:0.2s !important; }
.delay-3 { animation-delay:0.3s !important; }
.delay-4 { animation-delay:0.4s !important; }
.delay-5 { animation-delay:0.5s !important; }

/* ── RESPONSIVE ── */
@media (max-width:768px) {
    .hero-title { font-size:2rem; }
    .page-title { font-size:1.8rem; }
    .home-card { min-height:180px; padding:24px 18px; }
}
</style>
"""
