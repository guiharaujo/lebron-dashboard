# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

LeBron James Career Dashboard — a Streamlit web application that displays career statistics, championships, and NBA records using live data from the NBA API with hardcoded fallback data.

## Running the App

```bash
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
streamlit run app.py           # Launches at http://localhost:8501
```

Requires Python 3.9+ and internet access for live NBA stats (falls back to hardcoded data if offline).

## Architecture

```
app.py                  # Entry point — configures page, applies CSS, renders all components
data/
  fetcher.py            # NBA API integration with 1-hour Streamlit cache and fallback data
  constants.py          # Static data: LEBRON_ID, CHAMPIONSHIPS, RECORDS, TEAM_COLORS
components/
  header.py             # Bio, photo, and career totals (Points, Games, PPG, APG)
  career_stats.py       # Team comparison Plotly charts and season-by-season table
  championships.py      # Championship cards for 2012, 2013, 2016, 2020
  records.py            # NBA records display
```

**Data flow:** `fetcher.py` fetches from `stats.nba.com` via `nba_api` (with Windows-specific HTTP headers to bypass API blocks), computes per-game stats, and returns DataFrames. Each component module exports a single `render()` function called by `app.py`.

**Caching:** `@st.cache_data(ttl=3600)` on all data fetchers. If the NBA API fails, `fetcher.py` automatically falls back to `_FALLBACK_DATA` — hardcoded stats for all 22 seasons (2003–2024).

## Key Constants

- `LEBRON_ID = 2544` — NBA player ID used in all API calls
- Team colors in `TEAM_COLORS`/`TEAM_SECONDARY_COLORS` drive visual theming per season
- Championship years (2012, 2013, 2016, 2020) are marked with 🏆 in the season table

## GitHub Repository

Repository: https://github.com/guiharaujo/lebron-dashboard

**Auto-sync:** A Claude Code hook (`PostToolUse` on `Edit|Write`) automatically commits and pushes every file change to GitHub. No manual git commands needed — every edit is synced automatically.

To manage the hook: open `/hooks` in Claude Code to view, edit, or disable it. The hook config lives in `.claude/settings.json`.

## Live App

URL: https://lebron-dashboard-oxu6odw5dzngyq3y8l9zjf.streamlit.app/

Hosted on Streamlit Community Cloud, connected to the `main` branch of the GitHub repo. Every push automatically redeploys the app.
