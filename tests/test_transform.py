import os, duckdb
def test_duckdb(): assert duckdb.connect().execute("SELECT 1").fetchone()[0] == 1
def test_dir():
    d = os.path.join(os.path.dirname(__file__), "..", "output")
    os.makedirs(d, exist_ok=True); assert os.path.isdir(d)
