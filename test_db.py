from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:2208@localhost:5432/fastapi_db"
)

try:
    conn = engine.connect()
    print("✅ DB CONNECTED")
    conn.close()
except Exception as e:
    print("❌ ERROR:", e)

    print ("venkat")