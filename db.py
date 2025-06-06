import psycopg2
import os

class Database:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host="db",
            port=5432
        )

    def init_db(self):
        if not self.conn:
            self.connect()
        cur = self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS visits (id SERIAL PRIMARY KEY);")
        self.conn.commit()
        cur.close()
        self.conn.close()
        self.conn = None

# Singleton instance
db = Database()
