import os, sys, requests
from datetime import datetime, timedelta
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)
def get_latest_available_month():
    return (datetime.today() - timedelta(days=90)).strftime("%Y-%m")
def download_taxi_data(year_month=None):
    if year_month is None: year_month = get_latest_available_month()
    year, month = year_month.split("-")
    url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month}.parquet"
    local_path = os.path.join(DATA_DIR, f"yellow_tripdata_{year}-{month}.parquet")
    if os.path.exists(local_path):
        print(f"Veri zaten mevcut: {local_path}"); return local_path
    print(f"Indiriliyor: {url}")
    r = requests.get(url, stream=True, timeout=180); r.raise_for_status()
    with open(local_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192): f.write(chunk)
    print(f"Indirme tamam: {local_path}"); return local_path
if __name__ == "__main__":
    download_taxi_data(sys.argv[1] if len(sys.argv) > 1 else None)
