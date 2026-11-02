import duckdb

query = """
SELECT
    hour(tpep_pickup_datetime) AS hour,
    COUNT(*) AS trips,
    ROUND(AVG(duration_min), 1) AS avg_duration_min
FROM 'data/clean.parquet'
GROUP BY hour
ORDER BY trips DESC
"""

print(duckdb.sql(query).show(max_rows=24))