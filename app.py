import streamlit as st
import numpy as np
import pandas as pd
import joblib
import warnings
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import os

warnings.filterwarnings("ignore")

# Page Config 
st.set_page_config(
    page_title="Financial Risk & Forecasting System",
    page_icon="💹",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS 
st.markdown("""
<style>
/* 🔥 Make column stack properly */
[data-testid="column"] > div {
    display: flex;
    flex-direction: column;
    height: 100%;
}

/* 🔥 Push button to bottom and align */
div.stButton {
    margin-top: auto !important;
    padding-top: 12px;
}

/* 🔥 Ensure consistent spacing */
.home-card {
    margin-bottom: 0;
    flex-grow: 1;
}
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    /* ── Animated background ── */
    .stApp {
        background: #050b18;
        background-image:
            radial-gradient(ellipse 80% 50% at 50% -20%, rgba(56,100,220,0.12) 0%, transparent 70%),
            radial-gradient(ellipse 60% 40% at 80% 100%, rgba(139,92,246,0.08) 0%, transparent 60%);
        color: #e2e8f0;
    }

    /* ── Sidebar — frosted glass ── */
    [data-testid="stSidebar"] {
        background: linear-gradient(195deg, #080e1e 0%, #0d1527 40%, #111c35 100%) !important;
        border-right: 1px solid rgba(99,130,190,0.12);
        box-shadow: 4px 0 24px rgba(0,0,0,0.3);
    }
    [data-testid="stSidebar"] * { color: #c8d6e5 !important; }
    [data-testid="stSidebar"] [data-testid="stRadio"] label {
        border-radius: 10px; padding: 6px 12px; margin: 2px 0;
        transition: all 0.25s ease;
    }
    [data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
        background: rgba(59,130,246,0.1);
    }

    /* ── Glassmorphism cards ── */
    .metric-card {
        background: rgba(15,25,50,0.6);
        backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(99,130,190,0.15);
        border-radius: 16px;
        padding: 22px 26px;
        margin: 8px 0;
        transition: all 0.35s cubic-bezier(.25,.8,.25,1);
        position: relative;
        overflow: hidden;
    }
    .metric-card::before {
        content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.08), transparent);
    }
    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(0,0,0,0.35), 0 0 20px rgba(59,130,246,0.06);
        border-color: rgba(99,130,190,0.25);
    }

    /* ── Result badges ── */
    .result-approved {
        background: linear-gradient(135deg, rgba(6,78,59,0.7), rgba(4,120,87,0.5));
        backdrop-filter: blur(12px);
        border: 1px solid rgba(16,185,129,0.4);
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        font-size: 1.4rem;
        font-weight: 700;
        color: #d1fae5 !important;
        margin: 16px 0;
        box-shadow: 0 0 30px rgba(16,185,129,0.1);
    }
    .result-rejected {
        background: linear-gradient(135deg, rgba(127,29,29,0.7), rgba(153,27,27,0.5));
        backdrop-filter: blur(12px);
        border: 1px solid rgba(239,68,68,0.4);
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        font-size: 1.4rem;
        font-weight: 700;
        color: #fee2e2 !important;
        margin: 16px 0;
        box-shadow: 0 0 30px rgba(239,68,68,0.1);
    }
    .result-neutral {
        background: linear-gradient(135deg, rgba(30,58,95,0.7), rgba(30,64,175,0.4));
        backdrop-filter: blur(12px);
        border: 1px solid rgba(59,130,246,0.35);
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        font-size: 1.3rem;
        font-weight: 700;
        color: #dbeafe !important;
        margin: 16px 0;
        box-shadow: 0 0 30px rgba(59,130,246,0.08);
    }

    /* ── Section headers ── */
    .section-header {
        background: linear-gradient(90deg, rgba(15,23,50,0.7), transparent);
        border-left: 3px solid;
        border-image: linear-gradient(180deg, #3b82f6, #8b5cf6) 1;
        padding: 11px 18px;
        border-radius: 0 10px 10px 0;
        margin: 24px 0 16px 0;
        font-size: 1.05rem;
        font-weight: 600;
        color: #93c5fd;
        letter-spacing: 0.2px;
    }

    /* ── Input labels ── */
    label { color: #8899b5 !important; font-size: 0.85rem !important; font-weight: 500 !important; }

    /* ── Buttons — gradient glow ── */
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #6366f1 50%, #8b5cf6 100%);
        background-size: 200% 200%;
        animation: btnGlow 4s ease infinite;
        color: white !important;
        border: none;
        border-radius: 12px;
        padding: 13px 32px;
        font-size: 0.95rem;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s cubic-bezier(.25,.8,.25,1);
        letter-spacing: 0.5px;
        box-shadow: 0 4px 15px rgba(99,102,241,0.25);
    }
    @keyframes btnGlow {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(99,102,241,0.4), 0 0 40px rgba(59,130,246,0.15);
    }
    .stButton > button:active { transform: translateY(0); }

    /* ── Inputs dark ── */
    .stSlider > div > div > div { background: linear-gradient(90deg, #3b82f6, #8b5cf6) !important; }
    [data-testid="stNumberInput"] input,
    [data-testid="stTextInput"] input,
    .stSelectbox select,
    [data-testid="stTextArea"] textarea {
        background-color: rgba(15,23,42,0.8) !important;
        color: #e2e8f0 !important;
        border: 1px solid rgba(99,130,190,0.2) !important;
        border-radius: 10px !important;
        transition: border-color 0.3s, box-shadow 0.3s;
    }
    [data-testid="stNumberInput"] input:focus,
    [data-testid="stTextInput"] input:focus {
        border-color: rgba(59,130,246,0.5) !important;
        box-shadow: 0 0 12px rgba(59,130,246,0.1) !important;
    }

    /* ── Dividers ── */
    hr { border-color: rgba(99,130,190,0.12) !important; }

    /* ── Info boxes ── */
    .info-box {
        background: rgba(59,130,246,0.06);
        border: 1px solid rgba(59,130,246,0.18);
        border-radius: 12px;
        padding: 14px 18px;
        font-size: 0.87rem;
        color: #7cb3f4;
        margin: 10px 0;
        backdrop-filter: blur(8px);
    }

    /* ── Page title ── */
    .page-title {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 50%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2px;
        letter-spacing: -0.5px;
    }
    .page-subtitle {
        color: #566a88;
        font-size: 0.92rem;
        margin-bottom: 28px;
        font-weight: 400;
        letter-spacing: 0.3px;
    }

    /* ── Home cards — glassmorphism ── */
    .home-card {
        background: rgba(12,20,42,0.65);
        backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(99,130,190,0.12);
        border-radius: 20px;
        padding: 30px 24px;
        text-align: center;
        min-height: 230px;
        transition: all 0.4s cubic-bezier(.25,.8,.25,1);
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }
    .home-card::before {
        content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.07), transparent);
    }
    .home-card::after {
        content: ''; position: absolute; bottom: -50%; left: -20%; width: 140%; height: 100%;
        background: radial-gradient(ellipse, rgba(59,130,246,0.04) 0%, transparent 70%);
        transition: opacity 0.4s;
        opacity: 0;
    }
    .home-card:hover {
        border-color: rgba(99,130,246,0.35);
        box-shadow: 0 16px 48px rgba(0,0,0,0.3), 0 0 40px rgba(59,130,246,0.08);
        transform: translateY(-6px);
    }
    .home-card:hover::after { opacity: 1; }
    .home-card-icon {
        font-size: 2.6rem; margin-bottom: 14px;
        filter: drop-shadow(0 4px 12px rgba(0,0,0,0.3));
    }
    .home-card-title {
        font-size: 1.05rem; font-weight: 700; color: #e2e8f0;
        margin-bottom: 10px; letter-spacing: 0.2px;
    }
    .home-card-desc {
        font-size: 0.82rem; color: #5e7394; line-height: 1.5;
    }

    /* ── Step cards ── */
    .step-card {
        text-align: center; padding: 24px 16px;
        background: rgba(12,20,42,0.5);
        backdrop-filter: blur(12px);
        border-radius: 16px;
        border: 1px solid rgba(99,130,190,0.1);
        transition: all 0.3s ease;
    }
    .step-card:hover {
        border-color: rgba(99,130,190,0.25);
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.2);
    }

    /* ── Placeholder panels ── */
    .placeholder-panel {
        display: flex; align-items: center; justify-content: center;
        height: 320px;
        background: rgba(12,20,42,0.4);
        backdrop-filter: blur(12px);
        border-radius: 16px;
        border: 1px dashed rgba(99,130,190,0.15);
        transition: all 0.3s;
    }
    .placeholder-panel:hover { border-color: rgba(99,130,190,0.3); }

    /* ── Pulse dot animation ── */
    @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.5; } }
    .pulse-dot { animation: pulse 2s ease-in-out infinite; }

    /* ── Streamlit metric styling ── */
    [data-testid="stMetric"] {
        background: rgba(12,20,42,0.5);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(99,130,190,0.1);
        border-radius: 12px;
        padding: 14px 18px;
    }
    [data-testid="stMetricLabel"] { color: #6b82a6 !important; font-size: 0.82rem !important; }
    [data-testid="stMetricValue"] { color: #e2e8f0 !important; font-weight: 700 !important; }

    /* ── Tabs ── */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(12,20,42,0.4);
        border-radius: 12px;
        padding: 4px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        padding: 8px 20px;
        color: #6b82a6 !important;
        font-weight: 500;
    }
    .stTabs [aria-selected="true"] {
        background: rgba(59,130,246,0.15) !important;
        color: #93c5fd !important;
    }

    /* ── Dataframe ── */
    [data-testid="stDataFrame"] {
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid rgba(99,130,190,0.1);
    }

    /* ── Footer ── */
    .app-footer {
        text-align: center; padding: 30px 0 10px; margin-top: 40px;
        border-top: 1px solid rgba(99,130,190,0.08);
        color: #3d4f6b; font-size: 0.75rem;
    }

    /* ── Sidebar brand ── */
    .sidebar-brand {
        text-align: center; padding: 28px 16px 16px;
    }
    .sidebar-brand-icon {
        width: 52px; height: 52px; margin: 0 auto 12px;
        background: linear-gradient(135deg, #3b82f6, #8b5cf6);
        border-radius: 14px; display: flex; align-items: center;
        justify-content: center; font-size: 1.6rem;
        box-shadow: 0 4px 20px rgba(99,102,241,0.3);
    }
    .sidebar-brand-name {
        font-size: 1.1rem; font-weight: 800; letter-spacing: 1.5px;
        background: linear-gradient(135deg, #60a5fa, #a78bfa);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .sidebar-brand-sub {
        font-size: 0.7rem; color: #3d5074 !important; margin-top: 4px;
        letter-spacing: 2px; text-transform: uppercase;
    }

    /* ── Model status cards ── */
    .model-status {
        padding: 14px 16px; margin-top: 8px;
        background: rgba(59,130,246,0.04);
        border: 1px solid rgba(99,130,190,0.08);
        border-radius: 12px; font-size: 0.76rem;
    }
    .model-status-row {
        display: flex; align-items: center; gap: 8px;
        padding: 5px 0; color: #4a6080 !important;
    }
    .model-status-dot {
        width: 6px; height: 6px; border-radius: 50%;
        background: #10b981; display: inline-block;
        box-shadow: 0 0 6px rgba(16,185,129,0.4);
    }
</style>
""", unsafe_allow_html=True)

# Load Models 
BASE = os.path.dirname(__file__)

@st.cache_resource
def load_models():
    models = {}
    try:
        models["stock"]      = joblib.load(os.path.join(BASE, "models/stock_model.pkl"))
        models["loan_model"] = joblib.load(os.path.join(BASE, "models/loan_model.pkl"))
        models["loan_scaler"]= joblib.load(os.path.join(BASE, "models/loan_scaler.pkl"))
        models["fraud"]      = joblib.load(os.path.join(BASE, "models/fraud_model.pkl"))
        models["kmeans"]     = joblib.load(os.path.join(BASE, "models/kmeans_model.pkl"))
    except Exception as e:
        st.error(f"Model loading error: {e}")
    return models

models = load_models()

#  Navigation Helper
NAV_OPTIONS = ["🏠 Dashboard", "📈 Stock Predictor", "🏦 Loan Approval", "🔍 Fraud Detection", "👥 Customer Segments"]

# Apply any pending navigation BEFORE the radio widget renders
if "_nav_target" in st.session_state:
    st.session_state["nav"] = st.session_state["_nav_target"]
    del st.session_state["_nav_target"]

# Sidebar Navigation
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <div class="sidebar-brand-icon">💹</div>
        <div class="sidebar-brand-name">FINRISK</div>
        <div class="sidebar-brand-sub">Intelligence Suite</div>
    </div>
    <hr/>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        options=["🏠 Dashboard", "📈 Stock Predictor", "🏦 Loan Approval", "🔍 Fraud Detection", "👥 Customer Segments"],
        label_visibility="collapsed",
        key="nav"
    )

    st.markdown("<hr/>", unsafe_allow_html=True)
    st.markdown("""
    <div class="model-status">
        <div style="font-weight:600; color:#566a88 !important; margin-bottom:8px; font-size:0.72rem; text-transform:uppercase; letter-spacing:1px;">System Status</div>
        <div class="model-status-row"><span class="model-status-dot pulse-dot"></span> Stock Price — Linear Regression</div>
        <div class="model-status-row"><span class="model-status-dot pulse-dot"></span> Loan Approval — Logistic Regression</div>
        <div class="model-status-row"><span class="model-status-dot pulse-dot"></span> Fraud Detection — Random Forest</div>
        <div class="model-status-row"><span class="model-status-dot pulse-dot"></span> Segmentation — K-Means</div>
    </div>
    """, unsafe_allow_html=True)

 
