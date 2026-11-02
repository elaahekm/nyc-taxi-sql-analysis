import duckdb

query = """
SELECT
    CASE WHEN dayofweek(tpep_pickup_datetime) IN (0, 6) THEN 'weekend' ELSE 'weekday' END AS day_type,
    COUNT(*) AS trips,
    ROUND(AVG(duration_min), 1) AS avg_duration_min,
    COUNT(DISTINCT CAST(tpep_pickup_datetime AS DATE)) AS days,
    ROUND(COUNT(*) * 1.0 / COUNT(DISTINCT CAST(tpep_pickup_datetime AS DATE)), 0) AS trips_per_day
FROM 'data/clean.parquet'
WHERE CAST(tpep_pickup_datetime AS DATE) NOT IN ('2015-01-26', '2015-01-27')
GROUP BY day_type
"""

duckdb.sql(query).show()