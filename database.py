import sqlite3
from contextlib import contextmanager
from typing import List
from pydantic import ValidationError
import pandas as pd
from models import Vendor


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

def add_vendor(vendor_data: dict):
    try:
        # Validate data using the Pydantic model
        vendor = Vendor(**vendor_data)
    except ValidationError as e:
        print("Validation error:", e)
        return

    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO vendors (vendor_id, vendor_name, category, years_in_business, 
                               contact, status)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            vendor.vendor_id,
            vendor.vendor_name,
            vendor.category,
            vendor.years_in_business,
            vendor.contact,
            vendor.status
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

def bulk_insert_vendors(df: pd.DataFrame):
    # Validate all rows using Pydantic
    try:
        vendors = [Vendor(**row) for _, row in df.iterrows()]
    except ValidationError as e:
        print("Validation error during bulk insert:", e)
        return

    with get_db_connection() as conn:
        for vendor in vendors:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO vendors (vendor_id, vendor_name, category, 
                                   years_in_business, contact, status)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                vendor.vendor_id,
                vendor.vendor_name,
                vendor.category,
                vendor.years_in_business,
                vendor.contact,
                vendor.status
            ))
        conn.commit()