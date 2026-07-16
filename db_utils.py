from sqlalchemy import create_engine
import pandas as pd

# Use 'db' as the hostname because Docker links the containers by service name
DB_URL = "postgresql://myuser:mypassword@db:5432/productivity_db"
engine = create_engine(DB_URL)

def get_from_db():
    query = "SELECT * FROM logs"
    return pd.read_sql(query, engine)