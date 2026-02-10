import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DB_SERVER = os.getenv("DATABRICKS_SERVER_HOSTNAME")
DB_HTTP_PATH = os.getenv("DATABRICKS_HTTP_PATH")
DB_TOKEN = os.getenv("DATABRICKS_ACCESS_TOKEN")

DB_CATALOG = os.getenv("DATABRICKS_CATALOG")
DB_SCHEMA = os.getenv("DATABRICKS_SCHEMA")
DB_TABLE = os.getenv("DATABRICKS_TABLE")
