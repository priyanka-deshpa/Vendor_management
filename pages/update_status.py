import streamlit as st
from database import get_all_vendors, update_vendor_status
import pandas as pd

def render_update_status_page():
    st.title("Update Vendor Status")
    
    vendors = get_all_vendors()
    
    if not vendors:
        st.info("No vendors found.")
        return
    
    df = pd.DataFrame(
        vendors,
        columns=['Vendor ID', 'Vendor Name', 'Category', 
                 'Years in Business', 'Contact', 'Status']
    )
    
    vendor_id = st.selectbox(
        "Select Vendor",
        options=df['Vendor ID'].tolist(),
        format_func=lambda x: f"{x} - {df[df['Vendor ID'] == x]['Vendor Name'].iloc[0]}"
    )
    
    new_status = st.selectbox(
        "New Status",
        options=["Active", "Inactive"]
    )
    
    if st.button("Update Status"):
        try:
            if update_vendor_status(vendor_id, new_status):
                st.success("Vendor status updated successfully!")
            else:
                st.error("Failed to update vendor status")
        except Exception as e:
            st.error(f"Error updating status: {str(e)}")