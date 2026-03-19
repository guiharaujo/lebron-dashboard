# LeBron James - Career Dashboard

Interactive dashboard visualizing LeBron James' complete NBA career using Python + Streamlit.

## Features

- **Career Stats**: PPG/RPG/APG per season with championship markers, team comparison, and raw data table
- **Championships**: Cards for all 4 titles (2012, 2013, 2016, 2020) with Finals MVP stats
- **Records**: Historical records including all-time NBA scoring leader

## Prerequisites

- Python 3.9+
- Internet connection (fetches data from stats.nba.com)

## Setup & Run

```bash
cd "C:\Users\guiha\OneDrive\Documentos\Projeto Claude"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Opens automatically at `http://localhost:8501`.

## Data Sources

- **Career statistics**: [nba_api](https://github.com/swar/nba_api) → stats.nba.com (endpoint: `PlayerCareerStats`, player ID 2544)
- **Championships & records**: Hard-coded in `data/constants.py`

## Project Structure

```
├── app.py                  # Streamlit entry point
├── requirements.txt
├── data/
│   ├── fetcher.py          # nba_api calls with cache + Windows headers
│   └── constants.py        # Static data: titles, records, team colors
└── components/
    ├── header.py           # Bio + career quick metrics
    ├── career_stats.py     # Season-by-season chart + table
    ├── championships.py    # Championship cards
    └── records.py          # Historical records
```
