from tqdm import tqdm
import mysql.connector
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

# Read CSV
df = pd.read_csv('cleaned_titanic.csv')

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password=os.getenv('DB_PASSWORD'),
    database='titanic_db'
)
cursor = conn.cursor()

# Prepare insert statement
cols = ",".join(df.columns)
placeholders = ",".join(["%s"] * len(df.columns))
sql = f"INSERT INTO cleaned_titanic ({cols}) VALUES ({placeholders})"

# Insert rows with progress bar
for row in tqdm(df.values, desc="Uploading rows"):
    cursor.execute(sql, tuple(row))
conn.commit()
cursor.close()
conn.close()
