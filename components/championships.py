import streamlit as st
from data.constants import CHAMPIONSHIPS


def render() -> None:
    st.subheader("Championships")

    cols = st.columns(4)

    for col, champ in zip(cols, CHAMPIONSHIPS):
        border_color = "#FDB927"
        with col:
            st.markdown(
                f"""
                <div style="
                    border: 2px solid {border_color};
                    border-radius: 10px;
                    padding: 16px 12px;
                    background: linear-gradient(145deg, #1a1a2e, #16213e);
                    text-align: center;
                    height: 100%;
                ">
                    <div style="font-size: 2.5rem">{champ['icon']}</div>
                    <div style="
                        color: {border_color};
                        font-size: 1.6rem;
                        font-weight: 700;
                        margin: 4px 0;
                    ">{champ['year']}</div>
                    <div style="
                        color: white;
                        font-size: 0.95rem;
                        font-weight: 600;
                        margin-bottom: 6px;
                    ">{champ['team']}</div>
                    <div style="color: #aaa; font-size: 0.8rem; margin-bottom: 10px;">
                        vs {champ['opponent']}<br>
                        Series: <strong style="color:white">{champ['series']}</strong>
                    </div>
                    <div style="
                        background: rgba(253,185,39,0.1);
                        border-radius: 6px;
                        padding: 6px;
                        font-size: 0.8rem;
                        color: #e0e0e0;
                    ">
                        <span style="color:{border_color}">Finals MVP</span><br>
                        {champ['ppg']} PPG &nbsp;
                        {champ['rpg']} RPG &nbsp;
                        {champ['apg']} APG
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.divider()
