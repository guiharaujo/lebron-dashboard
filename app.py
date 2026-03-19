import streamlit as st

st.set_page_config(
    page_title="LeBron James - Career Dashboard",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Minimal global CSS: dark background, gold/purple accents
st.markdown(
    """
    <style>
        body, .stApp {
            background-color: #0e1117;
            color: #e0e0e0;
        }
        h1, h2, h3 {
            color: #FDB927;
        }
        [data-testid="metric-container"] {
            background: #1a1a2e;
            border: 1px solid #333;
            border-radius: 8px;
            padding: 12px 16px;
        }
        [data-testid="stMetricValue"] {
            color: #FDB927;
            font-weight: 700;
        }
        div[data-testid="stExpander"] {
            border: 1px solid #333;
            border-radius: 8px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

from components import header, career_stats, championships, records

header.render()
career_stats.render()
championships.render()
records.render()

st.markdown(
    "<p style='text-align:center; color:#555; font-size:0.8rem; margin-top:2rem'>"
    "Data sourced from stats.nba.com via nba_api · Dashboard built with Streamlit & Plotly"
    "</p>",
    unsafe_allow_html=True,
)
