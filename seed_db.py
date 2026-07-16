import pandas as pd
from db_utils import engine
import os

def seed_database():
    file_path = "sample_log.csv"
    
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found in {os.getcwd()}")
        return

    try:
        # Load the CSV
        df = pd.read_csv(file_path)
        print(f"Loaded {len(df)} rows from {file_path}")

        # Push to DB
        # 'replace' creates a clean slate for your dashboard
        df.to_sql("logs", engine, if_exists="replace", index=False)
        print("Database seeded successfully! You are ready to launch the app.")

    except Exception as e:
        print(f"An error occurred while seeding the database: {e}")
        print("Tip: Ensure your database container is running and accessible.")

if __name__ == "__main__":
    seed_database()