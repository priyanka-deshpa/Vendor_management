import pandas as pd

def read_excel_file(file):
    """Read an Excel file and return a pandas DataFrame."""
    try:
        df = pd.read_excel(file)
        # Convert column names to lowercase
        df.columns = df.columns.str.lower()
        return df
    except Exception as e:
        raise Exception(f"Error reading Excel file: {str(e)}")

def validate_excel_data(df):
    """Validate the Excel data for required columns and empty values."""
    required_columns = ['vendor_id', 'vendor_name', 'category', 
                       'years_in_business', 'contact', 'status']
    
    # Check if all required columns exist
    if not all(col in df.columns for col in required_columns):
        return False, "Missing required columns"
    
    # Check for empty values
    if df[required_columns].isnull().values.any():
        return False, "Excel file contains empty values"
    
    return True, "Data is valid"