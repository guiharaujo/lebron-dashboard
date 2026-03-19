import streamlit as st
from data.fetcher import get_career_totals


def render() -> None:
    totals = get_career_totals()

    col_img, col_bio = st.columns([1, 3])

    with col_img:
        st.image(
            "https://cdn.nba.com/headshots/nba/latest/1040x760/2544.png",
            width=220,
        )

    with col_bio:
        st.markdown(
            "<h1 style='margin-bottom:4px'>LeBron James</h1>"
            "<p style='color:#FDB927; font-size:1.1rem; margin-top:0'>"
            "Small Forward / Power Forward &nbsp;·&nbsp; #23 &nbsp;·&nbsp; Los Angeles Lakers"
            "</p>"
            "<p style='color:#aaa; font-size:0.95rem'>"
            "Born: December 30, 1984 &nbsp;·&nbsp; Akron, Ohio &nbsp;·&nbsp; "
            "Draft: 2003, Round 1, Pick 1 (Cleveland Cavaliers)"
            "</p>",
            unsafe_allow_html=True,
        )

        m1, m2, m3, m4, m5 = st.columns(5)
        m1.metric("Career Points", f"{totals['total_points']:,}")
        m2.metric("Games Played", f"{totals['total_games']:,}")
        m3.metric("Seasons", totals["total_seasons"])
        m4.metric("Career PPG", totals["career_ppg"])
        m5.metric("Career APG", totals["career_apg"])

    st.divider()
