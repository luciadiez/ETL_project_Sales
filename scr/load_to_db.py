

from main_script import clean_sales_data
from db_connection import create_db_and_engine
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# Clean data using main_script.py
df_clean = clean_sales_data()

# Connect to Postgres
engine = create_db_and_engine(user=user, password=password, host=host, port=port, db_name=db_name)

# Upload to Postgres, replaces if already exists
df_clean.to_sql('sales', engine, if_exists='replace', index=False)

print("Data correctly uploaded to Postgres")