import streamlit as st
import pandas as pd
from database import bulk_insert_vendors
from utils.excel_handler import read_excel_file, validate_excel_data

def render_upload_vendors_page():
    st.title("Upload Vendor Data")
    
    st.write("Upload an Excel file containing vendor data")
    
    # Show example format
    st.subheader("Required Excel Format")
    example_df = pd.DataFrame({
        'vendor_id': ['V001'],
        'vendor_name': ['Example Vendor'],
        'category': ['Technology'],
        'years_in_business': [5],
        'contact': ['contact@example.com'],
        'status': ['Active']
    })
    st.dataframe(example_df)
    
    uploaded_file = st.file_uploader("Choose an Excel file", type=['xlsx', 'xls'])
    
    if uploaded_file is not None:
        try:
            df = read_excel_file(uploaded_file)
            is_valid, message = validate_excel_data(df)
            
            if not is_valid:
                st.error(message)
                return
            
            st.write("Preview of uploaded data:")
            st.dataframe(df)
            
            if st.button("Import Vendors"):
                try:
                    bulk_insert_vendors(df)
                    st.success(f"Successfully imported {len(df)} vendors!")
                except Exception as e:
                    st.error(f"Error importing vendors: {str(e)}")
        except Exception as e:
            st.error(f"Error reading file: {str(e)}")