from sqlalchemy import create_engine

# Update this URL with your actual DB credentials
DB_URL = "postgresql://myuser:mypassword@localhost:5432/productivity_db"
engine = create_engine(DB_URL)

def save_to_db(df):
    df.to_sql("logs", engine, if_exists="append", index=False)