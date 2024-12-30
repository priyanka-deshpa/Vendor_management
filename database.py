import sqlite3
from contextlib import contextmanager
import pandas as pd

def init_db():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vendors (
                vendor_id TEXT PRIMARY KEY,
                vendor_name TEXT NOT NULL,
                category TEXT NOT NULL,
                years_in_business INTEGER NOT NULL,
                contact TEXT NOT NULL,
                status TEXT NOT NULL
            )
        ''')
        conn.commit()

@contextmanager
def get_db_connection():
    conn = sqlite3.connect('vendors.db')
    try:
        yield conn
    finally:
        conn.close()

def add_vendor(vendor_data):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO vendors (vendor_id, vendor_name, category, years_in_business, 
                               contact, status)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            vendor_data['vendor_id'],
            vendor_data['vendor_name'],
            vendor_data['category'],
            vendor_data['years_in_business'],
            vendor_data['contact'],
            vendor_data['status']
        ))
        conn.commit()

def get_all_vendors():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM vendors')
        vendors = cursor.fetchall()
        return vendors

def update_vendor_status(vendor_id, new_status):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE vendors 
            SET status = ? 
            WHERE vendor_id = ?
        ''', (new_status, vendor_id))
        conn.commit()
        return cursor.rowcount > 0

def bulk_insert_vendors(df):
    with get_db_connection() as conn:
        for _, row in df.iterrows():
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO vendors (vendor_id, vendor_name, category, 
                                   years_in_business, contact, status)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                row['vendor_id'],
                row['vendor_name'],
                row['category'],
                row['years_in_business'],
                row['contact'],
                row['status']
            ))
        conn.commit()