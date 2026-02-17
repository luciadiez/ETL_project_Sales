

from main_script import clean_sales_data
from db_connection import create_db_and_engine

# Clean data using main_script.py
df_clean = clean_sales_data()

# Connect to Postgres
engine = create_db_and_engine(user="postgres", password="mypassword")

# Upload to Postgres, replaces if already exists
df_clean.to_sql('sales', engine, if_exists='replace', index=False)

print("Data correctly uploaded to Postgres")