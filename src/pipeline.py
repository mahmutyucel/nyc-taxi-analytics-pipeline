import sys, os, subprocess
sys.path.insert(0, os.path.dirname(__file__))
from ingest import download_taxi_data, get_latest_available_month
from transform import run_transform
def run():
    print("NYC Taxi Analytics Pipeline")
    ym = sys.argv[1] if len(sys.argv) > 1 else get_latest_available_month()
    p = download_taxi_data(ym); run_transform(p)
    subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "plot.py")], check=True)
    print("Boru hatti tamamlandi")
if __name__ == "__main__": run()
