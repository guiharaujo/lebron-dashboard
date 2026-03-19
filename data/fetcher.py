import pandas as pd
import streamlit as st
from data.constants import LEBRON_ID

# Windows requires custom headers for nba_api to work
_HEADERS = {
    "Host": "stats.nba.com",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/123.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "x-nba-stats-origin": "stats",
    "x-nba-stats-token": "true",
    "Connection": "keep-alive",
    "Referer": "https://www.nba.com/",
    "Origin": "https://www.nba.com",
}

_FALLBACK_DATA = {
    "SEASON_ID": [
        "2003-04", "2004-05", "2005-06", "2006-07", "2007-08",
        "2008-09", "2009-10", "2010-11", "2011-12", "2012-13",
        "2013-14", "2014-15", "2015-16", "2016-17", "2017-18",
        "2018-19", "2019-20", "2020-21", "2021-22", "2022-23",
        "2023-24", "2024-25",
    ],
    "TEAM_ABBREVIATION": [
        "CLE", "CLE", "CLE", "CLE", "CLE",
        "CLE", "CLE", "MIA", "MIA", "MIA",
        "MIA", "CLE", "CLE", "CLE", "CLE",
        "LAL", "LAL", "LAL", "LAL", "LAL",
        "LAL", "LAL",
    ],
    "GP": [
        79, 80, 79, 78, 75,
        81, 76, 79, 62, 76,
        77, 69, 76, 74, 82,
        55, 67, 45, 56, 55,
        71, 60,
    ],
    "PTS": [
        1654, 2175, 2478, 2132, 2250,
        2304, 2258, 2111, 1683, 2036,
        2089, 1743, 1920, 1954, 2251,
        1505, 1839, 1216, 1695, 1590,
        1874, 1530,
    ],
    "REB": [
        588, 588, 556, 526, 617,
        613, 554, 599, 492, 610,
        554, 507, 567, 591, 645,
        453, 499, 365, 461, 417,
        561, 450,
    ],
    "AST": [
        465, 577, 521, 470, 539,
        587, 651, 554, 387, 551,
        507, 511, 514, 646, 747,
        516, 684, 347, 470, 430,
        591, 400,
    ],
    "STL": [
        130, 177, 123, 138, 138,
        146, 132, 109, 90, 129,
        109, 109, 104, 116, 116,
        101, 90, 60, 72, 72,
        78, 55,
    ],
    "BLK": [
        58, 52, 66, 55, 81,
        93, 75, 62, 54, 64,
        52, 49, 52, 53, 59,
        40, 46, 28, 35, 33,
        48, 40,
    ],
    "FG_PCT": [
        0.417, 0.472, 0.480, 0.476, 0.484,
        0.489, 0.503, 0.510, 0.531, 0.565,
        0.567, 0.488, 0.520, 0.548, 0.542,
        0.510, 0.493, 0.513, 0.524, 0.500,
        0.540, 0.521,
    ],
    "FG3_PCT": [
        0.290, 0.351, 0.335, 0.319, 0.315,
        0.344, 0.333, 0.330, 0.362, 0.406,
        0.341, 0.354, 0.309, 0.363, 0.367,
        0.348, 0.348, 0.365, 0.359, 0.323,
        0.410, 0.388,
    ],
    "MIN": [
        3122, 3388, 3361, 3190, 3054,
        3054, 2966, 3063, 2326, 2877,
        2902, 2493, 2709, 2794, 3025,
        1777, 2316, 1365, 1756, 1634,
        2311, 1850,
    ],
}


def _compute_per_game(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["PPG"] = (df["PTS"] / df["GP"]).round(1)
    df["RPG"] = (df["REB"] / df["GP"]).round(1)
    df["APG"] = (df["AST"] / df["GP"]).round(1)
    df["SPG"] = (df["STL"] / df["GP"]).round(1)
    df["BPG"] = (df["BLK"] / df["GP"]).round(1)
    df["MPG"] = (df["MIN"] / df["GP"]).round(1)
    return df


@st.cache_data(ttl=3600, show_spinner=False)
def get_career_stats() -> pd.DataFrame:
    try:
        from nba_api.stats.endpoints import playercareerstats
        from nba_api.stats.library.http import NBAStatsHTTP

        NBAStatsHTTP.HEADERS = _HEADERS

        raw = playercareerstats.PlayerCareerStats(
            player_id=LEBRON_ID,
            timeout=30,
        ).get_data_frames()[0]

        # Keep only regular season rows (exclude TOT rows when traded)
        df = raw[raw["TEAM_ABBREVIATION"] != "TOT"].copy()

        # Normalise season label: nba_api returns "2003-04" style already
        df = df.rename(columns={"SEASON_ID": "SEASON_ID"})

        return _compute_per_game(df)

    except Exception:
        df = pd.DataFrame(_FALLBACK_DATA)
        return _compute_per_game(df)


@st.cache_data(ttl=3600, show_spinner=False)
def get_career_totals() -> dict:
    df = get_career_stats()
    return {
        "total_points": int(df["PTS"].sum()),
        "total_games": int(df["GP"].sum()),
        "total_seasons": len(df),
        "career_ppg": round(df["PTS"].sum() / df["GP"].sum(), 1),
        "career_rpg": round(df["REB"].sum() / df["GP"].sum(), 1),
        "career_apg": round(df["AST"].sum() / df["GP"].sum(), 1),
    }
