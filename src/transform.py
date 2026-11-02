import os, glob, duckdb
D = os.path.join(os.path.dirname(__file__), "..", "data")
O = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(O, exist_ok=True)
def run_transform(pf):
    con = duckdb.connect()
    con.execute(f"""COPY (SELECT tpep_pickup_datetime, tpep_dropoff_datetime, passenger_count, trip_distance, fare_amount, tip_amount, total_amount, payment_type, EXTRACT(hour FROM tpep_pickup_datetime) AS pickup_hour, EXTRACT(dow FROM tpep_pickup_datetime) AS pickup_dow FROM read_parquet('{pf}') WHERE fare_amount > 0 AND trip_distance > 0 AND trip_distance < 200 AND total_amount > 0) TO '{O}/cleaned_trips.parquet' (FORMAT PARQUET)""")
    con.execute(f"""COPY (SELECT pickup_hour, ROUND(AVG(tip_amount / NULLIF(fare_amount,0)) * 100, 2) AS avg_tip_pct, COUNT(*) AS trip_count FROM read_parquet('{O}/cleaned_trips.parquet') WHERE fare_amount > 0 GROUP BY pickup_hour ORDER BY pickup_hour) TO '{O}/hourly_tip.parquet' (FORMAT PARQUET)""")
    print("transform OK")
if __name__ == "__main__":
    files = glob.glob(os.path.join(D, "*.parquet"))
    if not files: raise FileNotFoundError("data/ bos")
    run_transform(max(files, key=os.path.getmtime))
