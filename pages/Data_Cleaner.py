import io
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Data Cleaner - Smart File AI", page_icon="📊", layout="wide")

st.title("📊 Data Cleaner")
st.write("Upload your Excel or CSV file to clean, deduplicate, and format your data instantly.")

uploaded_file = st.file_uploader("Upload Data File (.xlsx, .xls, .csv)", type=["xlsx", "xls", "csv"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success(f"File loaded successfully! Rows: {df.shape[0]} | Columns: {df.shape[1]}")
        
        st.subheader("🔍 Raw Data Preview:")
        st.dataframe(df.head(10), use_container_width=True)

        st.markdown("---")
        st.subheader("🛠️ Cleaning Options:")

        col_a, col_b = st.columns(2)
        with col_a:
            remove_dups = st.checkbox("Remove Duplicate Rows", value=True)
            drop_empty_rows = st.checkbox("Drop Completely Empty Rows", value=True)

        with col_b:
            clean_spaces = st.checkbox("Trim Extra Whitespaces", value=True)

        if st.button("🚀 Clean Data Now", type="primary"):
            cleaned_df = df.copy()

            if remove_dups:
                cleaned_df = cleaned_df.drop_duplicates()

            if drop_empty_rows:
                cleaned_df = cleaned_df.dropna(how='all')

            if clean_spaces:
                for col in cleaned_df.select_dtypes(include=['object']).columns:
                    cleaned_df[col] = cleaned_df[col].astype(str).str.strip()

            st.success("✨ Data cleaned successfully!")
            st.dataframe(cleaned_df.head(10), use_container_width=True)

            # Prepare buffer for download
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                cleaned_df.to_excel(writer, index=False, sheet_name='Cleaned_Data')
            buffer.seek(0)

            st.download_button(
                label="📥 Download Cleaned Excel (.xlsx)",
                data=buffer,
                file_name="Cleaned_Data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    except Exception as e:
        st.error(f"Error reading file: {e}")