#   DASHBOARD

if page == "🏠 Dashboard":
    st.markdown('<div class="page-title">Financial Risk & Forecasting System</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle"> Real-time predictions </div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    stats = [
        (c1, "📈", "Stock Prediction", "Linear Regression", "#3b82f6", "Real-time"),
        (c2, "🏦", "Loan Approval",    "Logistic Regression", "#10b981", "Instant"),
        (c3, "🔍", "Fraud Detection",  "Random Forest",       "#f59e0b", "99.9% Acc"),
        (c4, "👥", "Segmentation",     "K-Means Clustering",  "#8b5cf6", "4 Clusters"),
    ]
    for col, icon, title, model_type, color, badge in stats:
        with col:
            st.markdown(f"""
            <div class="metric-card" style="border-top: 3px solid {color};">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                    <div style="font-size:1.8rem; filter:drop-shadow(0 2px 8px rgba(0,0,0,0.3));">{icon}</div>
                    <div style="font-size:0.65rem; padding:3px 10px; background:rgba({int(color[1:3],16)},{int(color[3:5],16)},{int(color[5:7],16)},0.12);
                         border-radius:20px; color:{color}; font-weight:600; letter-spacing:0.5px;">{badge}</div>
                </div>
                <div style="font-size:0.95rem; font-weight:700; color:#e2e8f0; margin-bottom:4px;">{title}</div>
                <div style="font-size:0.75rem; color:#4a6080;">{model_type}</div>
                <div style="font-size:0.7rem; color:{color}; margin-top:10px; display:flex; align-items:center; gap:6px;">
                    <span class="pulse-dot" style="width:6px; height:6px; border-radius:50%; background:{color};
                          display:inline-block; box-shadow:0 0 6px {color}40;"></span> Active
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # Feature cards
    cols = st.columns(4)
    features = [
        ("📈", "Stock Price Predictor", "Predict tomorrow's stock price using today's value. Real-time forecasting for informed trading decisions.", "Use → Stock Predictor", "📈 Stock Predictor"),
        ("🏦", "Loan Approval System",  "Predict loan approval based on income, CIBIL score, loan amount, and employment status.",                  "Use → Loan Approval",  "🏦 Loan Approval"),
        ("🔍", "Fraud Detection",       "Detect fraudulent credit card transactions using 30 PCA-transformed features with high accuracy.",          "Use → Fraud Detection", "🔍 Fraud Detection"),
        ("👥", "Customer Segments",     "Segment customers by spending score into clusters for targeted marketing and personalization.",              "Use → Customer Segments", "👥 Customer Segments"),
    ]
    for col, (icon, title, desc, cta, target_page) in zip(cols, features):
        with col:
            st.markdown(f"""
            <div class="home-card">
                <div class="home-card-icon">{icon}</div>
                <div class="home-card-title">{title}</div>
                <div class="home-card-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(cta, key=f"nav_{target_page}"):
                st.session_state["_nav_target"] = target_page
                st.rerun()

    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">📊 How to Use This System</div>', unsafe_allow_html=True)
    steps = [
        ("1", "Navigate", "Select a module from the left sidebar", "#3b82f6"),
        ("2", "Input Data", "Fill in the required financial parameters", "#10b981"),
        ("3", "Predict", "Click the Predict button to run the model", "#f59e0b"),
        ("4", "Analyze", "Review the result and visual insights", "#8b5cf6"),
    ]
    s1, s2, s3, s4 = st.columns(4)
    for col, (num, title, desc, color) in zip([s1, s2, s3, s4], steps):
        with col:
            st.markdown(f"""
            <div class="step-card">
                <div style="width:36px; height:36px; margin:0 auto 12px; background:linear-gradient(135deg, {color}, {color}88);
                     border-radius:10px; display:flex; align-items:center; justify-content:center;
                     font-size:0.9rem; font-weight:800; color:white;
                     box-shadow:0 4px 12px {color}30;">{num}</div>
                <div style="font-size:0.9rem; font-weight:700; color:#e2e8f0; margin-bottom:6px;">{title}</div>
                <div style="font-size:0.78rem; color:#4a6080; line-height:1.4;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

# STOCK PRICE PREDICTION

elif page == "📈 Stock Predictor":
    st.markdown('<div class="page-title">📈 Stock Price Predictor</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Linear Regression · Predict next trading day\'s price</div>', unsafe_allow_html=True)

    col_form, col_result = st.columns([1, 1.3], gap="large")

    with col_form:
        st.markdown('<div class="section-header">📥 Input Parameters</div>', unsafe_allow_html=True)
        current_price = st.number_input(
            "Current Stock Price (₹ / $)",
            min_value=1.0, max_value=100000.0,
            value=250.0, step=0.5,
            help="Enter today's closing price of the stock"
        )

        st.markdown('<div class="section-header">🧮 Forecast Settings</div>', unsafe_allow_html=True)
        forecast_days = st.slider("Days to Simulate", min_value=1, max_value=30, value=10)

        st.markdown('<div class="info-box">💡 Model trained on historical stock data using next-day price regression. Input today\'s price to get tomorrow\'s prediction.</div>', unsafe_allow_html=True)

        predict_stock = st.button("🔮 Predict Stock Price", key="stock_btn")

    with col_result:
        if predict_stock:
            model_s = models.get("stock")
            if model_s:
                X_input = np.array([[current_price]])
                predicted = model_s.predict(X_input)[0]
                change = predicted - current_price
                pct = (change / current_price) * 100
                direction = "▲" if change >= 0 else "▼"
                color_dir = "#10b981" if change >= 0 else "#ef4444"

                st.markdown(f"""
                <div class="result-neutral" style="border-color:{color_dir}; background: linear-gradient(135deg, #1e293b, #0f172a);">
                    <div style="font-size:0.9rem; color:#94a3b8; margin-bottom:8px;">Predicted Next-Day Price</div>
                    <div style="font-size:2.4rem; font-weight:800; color:#e2e8f0;">₹ {predicted:.2f}</div>
                    <div style="font-size:1rem; color:{color_dir}; margin-top:8px;">
                        {direction} {abs(change):.2f} ({pct:+.2f}%)
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Forecast simulation chart
                prices = [current_price]
                for _ in range(forecast_days):
                    next_p = model_s.predict(np.array([[prices[-1]]]))[0]
                    prices.append(next_p)

                days = list(range(forecast_days + 1))
                colors = ["#3b82f6" if i == 0 else ("#10b981" if prices[i] >= prices[0] else "#ef4444") for i in range(len(prices))]

                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=days, y=prices,
                    mode='lines+markers',
                    line=dict(color='#3b82f6', width=2.5),
                    marker=dict(size=7, color=colors),
                    fill='tozeroy',
                    fillcolor='rgba(59,130,246,0.08)',
                    name='Forecast Price'
                ))
                fig.add_hline(y=current_price, line_dash="dash", line_color="#64748b",
                              annotation_text="Entry Price", annotation_position="right")
                fig.update_layout(
                    title="📊 Price Forecast Simulation",
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(15,23,42,0.6)',
                    font=dict(color='#94a3b8'),
                    xaxis=dict(title="Day", gridcolor='#1e293b', color='#64748b'),
                    yaxis=dict(title="Price", gridcolor='#1e293b', color='#64748b'),
                    margin=dict(l=0, r=0, t=40, b=0),
                    height=300
                )
                st.plotly_chart(fig, use_container_width=True)

                c1, c2, c3 = st.columns(3)
                c1.metric("Entry Price", f"₹{current_price:.2f}")
                c2.metric("Predicted", f"₹{predicted:.2f}", f"{pct:+.2f}%")
                c3.metric("10-Day High", f"₹{max(prices):.2f}")
            else:
                st.error("Stock model not loaded.")
        else:
            st.markdown("""
            <div style="display:flex; align-items:center; justify-content:center; height:300px;
                 background:#1e293b; border-radius:12px; border:1px dashed #334155;">
                <div style="text-align:center; color:#475569;">
                    <div style="font-size:2.5rem;">📈</div>
                    <div style="margin-top:12px; font-size:0.9rem;">Enter stock price and click Predict</div>
                </div>
            </div>
            """, unsafe_allow_html=True)


