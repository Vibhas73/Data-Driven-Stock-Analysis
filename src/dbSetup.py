# db_setup.py
import os
import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
from datetime import datetime

# --- CONFIGURATION ---
# IMPORTANT: Replace these with your actual MySQL credentials
DB_CONFIG = {
    'user': 'root', 
    'password': 'root',
    'host': 'localhost',
    'database': 'stock_analysis_db' # Ensure this database is created manually first
}

def connect_db():
    """Establishes and returns a database connection."""
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as err:
        print(f"Database Connection Error: {err}")
        return None

def create_connection():
    """Creates connection and ensures the database exists."""
    try:
        # Initial connection without specifying the database
        conn = mysql.connector.connect(
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            host=DB_CONFIG['host']
        )
        cursor = conn.cursor()
        
        # Create database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
        
        # Now switch to using that database
        conn.database = DB_CONFIG['database']
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def load_initial_data(csv_folder_path):
    """Reads initial data from CSV and loads it into the query_log table."""
    engine = create_engine(f"mysql+mysqlconnector://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['database']}")

    all_files = [f for f in os.listdir(csv_folder_path) if f.endswith('.csv')]
        
    if not all_files:
        print("No CSV files found to upload.")
        return

    print(f"Uploading {len(all_files)} files to database...")
    
    try:
        for file in all_files:
            file_path = os.path.join(csv_folder_path, file)
            df = pd.read_csv(file_path)
            if 'date' in df.columns:
                df['date'] = pd.to_datetime(df['date'])
            try:
                df.to_sql('stock_data', con=engine, if_exists='append', index=False, chunksize=1000)
                print(f"Uploaded {file}")
            except Exception as e:
                print(f"Failed to upload {file}: {e}")
        
        print("Database upload complete.")

    except Exception as e:
        print(f"An unexpected error occurred during data loading: {e}")

def get_data():
    """Fetch data using SQL query"""
    query = "SELECT * FROM stock_data"
    conn = connect_db()
    if not conn: return None
    
    cursor = conn.cursor(dictionary=True) # Return results as dictionaries
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        print(f"Database Fetch Error: {err}")
        return None
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    # 1. Create a connection
    conn = create_connection()
    if conn:
        # 2. Load initial data
        load_initial_data("../data_processed")
        
        conn.close()
        print("Database setup complete.")