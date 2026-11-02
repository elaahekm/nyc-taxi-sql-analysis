import duckdb

query = """
SELECT
    CAST(tpep_pickup_datetime AS DATE) AS day,
    dayname(tpep_pickup_datetime) AS weekday_name,
    COUNT(*) AS trips
FROM 'data/clean.parquet'
GROUP BY day, weekday_name
ORDER BY day
"""

duckdb.sql(query).show(max_rows=31)