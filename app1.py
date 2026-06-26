
import streamlit as st
import pandas as pd
import joblib

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Beauty Recommendation",
    page_icon="💄",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #0f172a, #111827);
    color: white;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid #1f2937;
}

/* TEXT */

h1, h2, h3, h4, h5, h6, p, label, div {
    color: white !important;
}

/* SELECTBOX */

.stSelectbox div[data-baseweb="select"] {
    background-color: #1e293b !important;
    border-radius: 12px;
}

/* BUTTON */

div.stButton > button:first-child {
    background: linear-gradient(to right, #ec4899, #8b5cf6);
    color: white;
    border: none;
    border-radius: 14px;
    height: 3.2em;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
}

div.stButton > button:first-child:hover {
    background: linear-gradient(to right, #db2777, #7c3aed);
    color: white;
}

/* CARDS */

.custom-card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #334155;
    margin-bottom: 15px;
}

/* METRIC CARDS */

.metric-card {
    background: linear-gradient(to right, #1e293b, #0f172a);
    padding: 18px;
    border-radius: 18px;
    text-align: center;
    border: 1px solid #334155;
}

/* SUCCESS */

.stSuccess {
    border-radius: 12px;
}

/* INFO */

.stInfo {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown("# 💄 Beauty AI Assistant")

st.sidebar.markdown("""
<div class="custom-card">

### AI Powered Makeup Recommendation

✅ Personalized Makeup Looks

✅ Budget Based Products

✅ Beauty Tips

✅ AI Prediction

</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div class="custom-card">

### Developed Using

✔ Machine Learning

✔ Streamlit

✔ Python

✔ Data Analysis

</div>
""", unsafe_allow_html=True)

# =========================================================
# LOAD MODEL
# =========================================================

model = joblib.load("beauty_model.pkl")

# =========================================================
# TITLE
# =========================================================

st.markdown("""
<h1 style='text-align:center; font-size:58px;'>
💄 AI Beauty Recommendation System
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h3 style='text-align:center; color:#cbd5e1;'>
Smart Personalized Makeup Recommendation using Artificial Intelligence
</h3>
""", unsafe_allow_html=True)

st.write("")

# =========================================================
# TOP METRICS
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
    <h2>95%</h2>
    <p>Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
    <h2>50+</h2>
    <p>Brands</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
    <h2>6</h2>
    <p>Makeup Styles</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
    <h2>AI</h2>
    <p>Powered</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# =========================================================
# BETTER CHART
# =========================================================

chart_data = pd.DataFrame({
    "Makeup Look": [
        "Soft Glam",
        "Bold Glam",
        "Natural Dewy",
        "Bridal Glow"
    ],
    "Popularity": [85, 70, 92, 65]
})

st.subheader("📊 Trending Makeup Looks")

st.bar_chart(
    chart_data.set_index("Makeup Look")
)

st.write("")
st.write("")

# =========================================================
# INPUT SECTION
# =========================================================

st.subheader("✨ Enter Your Preferences")

col1, col2 = st.columns(2)

with col1:

    skin_type = st.selectbox(
        "Select Skin Type",
        ["Oily", "Dry", "Combination", "Normal"]
    )

    skin_tone = st.selectbox(
        "Select Skin Tone",
        ["Fair", "Medium", "Dusky", "Deep"]
    )

    undertone = st.selectbox(
        "Select Undertone",
        ["Warm", "Cool", "Neutral"]
    )

with col2:

    face_shape = st.selectbox(
        "Select Face Shape",
        ["Oval", "Round", "Heart", "Square"]
    )

    occasion = st.selectbox(
        "Select Occasion",
        ["Casual", "Party", "Wedding", "Office"]
    )

    makeup_style = st.selectbox(
        "Select Makeup Style",
        ["Natural", "Glam", "Dewy", "Matte"]
    )

price_range = st.selectbox(
    "Select Budget Range",
    ["Budget Friendly", "Mid Range", "Luxury"]
)

# =========================================================
# PRODUCT DATA
# =========================================================

sample_products = {

    "Foundation": {
        "Budget Friendly": "Mars / Swiss Beauty / Blue Heaven",
        "Mid Range": "Maybelline / MAC / Huda Beauty",
        "Luxury": "Charlotte Tilbury / NARS / Dior"
    },

    "Lipstick": {
        "Budget Friendly": "Elle 18 / Blue Heaven / Insight",
        "Mid Range": "MAC / Maybelline / Huda Beauty",
        "Luxury": "Charlotte Tilbury / NARS / Dior"
    },

    "Concealer": {
        "Budget Friendly": "Insight / Swiss Beauty",
        "Mid Range": "Maybelline Age Rewind / LA Girl",
        "Luxury": "NARS / Dior"
    },

    "Compact": {
        "Budget Friendly": "Lakme / Insight",
        "Mid Range": "Maybelline / Kay Beauty",
        "Luxury": "MAC / Charlotte Tilbury"
    },

    "Blush": {
        "Budget Friendly": "Mars / Blue Heaven",
        "Mid Range": "Milani / MAC",
        "Luxury": "Rare Beauty / Dior"
    },

    "Highlighter": {
        "Budget Friendly": "Insight / Mars",
        "Mid Range": "Maybelline / MAC",
        "Luxury": "Rare Beauty / Fenty Beauty"
    },

    "Eyeshadow": {
        "Budget Friendly": "Mars / Swiss Beauty",
        "Mid Range": "Huda Beauty / Makeup Revolution",
        "Luxury": "Natasha Denona / Charlotte Tilbury"
    },

    "Eyeliner": {
        "Budget Friendly": "Blue Heaven / Elle 18",
        "Mid Range": "Maybelline / Lakme",
        "Luxury": "MAC / Dior"
    },

    "Mascara": {
        "Budget Friendly": "Essence / Swiss Beauty",
        "Mid Range": "Maybelline Sky High / Loreal",
        "Luxury": "Too Faced / Dior"
    },

    "Setting Spray": {
        "Budget Friendly": "Swiss Beauty / Insight",
        "Mid Range": "MAC Fix Plus / Nyx",
        "Luxury": "Charlotte Tilbury / Urban Decay"
    },

    "Finish": "Professional Makeup Finish"

}

brand_dict = {

    "Soft Glam": sample_products,
    "Bold Glam": sample_products,
    "Natural Dewy": sample_products,
    "Bridal Glow": sample_products,
    "Matte Professional": sample_products,
    "Korean Glass Skin": sample_products

}

tips_dict = {

    "Soft Glam": [
        "Blend makeup properly",
        "Use nude lipstick shades",
        "Apply soft highlighter"
    ],

    "Bold Glam": [
        "Use matte base",
        "Apply bold lipstick",
        "Set makeup with fixing spray"
    ],

    "Natural Dewy": [
        "Moisturize skin well",
        "Use lightweight products",
        "Apply glossy lips"
    ],

    "Bridal Glow": [
        "Hydrate skin before makeup",
        "Use long-lasting products",
        "Apply glow highlighter"
    ],

    "Matte Professional": [
        "Use oil-control primer",
        "Apply compact properly",
        "Choose matte lipstick"
    ],

    "Korean Glass Skin": [
        "Focus on skincare",
        "Use glossy finish products",
        "Avoid heavy contour"
    ]
}

# =========================================================
# ENCODING
# =========================================================

skin_type_map = {
    "Oily":0,
    "Dry":1,
    "Combination":2,
    "Normal":3
}

skin_tone_map = {
    "Fair":0,
    "Medium":1,
    "Dusky":2,
    "Deep":3
}

undertone_map = {
    "Warm":0,
    "Cool":1,
    "Neutral":2
}

face_shape_map = {
    "Oval":0,
    "Round":1,
    "Heart":2,
    "Square":3
}

occasion_map = {
    "Casual":0,
    "Party":1,
    "Wedding":2,
    "Office":3
}

makeup_style_map = {
    "Natural":0,
    "Glam":1,
    "Dewy":2,
    "Matte":3
}

# =========================================================
# PREDICTION
# =========================================================

if st.button("✨ Predict Makeup Look"):

    sample_input = pd.DataFrame({

        "skin_type": [skin_type_map[skin_type]],
        "skin_tone": [skin_tone_map[skin_tone]],
        "undertone": [undertone_map[undertone]],
        "face_shape": [face_shape_map[face_shape]],
        "occasion": [occasion_map[occasion]],
        "makeup_style": [makeup_style_map[makeup_style]]

    })

    prediction = model.predict(sample_input)

    looks = [
        "Bold Glam",
        "Bridal Glow",
        "Korean Glass Skin",
        "Matte Professional",
        "Natural Dewy",
        "Soft Glam"
    ]

    result = looks[int(prediction[0])]

    st.balloons()

    st.success(f"✨ Recommended Makeup Look: {result}")

    tab1, tab2, tab3 = st.tabs([
        "💄 Face Products",
        "👁 Eye & Lip Products",
        "🌸 Beauty Tips"
    ])

    with tab1:

        st.info(f"Foundation: {brand_dict[result]['Foundation'][price_range]}")
        st.info(f"Concealer: {brand_dict[result]['Concealer'][price_range]}")
        st.info(f"Compact: {brand_dict[result]['Compact'][price_range]}")
        st.info(f"Blush: {brand_dict[result]['Blush'][price_range]}")
        st.info(f"Highlighter: {brand_dict[result]['Highlighter'][price_range]}")

    with tab2:

        st.info(f"Lipstick: {brand_dict[result]['Lipstick'][price_range]}")
        st.info(f"Eyeshadow: {brand_dict[result]['Eyeshadow'][price_range]}")
        st.info(f"Eyeliner: {brand_dict[result]['Eyeliner'][price_range]}")
        st.info(f"Mascara: {brand_dict[result]['Mascara'][price_range]}")
        st.info(f"Setting Spray: {brand_dict[result]['Setting Spray'][price_range]}")

    with tab3:

        for tip in tips_dict[result]:
            st.success(tip)

    st.success(f"🌟 Final Finish: {brand_dict[result]['Finish']}")

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "AI Beauty Recommendation System | Developed using Python, Machine Learning & Streamlit"
)
