from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:AvilaIT@localhost:5432/postgres")

try:
    conn = engine.connect()
    print("Connected successfully")
    conn.close()
except Exception as e:
    print("Connection failed:", e)