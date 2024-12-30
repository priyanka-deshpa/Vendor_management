import streamlit as st
import pandas as pd
from database import get_all_vendors

def render_view_vendors_page():
    st.title("View Vendors")
    
    vendors = get_all_vendors()
    
    if vendors:
        df = pd.DataFrame(
            vendors,
            columns=['Vendor ID', 'Vendor Name', 'Category', 
                     'Years in Business', 'Contact', 'Status']
        )
        
        # Add filters
        st.subheader("Filters")
        col1, col2 = st.columns(2)
        with col1:
            status_filter = st.multiselect(
                "Filter by Status",
                options=df['Status'].unique()
            )
        with col2:
            category_filter = st.multiselect(
                "Filter by Category",
                options=df['Category'].unique()
            )
        
        # Apply filters
        filtered_df = df
        if status_filter:
            filtered_df = filtered_df[filtered_df['Status'].isin(status_filter)]
        if category_filter:
            filtered_df = filtered_df[filtered_df['Category'].isin(category_filter)]
        
        st.dataframe(filtered_df)
    else:
        st.info("No vendors found. Add some vendors to get started!")