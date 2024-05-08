import os

DB_HOST = os.environ.get("DB_HOST", "")
DB_PORT = os.environ.get("DB_PORT", "")
DB_USER = os.environ.get("DB_USER", "")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
DB_NAME = os.environ.get("DB_NAME", "")

DB_CONNECTION_URL = f"jdbc:mysql://{DB_USER}:{DB_PASSWORD}@{DB_PORT}/{DB_NAME}/"
