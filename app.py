import streamlit as st
from database import init_db
from pages.home import render_home_page
from pages.add_vendor import render_add_vendor_page
from pages.upload_vendors import render_upload_vendors_page
from pages.view_vendors import render_view_vendors_page
from pages.update_status import render_update_status_page

def main():
    st.set_page_config(
        page_title="Vendor Management System",
        page_icon="🏢",
        layout="wide"
    )
    
    # Initialize database
    init_db()
    
    # Sidebar navigation
    page = st.sidebar.selectbox(
        "Navigation",
        ["Home", "View Vendors", "Add Vendor", "Upload Vendors", "Update Status"]
    )
    
    # Render selected page
    if page == "Home":
        render_home_page()
    elif page == "Add Vendor":
        render_add_vendor_page()
    elif page == "Upload Vendors":
        render_upload_vendors_page()
    elif page == "View Vendors":
        render_view_vendors_page()
    elif page == "Update Status":
        render_update_status_page()

if __name__ == "__main__":
    main()