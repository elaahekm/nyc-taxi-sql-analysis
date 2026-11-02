import duckdb

query = """
SELECT
    t.PULocationID AS pickup_zone,
    t.DOLocationID AS dropoff_zone,
    COUNT(*) AS trips,
    ROUND(AVG(t.duration_min), 1) AS avg_duration_min
FROM 'data/clean.parquet' t
GROUP BY pickup_zone, dropoff_zone
ORDER BY trips DESC
LIMIT 10
"""

duckdb.sql(query).show()