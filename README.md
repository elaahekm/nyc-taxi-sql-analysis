# NYC Taxi Trips: SQL Analysis (January 2015)

An exploratory analysis of 12.6 million NYC yellow taxi trips using SQL (DuckDB) on parquet files, answering a few simple business questions.

## Data

- Source: NYC TLC Trip Record Data, Yellow Taxi, January 2015 (`yellow_tripdata_2015-01.parquet`).
- Taxi zone names: `taxi_zone_lookup.csv` from the NYC TLC website.
- `clean.py` keeps only January 2015 pickups with trip durations between 1 and 180 minutes: 12,741,035 raw trips become 12,630,986.
- The data files are not included in this repository. Put them in `data/`.

## Questions and findings

**1. Which hours are busiest?** (`q1_busy_hours.py`)
Hours 19, 18 and 20 are the busiest, with roughly 730,000 to 800,000 trips each over the month. The quietest hours are 3 to 5 AM. Busy hours are not the slowest trips: average duration is highest around 2-3 PM (13.4 to 13.6 min).

**2. Which routes are most popular?** (`q3_top_routes_named.py`)
After removing unknown zones, the top routes are short trips inside or between neighbouring Manhattan neighbourhoods, mostly on the Upper East Side and Upper West Side. The top route, Upper East Side South to Upper East Side North, has 59,206 trips averaging 6 minutes.

**3. Weekend vs weekday?** (`q4_weekend.py`)
Excluding the two storm days, weekends have about 436,000 trips per day against about 417,000 on weekdays, and weekend trips are shorter (11.5 vs 12.8 minutes on average).

**4. What happened on January 26-27?** (`q5_daily.py`, `q6_chart.py`)
Daily