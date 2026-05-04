def hero_section():
    return """
    <div class="hero-section">
        <div class="hero-badge">
            <span class="pulse-dot" style="width:6px;height:6px;border-radius:50%;background:#10b981;display:inline-block;box-shadow:0 0 8px rgba(16,185,129,0.5);"></span>
            All Systems Operational
        </div>
        <div class="hero-title">Financial Risk &<br/>Forecasting Intelligence</div>
        <div class="hero-subtitle">Enterprise-grade predictions for stock markets, loan approvals, fraud detection, and customer segmentation — all in one platform.</div>
    </div>
    """

def stat_card(icon, title, model_type, color, badge, delay_class=""):
    r, g, b = int(color[1:3],16), int(color[3:5],16), int(color[5:7],16)
    return f"""
    <div class="stat-card {delay_class}" style="border-top:none;">
        <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,{color},{color}88);border-radius:20px 20px 0 0;"></div>
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
            <div class="stat-icon" style="animation:float 4s ease-in-out infinite;">{icon}</div>
            <div class="stat-badge" style="background:rgba({r},{g},{b},0.1);color:{color};">{badge}</div>
        </div>
        <div class="stat-value">{title}</div>
        <div class="stat-label">{model_type}</div>
        <div class="stat-active" style="color:{color};">
            <span class="pulse-dot" style="width:6px;height:6px;border-radius:50%;background:{color};display:inline-block;box-shadow:0 0 8px {color}50;"></span>
            <span style="font-size:0.72rem;">Active</span>
        </div>
    </div>
    """

def feature_card(icon, title, desc, delay_class=""):
    return f"""
    <div class="home-card {delay_class}">
        <div class="home-card-icon">{icon}</div>
        <div class="home-card-title">{title}</div>
        <div class="home-card-desc">{desc}</div>
    </div>
    """

def step_card(num, title, desc, color, delay_class=""):
    return f"""
    <div class="step-card {delay_class}">
        <div style="width:40px;height:40px;margin:0 auto 14px;background:linear-gradient(135deg,{color},{color}88);
             border-radius:12px;display:flex;align-items:center;justify-content:center;
             font-size:0.9rem;font-weight:800;color:white;
             box-shadow:0 6px 16px {color}30;">{num}</div>
        <div style="font-size:0.92rem;font-weight:700;color:#e2e8f0;margin-bottom:8px;">{title}</div>
        <div style="font-size:0.78rem;color:#4a6080;line-height:1.5;">{desc}</div>
    </div>
    """

def placeholder_panel(icon, text):
    return f"""
    <div class="placeholder-panel">
        <div style="text-align:center;">
            <div class="placeholder-icon">{icon}</div>
            <div style="margin-top:16px;font-size:0.92rem;color:#475569;">{text}</div>
        </div>
    </div>
    """

def result_card(css_class, main_text, sub_text):
    return f"""
    <div class="{css_class}">
        {main_text}<br/>
        <span style="font-size:1rem;font-weight:400;">{sub_text}</span>
    </div>
    """

def footer():
    return """
    <div class="app-footer">
        <div class="footer-line"></div>
        <div class="footer-text">Built with ❤️ using Streamlit · Powered by Machine Learning</div>
        <div class="footer-badge">
            <span class="pulse-dot" style="width:5px;height:5px;border-radius:50%;background:#10b981;display:inline-block;box-shadow:0 0 6px rgba(16,185,129,0.4);"></span>
            FINRISK Intelligence v2.0
        </div>
    </div>
    """

def sidebar_brand():
    return """
    <div class="sidebar-brand">
        <div class="sidebar-brand-icon">💹</div>
        <div class="sidebar-brand-name">FINRISK</div>
        <div class="sidebar-brand-sub">Intelligence Suite</div>
    </div>
    <hr/>
    """

def sidebar_status():
    return """
    <div class="model-status">
        <div style="font-weight:600;color:#566a88 !important;margin-bottom:10px;font-size:0.72rem;text-transform:uppercase;letter-spacing:1.5px;">System Status</div>
        <div class="model-status-row"><span class="model-status-dot"></span> Stock Price — Linear Regression</div>
        <div class="model-status-row"><span class="model-status-dot"></span> Loan Approval — Logistic Regression</div>
        <div class="model-status-row"><span class="model-status-dot"></span> Fraud Detection — Random Forest</div>
        <div class="model-status-row"><span class="model-status-dot"></span> Segmentation — K-Means</div>
    </div>
    """
