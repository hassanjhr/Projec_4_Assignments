import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="📊 Data Dashboard", page_icon="📈")

st.title("📊 Simple Data Dashboard")
st.markdown("Upload a CSV file and explore your data easily!")

uploaded_file = st.file_uploader("📂 Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("🔍 Data Preview")
    st.write(df.head())

    st.subheader("📋 Data Summary")
    st.write(df.describe())

    st.subheader("🔎 Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by 🔽", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value to filter 🔽", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.success(f"Showing results where `{selected_column}` is `{selected_value}` ✅")
    st.write(filtered_df)

    st.subheader("📈 Plot Data")
    x_column = st.selectbox("X-axis column", columns)
    y_column = st.selectbox("Y-axis column", columns)

    if st.button("Generate Plot 🚀"):
        try:
            st.line_chart(filtered_df.set_index(x_column)[y_column])
        except Exception as e:
            st.error(f"⚠️ Error plotting data: {e}")
else:
    st.info("📥 Waiting on CSV file upload... Upload one to begin.")
