import duckdb

query = """
SELECT
    COUNT(*) AS total_trips,
    MIN(tpep_pickup_datetime) AS first_pickup,
    MAX(tpep_pickup_datetime) AS last_pickup,
    ROUND(AVG(duration_min), 2) AS avg_duration_min
FROM 'data/clean.parquet'
"""

print(duckdb.sql(query))