import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from data.fetcher import get_career_stats
from data.constants import CHAMPIONSHIP_YEARS, TEAM_COLORS, TEAM_NAMES


def _build_team_comparison(df: pd.DataFrame) -> go.Figure:
    teams = df["TEAM_ABBREVIATION"].unique()
    fig = go.Figure()

    for team in teams:
        team_df = df[df["TEAM_ABBREVIATION"] == team]
        color = TEAM_COLORS.get(team, "#888888")
        name = TEAM_NAMES.get(team, team)

        fig.add_trace(
            go.Bar(
                name=name,
                x=["PPG", "RPG", "APG"],
                y=[
                    round(team_df["PPG"].mean(), 1),
                    round(team_df["RPG"].mean(), 1),
                    round(team_df["APG"].mean(), 1),
                ],
                marker_color=color,
                text=[
                    str(round(team_df["PPG"].mean(), 1)),
                    str(round(team_df["RPG"].mean(), 1)),
                    str(round(team_df["APG"].mean(), 1)),
                ],
                textposition="outside",
            )
        )

    fig.update_layout(
        title="Average Stats by Team (regular season)",
        barmode="group",
        plot_bgcolor="#0e1117",
        paper_bgcolor="#0e1117",
        font_color="#e0e0e0",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="#222"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
        margin=dict(t=60, b=40),
    )
    return fig


def render() -> None:
    st.subheader("Career Statistics")

    with st.spinner("Loading career stats..."):
        df = get_career_stats()

    tab_teams, tab_table = st.tabs(["🏀 By Team", "📋 All Seasons"])

    with tab_teams:
        st.plotly_chart(_build_team_comparison(df), use_container_width=True)

    with tab_table:
        display_cols = [
            "SEASON_ID", "TEAM_ABBREVIATION", "GP",
            "PTS", "PPG", "RPG", "APG", "SPG", "BPG",
            "FG_PCT", "FG3_PCT", "MPG",
        ]
        available = [c for c in display_cols if c in df.columns]
        table_df = df[available].rename(columns={
            "SEASON_ID": "Season",
            "TEAM_ABBREVIATION": "Team",
            "GP": "G",
            "PTS": "Total PTS",
            "FG_PCT": "FG%",
            "FG3_PCT": "3P%",
        })

        # Add trophy to championship seasons
        champ_season_labels = {
            f"{y - 1}-{str(y)[-2:]}" for y in CHAMPIONSHIP_YEARS
        }
        table_df["Season"] = table_df["Season"].apply(
            lambda s: f"🏆 {s}" if s in champ_season_labels else s
        )

        row_colors = [
            TEAM_COLORS.get(t, "#1a1a2e")
            for t in df["TEAM_ABBREVIATION"].values
        ]

        fig_table = go.Figure(data=[go.Table(
            header=dict(
                values=list(table_df.columns),
                fill_color="#FDB927",
                font=dict(color="black", size=13),
                align="center",
                height=32,
            ),
            cells=dict(
                values=[table_df[c] for c in table_df.columns],
                fill_color=[row_colors],
                font=dict(color="white", size=12),
                align="center",
                height=28,
            ),
        )])

        row_count = len(table_df)
        fig_table.update_layout(
            margin=dict(t=10, b=10, l=10, r=10),
            paper_bgcolor="#0e1117",
            height=32 + row_count * 28 + 40,
        )
        st.plotly_chart(fig_table, use_container_width=True)

    st.divider()
