
from sqlalchemy import create_engine,text

def create_db_and_engine(user, password, host, port, db_name):
    # Connect to default database 'postgres'
    engine_default = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/postgres")

    # Create new database
    with engine_default.connect() as conn:
        conn.execute(text("COMMIT"))  
        
        # Check if database already exists
        result = conn.execute(
            text("SELECT 1 FROM pg_database WHERE datname = :db"),
            {"db": db_name}
        )
        exists = result.scalar() is not None

        if not exists:
            conn.execute(text(f'CREATE DATABASE "{db_name}"'))
    
    engine_default.dispose() #close connection


    # Connect to new database
    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}")
    
    return engine