# NYC Taxi Analytics Pipeline

[![Monthly Pipeline](https://github.com/mahmutyucel/nyc-taxi-analytics-pipeline/actions/workflows/pipeline.yml/badge.svg)](https://github.com/mahmutyucel/nyc-taxi-analytics-pipeline/actions/workflows/pipeline.yml)

> NYC TLC'nin resmi açık verisi üzerinde çalışan, aylık otomatik tetiklenen uçtan uca veri mühendisliği boru hattı. Python + DuckDB + Parquet + GitHub Actions.

## Mimari

```text
GitHub Actions (aylik cron)
    |
    v
src/pipeline.py  -->  ingest.py    -> TLC CDN'den en son ayin Parquet'i indirir
    |
    +-->  transform.py  -> DuckDB ile temizler, saatlik bahsis istatistigi
    |
    +-->  plot.py       -> matplotlib ile grafik uretir
                                  |
                                  v
                       output/hourly_tip.png
                       (repoya otomatik commit edilir)
