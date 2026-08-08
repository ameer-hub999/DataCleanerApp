import streamlit as st
import pandas as pd
import io

# 1. Page Configuration
st.set_page_config(
    page_title="Data Cleaner Pro", 
    page_icon="📊", 
    layout="centered"
)

# 2. Header Section
st.title("📊 Universal Data Cleaner & Auto-Formatter")
st.write("Upload your CSV or Excel files to clean missing values, remove duplicates, and export ready-to-use reports in seconds.")

# 3. File Uploader
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        # Load dataset
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
            
        st.subheader("👀 Raw Data Preview")
        st.dataframe(df.head())

        # Sidebar Controls
        st.sidebar.header("⚙️ Cleaning Options")
        drop_duplicates = st.sidebar.checkbox("Remove Duplicate Rows", value=True)
        fill_na = st.sidebar.checkbox("Fill Missing Values with 0", value=True)
        
        # Data Processing
        cleaned_df = df.copy()
        
        if drop_duplicates:
            cleaned_df = cleaned_df.drop_duplicates()
            
        if fill_na:
            cleaned_df = cleaned_df.fillna(0)

        # Processed Data Preview
        st.subheader("✅ Cleaned Data Preview")
        st.dataframe(cleaned_df.head())

        # Export Options
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            cleaned_df.to_excel(writer, index=False, sheet_name='CleanedData')
        
        st.download_button(
            label="📥 Download Cleaned Excel File",
            data=buffer.getvalue(),
            file_name="Cleaned_Data_Report.xlsx",
            mime="application/vnd.ms-excel"
        )
        st.success("File processed successfully!")

    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")