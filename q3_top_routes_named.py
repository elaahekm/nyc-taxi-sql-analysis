import duckdb

query = """
SELECT
    p.Zone AS pickup,
    d.Zone AS dropoff,
    COUNT(*) AS trips,
    ROUND(AVG(t.duration_min), 1) AS avg_duration_min
FROM 'data/clean.parquet' t
JOIN 'data/taxi_zone_lookup.csv' p ON t.PULocationID = p.LocationID
JOIN 'data/taxi_zone_lookup.csv' d ON t.DOLocationID = d.LocationID
WHERE t.PULocationID NOT IN (264, 265)
  AND t.DOLocationID NOT IN (264, 265)
GROUP BY pickup, dropoff
ORDER BY trips DESC
LIMIT 10
"""

duckdb.sql(query).show(max_width=200)