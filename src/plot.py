import os, duckdb, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
O = os.path.join(os.path.dirname(__file__), "..", "output")
con = duckdb.connect()
rows = con.execute(f"SELECT pickup_hour, avg_tip_pct FROM read_parquet('{O}/hourly_tip.parquet') ORDER BY pickup_hour").fetchall()
h = [r[0] for r in rows]; p = [r[1] for r in rows]
plt.figure(figsize=(10,5)); plt.plot(h, p, marker="o")
plt.title("NYC Taxi - Saatlik Ortalama Bahsis Orani (%)"); plt.xlabel("Saat"); plt.ylabel("Bahsis %"); plt.grid(True, alpha=0.3)
out = os.path.join(O, "hourly_tip.png"); plt.savefig(out, dpi=120, bbox_inches="tight"); print("Grafik:", out)
