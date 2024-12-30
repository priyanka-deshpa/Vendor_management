import streamlit as st
from database import get_all_vendors
import pandas as pd

def render_home_page():
    st.title("Vendor Management System")
    st.write("Welcome to the Vendor Management System. Use the sidebar to navigate.")