
from sqlalchemy import create_engine

def create_db_and_engine(user, password, host="localhost", port=5432, db_name="sales_db"):
    # Connect to base default 'postgres'
    engine_default = create_engine("postgresql+psycopg2://postgres:dlasoidIND0034fj@localhost:5432/postgres")

    # Create new database
    engine_default = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/postgres")
    engine_default.execute("COMMIT")
    engine_default.execute(f"CREATE DATABASE {db_name}")  # create DB
    engine_default.dispose()  # cerrar conexión

    # Connect to new database
    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}")
    
    return engine