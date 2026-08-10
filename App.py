import streamlit as st

st.set_page_config(
    page_title="Smart File AI - Platform",
    page_icon="🚀",
    layout="wide"
)

# --- CUSTOM CSS STYLING FOR MODERN COLOR THEME ---
st.markdown("""
<style>
    /* تغيير خلفية الصفحة بالكامل لتدرج كحلي فاخر */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
        color: #f8fafc;
    }

    /* العنوان الرئيسي بتدرج نيون أزرق وبنفسجي */
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }

    .hero-subtitle {
        font-size: 1.15rem;
        color: #94a3b8;
        margin-bottom: 2rem;
    }

    /* كروت الأدوات بتصميم زجاجي احترافي (Glassmorphism) */
    .saas-card {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 28px;
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }

    .saas-card:hover {
        transform: translateY(-5px);
        border-color: #818cf8;
        box-shadow: 0 20px 40px -15px rgba(99, 102, 241, 0.3);
    }

    /* شارات المميزات الملونة (Badges) */
    .badge {
        display: inline-block;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-right: 6px;
        margin-top: 12px;
    }
    
    .badge-cyan { background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); }
    .badge-purple { background: rgba(192, 132, 252, 0.15); color: #c084fc; border: 1px solid rgba(192, 132, 252, 0.3); }
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown('<div class="hero-title">🚀 Smart File AI</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Your Intelligent Workspace for Automated Data Cleaning & AI Document Review</div>', unsafe_allow_html=True)

st.markdown("---")

# --- CARDS SECTION ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="saas-card">
        <h3 style="color: #38bdf8; margin-top:0;">📊 Data Cleaner</h3>
        <p style="color: #cbd5e1; line-height: 1.6;">
            Instantly clean, deduplicate, and format Excel & CSV files with high efficiency. Fix spaces, column types, and duplicate entries in one click.
        </p>
        <span class="badge badge-cyan">Deduplication</span>
        <span class="badge badge-cyan">Trim Spaces</span>
        <span class="badge badge-cyan">Auto-Format</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="saas-card">
        <h3 style="color: #c084fc; margin-top:0;">📝 Document AI & Proofreader</h3>
        <p style="color: #cbd5e1; line-height: 1.6;">
            Scan Word & PDF documents across 5 global languages. Generate instant Quality Scores with interactive error explanations and fixes.
        </p>
        <span class="badge badge-purple">AI Quality Score</span>
        <span class="badge badge-purple">5 Languages</span>
        <span class="badge badge-purple">Accept/Ignore Fixes</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.info("👈 *Get Started:* Select an application from the sidebar on the left.")
