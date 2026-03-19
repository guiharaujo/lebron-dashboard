LEBRON_ID = 2544

CHAMPIONSHIPS = [
    {
        "year": 2012,
        "team": "Miami Heat",
        "opponent": "OKC Thunder",
        "series": "4-1",
        "ppg": 28.6,
        "rpg": 10.2,
        "apg": 7.4,
        "color": "#98002E",
        "icon": "🔥",
    },
    {
        "year": 2013,
        "team": "Miami Heat",
        "opponent": "San Antonio Spurs",
        "series": "4-3",
        "ppg": 25.3,
        "rpg": 10.9,
        "apg": 7.0,
        "color": "#98002E",
        "icon": "🔥",
    },
    {
        "year": 2016,
        "team": "Cleveland Cavaliers",
        "opponent": "Golden State Warriors",
        "series": "4-3",
        "ppg": 29.7,
        "rpg": 11.3,
        "apg": 8.9,
        "color": "#860038",
        "icon": "⚡",
    },
    {
        "year": 2020,
        "team": "Los Angeles Lakers",
        "opponent": "Miami Heat",
        "series": "4-2",
        "ppg": 29.8,
        "rpg": 11.8,
        "apg": 8.5,
        "color": "#552583",
        "icon": "👑",
    },
]

CHAMPIONSHIP_YEARS = [c["year"] for c in CHAMPIONSHIPS]

RECORDS = [
    {
        "title": "NBA All-Time Scoring Leader",
        "value": "40,828+ points",
        "detail": "Surpassed Kareem Abdul-Jabbar on February 7, 2023 in Sacramento. Still active and adding to the record.",
        "highlight": True,
        "icon": "🏆",
    },
    {
        "title": "All-Time Playoffs Scoring Leader",
        "value": "8,000+ playoff points",
        "detail": "Most points scored in NBA playoff history, surpassing Michael Jordan's previous record.",
        "highlight": False,
        "icon": "🥇",
    },
    {
        "title": "Consecutive 27+ PPG Seasons",
        "value": "13 consecutive seasons",
        "detail": "Scored 27 or more points per game in 13 consecutive seasons (2005-06 through 2017-18), an NBA record.",
        "highlight": False,
        "icon": "📈",
    },
    {
        "title": "Finals MVP Awards",
        "value": "4 Finals MVPs",
        "detail": "Won Finals MVP in 2012, 2013, 2016, and 2020 — one with each of his three franchises.",
        "highlight": False,
        "icon": "🌟",
    },
    {
        "title": "All-NBA First Team Selections",
        "value": "13x All-NBA First Team",
        "detail": "Most All-NBA First Team selections in history, surpassing Kareem Abdul-Jabbar's record of 10.",
        "highlight": False,
        "icon": "🏅",
    },
]

TEAM_COLORS = {
    "CLE": "#860038",
    "MIA": "#98002E",
    "LAL": "#552583",
}

TEAM_SECONDARY_COLORS = {
    "CLE": "#FDBB30",
    "MIA": "#F9A01B",
    "LAL": "#FDB927",
}

TEAM_NAMES = {
    "CLE": "Cleveland Cavaliers",
    "MIA": "Miami Heat",
    "LAL": "Los Angeles Lakers",
}

STAT_COLORS = {
    "PPG": "#FDB927",
    "RPG": "#17408B",
    "APG": "#C9082A",
}
