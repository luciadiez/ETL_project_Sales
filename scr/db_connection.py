
from sqlalchemy import create_engine

def create_db_and_engine(user, password, host, port, db_name):
    # Connect to base default 'postgres'
    engine_default = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/postgres")

    # Create new database
    engine_default = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/postgres")
    engine_default.execute("COMMIT")
    engine_default.execute(f"CREATE DATABASE {db_name}")  # create DB
    engine_default.dispose()  # cerrar conexión

    # Connect to new database
    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}")
    
    return engine