import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="AA Fraud Detection",
    page_icon="🔍",
    layout="wide"
)

# Custom CSS - Purple Gradient Theme
st.markdown("""
<style>
    /* Main background gradient */
    .stApp {
        background: linear-gradient(135deg, #0d0015 0%, #1a0030 30%, #2d0050 60%, #1a0030 100%);
        min-height: 100vh;
    }
    
    /* Header/Hero section */
    .hero-section {
        background: linear-gradient(135deg, #6a0dad 0%, #9b30ff 40%, #bf5fff 70%, #7b2fbe 100%);
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 8px 32px rgba(138, 43, 226, 0.5);
        border: 1px solid rgba(191, 95, 255, 0.3);
    }
    
    /* AA Logo */
    .aa-logo {
        font-size: 64px;
        font-weight: 900;
        background: linear-gradient(180deg, #ffffff 0%, #e0b0ff 50%, #bf5fff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -4px;
        font-family: 'Georgia', serif;
        text-shadow: none;
        display: block;
        line-height: 1;
    }
    
    .hero-title {
        color: #ffffff;
        font-size: 32px;
        font-weight: 700;
        margin: 10px 0 5px 0;
        letter-spacing: 2px;
    }
    
    .hero-subtitle {
        color: #d8b4fe;
        font-size: 16px;
        letter-spacing: 1px;
    }
    
    /* Cards */
    .feature-card {
        background: linear-gradient(145deg, rgba(106, 13, 173, 0.3), rgba(45, 0, 80, 0.6));
        border: 1px solid rgba(191, 95, 255, 0.3);
        border-radius: 15px;
        padding: 25px;
        margin: 10px 0;
        box-shadow: 0 4px 20px rgba(138, 43, 226, 0.2);
        backdrop-filter: blur(10px);
    }
    
    /* Result boxes */
    .result-fraud {
        background: linear-gradient(135deg, rgba(200, 0, 0, 0.3), rgba(100, 0, 50, 0.5));
        border: 2px solid #ff4444;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        animation: pulse 1.5s infinite;
    }
    
    .result-safe {
        background: linear-gradient(135deg, rgba(0, 150, 0, 0.3), rgba(0, 80, 40, 0.5));
        border: 2px solid #44ff88;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
    }
    
    .result-suspicious {
        background: linear-gradient(135deg, rgba(200, 150, 0, 0.3), rgba(100, 70, 0, 0.5));
        border: 2px solid #ffaa00;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 10px rgba(255, 68, 68, 0.5); }
        50% { box-shadow: 0 0 30px rgba(255, 68, 68, 0.9); }
        100% { box-shadow: 0 0 10px rgba(255, 68, 68, 0.5); }
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(145deg, rgba(106, 13, 173, 0.4), rgba(75, 0, 130, 0.6));
        border: 1px solid rgba(191, 95, 255, 0.4);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(138, 43, 226, 0.3);
    }
    
    .metric-value {
        font-size: 28px;
        font-weight: 800;
        color: #bf5fff;
    }
    
    .metric-label {
        font-size: 13px;
        color: #c4b5fd;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    
    /* Detect button */
    .stButton > button {
        background: linear-gradient(135deg, #6a0dad, #9b30ff, #bf5fff) !important;
        color: white !important;
        font-size: 18px !important;
        font-weight: 700 !important;
        padding: 15px 40px !important;
        border-radius: 50px !important;
        border: none !important;
        box-shadow: 0 6px 25px rgba(138, 43, 226, 0.5) !important;
        letter-spacing: 2px !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 35px rgba(191, 95, 255, 0.7) !important;
    }
    
    /* Slider styling */
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #6a0dad, #bf5fff) !important;
    }
    
    /* Section headers */
    .section-header {
        color: #bf5fff;
        font-size: 18px;
        font-weight: 700;
        border-bottom: 2px solid rgba(191, 95, 255, 0.4);
        padding-bottom: 8px;
        margin-bottom: 15px;
        letter-spacing: 1px;
    }
    
    /* All text white */
    .stMarkdown, p, label, .stSlider label {
        color: #e9d5ff !important;
    }
    
    /* Sidebar */
    .css-1d391kg, [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d0015, #1a0030) !important;
        border-right: 1px solid rgba(191, 95, 255, 0.2) !important;
    }
    
    /* Number input */
    .stNumberInput input {
        background: rgba(45, 0, 80, 0.6) !important;
        border: 1px solid rgba(191, 95, 255, 0.4) !important;
        color: white !important;
        border-radius: 8px !important;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 20px;
        color: rgba(196, 181, 253, 0.5);
        font-size: 13px;
        margin-top: 40px;
        border-top: 1px solid rgba(191, 95, 255, 0.2);
    }
    
    /* Hide streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ── HERO SECTION ──────────────────────────────────────────────
st.markdown("""
<div class="hero-section">
    <span class="aa-logo">AA</span>
    <div class="hero-title">AI FRAUD DETECTION SYSTEM</div>
    <div class="hero-subtitle">by Areeb Ahsan &nbsp;|&nbsp; Real-Time Financial Transaction Analysis</div>
</div>
""", unsafe_allow_html=True)

# ── LOAD MODEL ────────────────────────────────────────────────
@st.cache_resource
def load_model():
    return joblib.load("fraud_detection_model.pkl")

model = load_model()

# ── STATS ROW ─────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
stats = [
    ("284,807", "Transactions Analyzed"),
    ("99.9%", "Model Accuracy"),
    ("Real-Time", "Detection Speed"),
    ("ML + AI", "Technology Used"),
]
for col, (val, label) in zip([c1, c2, c3, c4], stats):
    with col:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{val}</div>
            <div class="metric-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── INPUT SECTION ─────────────────────────────────────────────
st.markdown('<div class="section-header">💳 Transaction Details</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown("**Transaction Info**")
    amount = st.number_input("💰 Transaction Amount ($)", min_value=0.0, max_value=50000.0, value=150.0, step=10.0)
    time_val = st.slider("⏱️ Time Since First Transaction (seconds)", 0, 172800, 50000)
    
    st.markdown("**PCA Features V1 – V14**")
    v_vals = {}
    for i in range(1, 15):
        v_vals[f'V{i}'] = st.slider(f"V{i}", -5.0, 5.0, 0.0, key=f"v{i}")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown("**PCA Features V15 – V28**")
    for i in range(15, 29):
        v_vals[f'V{i}'] = st.slider(f"V{i}", -5.0, 5.0, 0.0, key=f"v{i}")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── DETECT BUTTON ─────────────────────────────────────────────
detect = st.button("🔍 RUN FRAUD DETECTION")

if detect:
    # Prepare input
    scaled_amount = (amount - 88.35) / 250.12
    scaled_time   = (time_val - 94813) / 47488
    data = {**{f'V{i}': [v_vals[f'V{i}']] for i in range(1, 29)},
            'scaled_amount': [scaled_amount],
            'scaled_time':   [scaled_time]}
    cols = [f'V{i}' for i in range(1, 29)] + ['scaled_amount', 'scaled_time']
    input_df = pd.DataFrame(data)[cols]

    prediction  = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.markdown("---")
    st.markdown('<div class="section-header">🧾 Detection Result</div>', unsafe_allow_html=True)

    if prediction == 1:
        st.markdown(f"""
        <div class="result-fraud">
            <h1>🚨 FRAUD DETECTED</h1>
            <h3>Fraud Probability: {probability*100:.2f}%</h3>
            <p>⛔ Recommended Action: <strong>BLOCK</strong> this transaction immediately & alert the cardholder!</p>
        </div>
        """, unsafe_allow_html=True)
    elif probability > 0.3:
        st.markdown(f"""
        <div class="result-suspicious">
            <h1>⚠️ SUSPICIOUS</h1>
            <h3>Fraud Probability: {probability*100:.2f}%</h3>
            <p>🔎 Recommended Action: <strong>FLAG</strong> for manual review by the fraud team.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="result-safe">
            <h1>✅ LEGITIMATE</h1>
            <h3>Fraud Probability: {probability*100:.2f}%</h3>
            <p>✅ Recommended Action: <strong>APPROVE</strong> this transaction.</p>
        </div>
        """, unsafe_allow_html=True)

    # Result metrics
    st.markdown("<br>", unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown(f"""<div class="metric-card">
            <div class="metric-value">{probability*100:.2f}%</div>
            <div class="metric-label">Fraud Probability</div>
        </div>""", unsafe_allow_html=True)
    with m2:
        status = "FRAUD 🚨" if prediction == 1 else ("SUSPICIOUS ⚠️" if probability > 0.3 else "LEGITIMATE ✅")
        st.markdown(f"""<div class="metric-card">
            <div class="metric-value" style="font-size:20px">{status}</div>
            <div class="metric-label">Prediction</div>
        </div>""", unsafe_allow_html=True)
    with m3:
        st.markdown(f"""<div class="metric-card">
            <div class="metric-value">${amount:,.2f}</div>
            <div class="metric-label">Transaction Amount</div>
        </div>""", unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    AA · AI Fraud Detection System · Built by Areeb Ahsan · Powered by Machine Learning
</div>
""", unsafe_allow_html=True)