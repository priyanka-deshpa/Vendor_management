import streamlit as st
from database import add_vendor

def render_add_vendor_page():
    st.title("Add New Vendor")
    
    with st.form("add_vendor_form"):
        vendor_id = st.text_input("Vendor ID")
        vendor_name = st.text_input("Vendor Name")
        category = st.selectbox(
            "Category",
            ["Technology", "Services", "Manufacturing", "Retail", "Other"]
        )
        years_in_business = st.number_input(
            "Years in Business",
            min_value=0,
            max_value=200,
            value=0
        )
        contact = st.text_input("Contact Information")
        status = st.selectbox(
            "Status",
            ["active", "inactive"]
        )
        
        submit_button = st.form_submit_button("Add Vendor")
        
        if submit_button:
            if not all([vendor_id, vendor_name, category, years_in_business, contact, status]):
                st.error("Please fill in all fields")
                return
                
            vendor_data = {
                "vendor_id": vendor_id,
                "vendor_name": vendor_name,
                "category": category,
                "years_in_business": years_in_business,
                "contact": contact,
                "status": status
            }
            
            try:
                add_vendor(vendor_data)
                st.success("Vendor added successfully!")
            except Exception as e:
                st.error(f"Error adding vendor: {str(e)}")