#  LOAN APPROVAL

elif page == "🏦 Loan Approval":
    st.markdown('<div class="page-title">🏦 Loan Approval Predictor</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Logistic Regression · Instant creditworthiness assessment</div>', unsafe_allow_html=True)

    col_form, col_result = st.columns([1, 1.3], gap="large")

    with col_form:
        st.markdown('<div class="section-header">👤 Personal Information</div>', unsafe_allow_html=True)
        education = st.selectbox("Education Level", ["Graduate", "Not Graduate"])
        self_employed = st.selectbox("Employment Type", ["Salaried", "Self Employed"])

        st.markdown('<div class="section-header">💰 Financial Details</div>', unsafe_allow_html=True)
        income = st.number_input(
            "Annual Income (₹)",
            min_value=100000, max_value=20000000,
            value=5000000, step=100000,
            format="%d"
        )
        loan_amount = st.number_input(
            "Loan Amount Requested (₹)",
            min_value=500000, max_value=50000000,
            value=15000000, step=500000,
            format="%d"
        )
        cibil_score = st.slider("CIBIL Credit Score", min_value=300, max_value=900, value=650, step=1)
        loan_term = st.slider("Loan Term (Years)", min_value=2, max_value=30, value=10, step=1)

        col_r = (income / loan_amount) if loan_amount > 0 else 0
        cibil_status = "Excellent ✅" if cibil_score >= 750 else "Good 👍" if cibil_score >= 650 else "Fair ⚠️" if cibil_score >= 550 else "Poor ❌"
        st.markdown(f"""
        <div class="info-box">
            💳 CIBIL Rating: <b>{cibil_status}</b> &nbsp;|&nbsp;
            📊 Income/Loan Ratio: <b>{col_r:.2f}x</b>
        </div>
        """, unsafe_allow_html=True)

        predict_loan = st.button("🏦 Check Loan Eligibility", key="loan_btn")

    with col_result:
        if predict_loan:
            loan_model  = models.get("loan_model")
            loan_scaler = models.get("loan_scaler")
            if loan_model and loan_scaler:
                edu_enc  = 1 if education == "Graduate" else 0
                emp_enc  = 1 if self_employed == "Self Employed" else 0
                raw = np.array([[income, loan_amount, cibil_score, loan_term, edu_enc, emp_enc]])
                scaled = loan_scaler.transform(raw)
                pred = loan_model.predict(scaled)[0]
                prob = loan_model.predict_proba(scaled)[0]

                if pred == 1:
                    st.markdown(f"""
                    <div class="result-approved">
                        ✅ LOAN APPROVED<br/>
                        <span style="font-size:1rem; font-weight:400;">Approval Confidence: {prob[1]*100:.1f}%</span>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="result-rejected">
                        ❌ LOAN REJECTED<br/>
                        <span style="font-size:1rem; font-weight:400;">Rejection Confidence: {prob[0]*100:.1f}%</span>
                    </div>
                    """, unsafe_allow_html=True)

                # Probability gauge
                fig = go.Figure(go.Indicator(
                    mode="gauge+number+delta",
                    value=prob[1] * 100,
                    title={'text': "Approval Probability (%)", 'font': {'color': '#94a3b8', 'size': 14}},
                    gauge={
                        'axis': {'range': [0, 100], 'tickcolor': '#64748b'},
                        'bar': {'color': '#3b82f6'},
                        'steps': [
                            {'range': [0, 40],   'color': '#7f1d1d'},
                            {'range': [40, 65],  'color': '#78350f'},
                            {'range': [65, 100], 'color': '#064e3b'},
                        ],
                        'threshold': {'line': {'color': '#e2e8f0', 'width': 2}, 'thickness': 0.75, 'value': 50}
                    },
                    number={'suffix': "%", 'font': {'color': '#e2e8f0', 'size': 28}}
                ))
                fig.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#94a3b8'),
                    height=260,
                    margin=dict(l=20, r=20, t=40, b=10)
                )
                st.plotly_chart(fig, use_container_width=True)

                # Factor breakdown
                st.markdown('<div class="section-header">📋 Risk Factor Analysis</div>', unsafe_allow_html=True)
                factors = {
                    "CIBIL Score":       min(100, max(0, (cibil_score - 300) / 600 * 100)),
                    "Income Ratio":      min(100, (income / loan_amount) * 100),
                    "Education":         100 if edu_enc == 1 else 40,
                    "Employment":        70 if emp_enc == 0 else 50,
                }
                fig2 = go.Figure(go.Bar(
                    x=list(factors.values()),
                    y=list(factors.keys()),
                    orientation='h',
                    marker=dict(
                        color=['#10b981' if v >= 60 else '#f59e0b' if v >= 40 else '#ef4444'
                               for v in factors.values()],
                        line=dict(color='rgba(0,0,0,0)')
                    ),
                    text=[f"{v:.0f}%" for v in factors.values()],
                    textposition='inside',
                    textfont=dict(color='white', size=12)
                ))
                fig2.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(15,23,42,0.6)',
                    font=dict(color='#94a3b8'),
                    xaxis=dict(range=[0, 110], gridcolor='#1e293b', color='#64748b'),
                    yaxis=dict(color='#94a3b8'),
                    height=200,
                    margin=dict(l=0, r=0, t=10, b=0)
                )
                st.plotly_chart(fig2, use_container_width=True)
            else:
                st.error("Loan models not loaded.")
        else:
            st.markdown("""
            <div style="display:flex; align-items:center; justify-content:center; height:350px;
                 background:#1e293b; border-radius:12px; border:1px dashed #334155;">
                <div style="text-align:center; color:#475569;">
                    <div style="font-size:2.5rem;">🏦</div>
                    <div style="margin-top:12px; font-size:0.9rem;">Fill in your details and check eligibility</div>
                </div>
            </div>
            """, unsafe_allow_html=True)


