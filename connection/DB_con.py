import sys
from pathlib import Path
import psycopg
sys.path.append(str(Path(__file__).parent.parent))
from setting import DB_PASSWORD

conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="postgres",
    password=DB_PASSWORD
)

cur = conn.cursor()

cur.execute("SELECT version();")

print(cur.fetchone())

cur.close()
conn.close()