# CREDIT CARD FRAUD DETECTION

elif page == "🔍 Fraud Detection":
    st.markdown('<div class="page-title">🔍 Credit Card Fraud Detection</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Random Forest · 30-feature PCA transaction analysis</div>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["⚙️ Manual Entry", "📂 Batch CSV Upload"])

    # Tab 1: Manual Entry
    with tab1:
        col_form, col_result = st.columns([1, 1.3], gap="large")

        with col_form:
            st.markdown('<div class="section-header">📝 Transaction Details</div>', unsafe_allow_html=True)
            time_val = st.number_input("Time (seconds since first transaction)", min_value=0.0, value=50000.0, step=100.0)
            amount   = st.number_input("Transaction Amount (₹ / $)", min_value=0.01, max_value=50000.0, value=150.0, step=0.01)

            st.markdown('<div class="section-header">🔢 PCA Feature Values (V1–V28)</div>', unsafe_allow_html=True)
            st.markdown('<div class="info-box">💡 These are PCA-transformed features from the original transaction data. For a real transaction, these values come from the payment processor.</div>', unsafe_allow_html=True)

            use_preset = st.selectbox(
                "Quick Preset",
                ["Custom Values", "Normal Transaction (Safe)", "Suspicious Transaction (High Risk)"]
            )

            PRESETS = {
                "Normal Transaction (Safe)": [
                    -1.36, -0.07, 2.54, 1.38, -0.34, 0.46, 0.24, 0.10,
                     0.36, 0.09, -0.55, -0.62, -0.99, -0.31, 1.47, 0.21,
                     0.89, 0.14, 1.31, -0.14, -0.02, 0.28, -0.11, 0.07,
                     0.13, -0.19, 0.13, -0.02
                ],
                "Suspicious Transaction (High Risk)": [
                    -3.04, -3.16, 1.09, 2.29, 4.58, 0.42, -2.74, -0.45,
                    -0.99, -3.00, 0.28, -1.74, 0.50, -0.45, 1.29, 1.95,
                    -0.88, 0.35, 1.29, -1.45, -0.23, -0.39, -0.70, -0.22,
                    -0.17, -0.89, 0.12, -0.33
                ]
            }

            v_vals = []
            if use_preset in PRESETS:
                preset_v = PRESETS[use_preset]
                cols3 = st.columns(4)
                for i in range(28):
                    with cols3[i % 4]:
                        v = st.number_input(f"V{i+1}", value=float(preset_v[i]),
                                            format="%.4f", key=f"v{i}")
                        v_vals.append(v)
            else:
                cols3 = st.columns(4)
                for i in range(28):
                    with cols3[i % 4]:
                        v = st.number_input(f"V{i+1}", value=0.0,
                                            format="%.4f", key=f"v{i}")
                        v_vals.append(v)

            predict_fraud = st.button("🔍 Analyze Transaction", key="fraud_btn")

        with col_result:
            if predict_fraud:
                fraud_model = models.get("fraud")
                if fraud_model:
                    features = np.array([[time_val] + v_vals + [amount]])
                    pred   = fraud_model.predict(features)[0]
                    prob   = fraud_model.predict_proba(features)[0]
                    risk   = prob[1] * 100

                    if pred == 1:
                        st.markdown(f"""
                        <div class="result-rejected">
                            🚨 FRAUDULENT TRANSACTION DETECTED<br/>
                            <span style="font-size:1rem; font-weight:400;">Fraud Probability: {risk:.2f}%</span>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class="result-approved">
                            ✅ LEGITIMATE TRANSACTION<br/>
                            <span style="font-size:1rem; font-weight:400;">Fraud Probability: {risk:.2f}%</span>
                        </div>
                        """, unsafe_allow_html=True)

                    # Risk gauge
                    fig = go.Figure(go.Indicator(
                        mode="gauge+number",
                        value=risk,
                        title={'text': "Fraud Risk Score (%)", 'font': {'color': '#94a3b8', 'size': 14}},
                        gauge={
                            'axis': {'range': [0, 100], 'tickcolor': '#64748b'},
                            'bar': {'color': '#ef4444' if risk > 50 else '#10b981'},
                            'steps': [
                                {'range': [0, 30],   'color': '#064e3b'},
                                {'range': [30, 60],  'color': '#78350f'},
                                {'range': [60, 100], 'color': '#7f1d1d'},
                            ],
                        },
                        number={'suffix': "%", 'font': {'color': '#e2e8f0', 'size': 28}}
                    ))
                    fig.update_layout(
                        paper_bgcolor='rgba(0,0,0,0)',
                        font=dict(color='#94a3b8'),
                        height=250,
                        margin=dict(l=20, r=20, t=40, b=10)
                    )
                    st.plotly_chart(fig, use_container_width=True)

                    # Top contributing features (abs values)
                    st.markdown('<div class="section-header">📊 Top Feature Contributions</div>', unsafe_allow_html=True)
                    feature_names = ["Time"] + [f"V{i}" for i in range(1, 29)] + ["Amount"]
                    feature_vals  = [time_val] + v_vals + [amount]
                    top_idx = np.argsort(np.abs(feature_vals))[-10:][::-1]

                    fig3 = go.Figure(go.Bar(
                        x=[feature_names[i] for i in top_idx],
                        y=[feature_vals[i] for i in top_idx],
                        marker_color=['#ef4444' if feature_vals[i] < 0 else '#3b82f6' for i in top_idx]
                    ))
                    fig3.update_layout(
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(15,23,42,0.6)',
                        font=dict(color='#94a3b8'),
                        xaxis=dict(gridcolor='#1e293b', color='#64748b'),
                        yaxis=dict(gridcolor='#1e293b', color='#64748b', title="Feature Value"),
                        height=220,
                        margin=dict(l=0, r=0, t=10, b=0)
                    )
                    st.plotly_chart(fig3, use_container_width=True)

                    # Summary
                    c1, c2, c3 = st.columns(3)
                    c1.metric("Transaction Amount", f"₹{amount:.2f}")
                    c2.metric("Risk Score", f"{risk:.1f}%", delta="HIGH" if risk > 50 else "LOW",
                              delta_color="inverse")
                    c3.metric("Decision", "⚠️ FRAUD" if pred == 1 else "✅ SAFE")
                else:
                    st.error("Fraud model not loaded.")
            else:
                st.markdown("""
                <div style="display:flex; align-items:center; justify-content:center; height:350px;
                     background:#1e293b; border-radius:12px; border:1px dashed #334155;">
                    <div style="text-align:center; color:#475569;">
                        <div style="font-size:2.5rem;">🔍</div>
                        <div style="margin-top:12px; font-size:0.9rem;">Select a preset or enter transaction features</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    #  Tab 2: Batch CSV Upload 
    with tab2:
        st.markdown('<div class="section-header">📂 Batch Transaction Analysis</div>', unsafe_allow_html=True)
        st.markdown('<div class="info-box">Upload a CSV file with columns: Time, V1–V28, Amount (same format as creditcard.csv)</div>', unsafe_allow_html=True)

        uploaded_file = st.file_uploader("Upload Transactions CSV", type=["csv"])
        if uploaded_file:
            df_upload = pd.read_csv(uploaded_file)
            st.write(f"**{len(df_upload)} transactions loaded**")
            st.dataframe(df_upload.head(5), use_container_width=True)

            if st.button("🔍 Run Batch Fraud Analysis"):
                fraud_model = models.get("fraud")
                if fraud_model:
                    feature_cols = ["Time"] + [f"V{i}" for i in range(1, 29)] + ["Amount"]
                    available = [c for c in feature_cols if c in df_upload.columns]
                    if len(available) == 30:
                        X_batch  = df_upload[available].values
                        preds    = fraud_model.predict(X_batch)
                        probs    = fraud_model.predict_proba(X_batch)[:, 1]
                        df_upload["Prediction"] = ["🚨 FRAUD" if p == 1 else "✅ SAFE" for p in preds]
                        df_upload["Fraud_Prob"] = (probs * 100).round(2)

                        fraud_count = (preds == 1).sum()
                        safe_count  = (preds == 0).sum()
                        c1, c2, c3 = st.columns(3)
                        c1.metric("Total Transactions", len(preds))
                        c2.metric("🚨 Fraudulent", fraud_count)
                        c3.metric("✅ Legitimate", safe_count)

                        fig_pie = go.Figure(go.Pie(
                            labels=["Legitimate", "Fraudulent"],
                            values=[safe_count, fraud_count],
                            marker=dict(colors=["#10b981", "#ef4444"]),
                            hole=0.5
                        ))
                        fig_pie.update_layout(
                            paper_bgcolor='rgba(0,0,0,0)',
                            font=dict(color='#94a3b8'),
                            height=250,
                            margin=dict(l=0, r=0, t=10, b=0)
                        )
                        st.plotly_chart(fig_pie, use_container_width=True)
                        st.dataframe(df_upload[["Prediction", "Fraud_Prob"] + available[:5]].head(20), use_container_width=True)
                    else:
                        st.error(f"Expected 30 feature columns. Found: {len(available)}")


#  CUSTOMER SEGMENTATION

elif page == "👥 Customer Segments":
    st.markdown('<div class="page-title">👥 Customer Segmentation</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">K-Means Clustering · 4 Segments by Spending Behavior</div>', unsafe_allow_html=True)

    SEGMENT_INFO = {
        0: {"name": "Budget Shoppers",    "emoji": "🛒", "color": "#3b82f6",
            "desc": "Low spending score. Value-focused buyers. Target with discounts & offers.",
            "strategy": "Discount campaigns, loyalty points, budget product lines"},
        1: {"name": "Standard Customers", "emoji": "🛍️", "color": "#10b981",
            "desc": "Moderate spending. Balanced buyers. Respond to seasonal deals.",
            "strategy": "Seasonal promotions, mid-range products, email campaigns"},
        2: {"name": "Premium Spenders",   "emoji": "💎", "color": "#f59e0b",
            "desc": "High spending score. Brand-conscious & quality-focused shoppers.",
            "strategy": "Premium products, VIP events, personalized recommendations"},
        3: {"name": "Ultra Premium",      "emoji": "👑", "color": "#8b5cf6",
            "desc": "Highest spenders. Luxury buyers with strong brand loyalty.",
            "strategy": "Exclusive memberships, luxury lines, concierge service"},
    }

    col_form, col_result = st.columns([1, 1.3], gap="large")

    with col_form:
        st.markdown('<div class="section-header">📋 Customer Profile</div>', unsafe_allow_html=True)

        spending_score = st.slider(
            "Spending Score (1–100)",
            min_value=1, max_value=100, value=50,
            help="Customer's spending score from loyalty program (1=low, 100=high)"
        )

        # Live preview
        km = models.get("kmeans")
        if km:
            cluster = km.predict(np.array([[spending_score]]))[0]
            info = SEGMENT_INFO.get(cluster, {})
            st.markdown(f"""
            <div class="info-box" style="border-color:{info.get('color','#3b82f6')}; margin-top:16px;">
                {info.get('emoji','')} <b>Live Preview:</b> Score {spending_score} →
                Likely <b>{info.get('name','')}</b>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="section-header">📊 Bulk Analysis</div>', unsafe_allow_html=True)
        st.markdown("**Analyze a group of customers:**")
        bulk_scores = st.text_area(
            "Enter multiple spending scores (comma-separated)",
            value="15, 35, 55, 72, 88, 92",
            help="e.g. 20, 45, 70, 90"
        )
        predict_seg = st.button("🎯 Classify Customers", key="seg_btn")

    with col_result:
        if predict_seg:
            km = models.get("kmeans")
            if km:
                # Single customer
                cluster = km.predict(np.array([[spending_score]]))[0]
                info = SEGMENT_INFO[cluster]
                st.markdown(f"""
                <div class="result-neutral" style="border-color:{info['color']}; background: linear-gradient(135deg, #1e293b, #0f172a);">
                    <div style="font-size:2rem;">{info['emoji']}</div>
                    <div style="font-size:1.4rem; font-weight:700; color:#e2e8f0; margin:8px 0;">
                        Segment {cluster}: {info['name']}
                    </div>
                    <div style="font-size:0.88rem; color:#94a3b8; margin-bottom:12px;">{info['desc']}</div>
                    <div style="background:rgba(255,255,255,0.05); border-radius:6px; padding:10px;
                         font-size:0.82rem; color:{info['color']};">
                        📌 Strategy: {info['strategy']}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Bulk analysis
                try:
                    scores_list = [float(s.strip()) for s in bulk_scores.split(",") if s.strip()]
                    if scores_list:
                        X_bulk    = np.array(scores_list).reshape(-1, 1)
                        clusters  = km.predict(X_bulk)
                        results   = pd.DataFrame({"Spending Score": scores_list, "Cluster": clusters})
                        results["Segment"] = results["Cluster"].map(
                            {k: v["name"] for k, v in SEGMENT_INFO.items()}
                        )

                        # Cluster distribution pie
                        cluster_counts = results["Segment"].value_counts()
                        fig_pie = go.Figure(go.Pie(
                            labels=cluster_counts.index,
                            values=cluster_counts.values,
                            marker=dict(colors=[next(v["color"] for k, v in SEGMENT_INFO.items()
                                                     if v["name"] == name)
                                               for name in cluster_counts.index]),
                            hole=0.4,
                            textinfo='label+percent'
                        ))
                        fig_pie.update_layout(
                            title="Segment Distribution",
                            paper_bgcolor='rgba(0,0,0,0)',
                            font=dict(color='#94a3b8'),
                            height=280,
                            margin=dict(l=0, r=0, t=40, b=0)
                        )
                        st.plotly_chart(fig_pie, use_container_width=True)

                        # Scatter of customers by score + cluster
                        results["Color"] = results["Cluster"].map(
                            {k: v["color"] for k, v in SEGMENT_INFO.items()}
                        )
                        fig_sc = go.Figure()
                        for cid, cinfo in SEGMENT_INFO.items():
                            sub = results[results["Cluster"] == cid]
                            if not sub.empty:
                                fig_sc.add_trace(go.Scatter(
                                    x=sub["Spending Score"],
                                    y=[cid] * len(sub),
                                    mode='markers',
                                    marker=dict(size=14, color=cinfo["color"],
                                                line=dict(color='white', width=1)),
                                    name=cinfo["name"]
                                ))
                        fig_sc.update_layout(
                            title="Customer Placement by Cluster",
                            paper_bgcolor='rgba(0,0,0,0)',
                            plot_bgcolor='rgba(15,23,42,0.6)',
                            font=dict(color='#94a3b8'),
                            xaxis=dict(title="Spending Score", gridcolor='#1e293b', color='#64748b'),
                            yaxis=dict(title="Cluster ID", gridcolor='#1e293b', color='#64748b',
                                       tickmode='array', tickvals=[0,1,2,3],
                                       ticktext=["Budget","Standard","Premium","Ultra"]),
                            height=220,
                            margin=dict(l=0, r=0, t=40, b=0),
                            showlegend=False
                        )
                        st.plotly_chart(fig_sc, use_container_width=True)

                        st.markdown('<div class="section-header">📋 Customer Results Table</div>', unsafe_allow_html=True)
                        st.dataframe(results[["Spending Score", "Segment"]], use_container_width=True, hide_index=True)
                except ValueError:
                    st.error("Please enter valid numeric spending scores separated by commas.")
            else:
                st.error("KMeans model not loaded.")
        else:
            st.markdown("""
            <div style="display:flex; align-items:center; justify-content:center; height:350px;
                 background:#1e293b; border-radius:12px; border:1px dashed #334155;">
                <div style="text-align:center; color:#475569;">
                    <div style="font-size:2.5rem;">👥</div>
                    <div style="margin-top:12px; font-size:0.9rem;">Adjust spending score and click Classify</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Always show segment legend
            st.markdown('<div class="section-header">📌 Segment Reference Guide</div>', unsafe_allow_html=True)
            for cid, info in SEGMENT_INFO.items():
                st.markdown(f"""
                <div class="metric-card" style="border-left: 4px solid {info['color']}; padding:14px 18px;">
                    <div style="display:flex; align-items:center; gap:12px;">
                        <span style="font-size:1.6rem;">{info['emoji']}</span>
                        <div>
                            <div style="font-weight:600; color:#e2e8f0;">Segment {cid}: {info['name']}</div>
                            <div style="font-size:0.82rem; color:#64748b; margin-top:3px;">{info['desc']}</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
