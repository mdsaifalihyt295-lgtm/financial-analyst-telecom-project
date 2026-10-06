import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Financial Analyst Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Financial Analyst Dashboard")
st.write("Telecom Data Analysis & Financial Insights")

# Upload CSV file
uploaded_file = st.file_uploader(
    "Upload your Telecom Dataset (CSV)",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset uploaded successfully!")

    # Sidebar
    st.sidebar.header("Dashboard Filters")

    # Dataset information
    st.subheader("📋 Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Records", f"{len(df):,}")

    with col2:
        st.metric("Total Columns", len(df.columns))

    with col3:
        st.metric("Missing Values", int(df.isnull().sum().sum()))

    with col4:
        st.metric("Duplicate Rows", int(df.duplicated().sum()))

    st.divider()

    # Data preview
    st.subheader("🔎 Data Preview")
    st.dataframe(df.head(20), use_container_width=True)

    st.divider()

    # Numeric columns
    numeric_columns = df.select_dtypes(
        include=np.number
    ).columns.tolist()

    if numeric_columns:

        st.subheader("📈 Financial / Numerical Analysis")

        selected_column = st.selectbox(
            "Select a numerical variable",
            numeric_columns
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Average",
                f"{df[selected_column].mean():,.2f}"
            )

        with col2:
            st.metric(
                "Maximum",
                f"{df[selected_column].max():,.2f}"
            )

        with col3:
            st.metric(
                "Minimum",
                f"{df[selected_column].min():,.2f}"
            )

        st.subheader(f"📊 {selected_column} Distribution")

        chart_data = df[[selected_column]].dropna()
        st.bar_chart(chart_data.head(50))

        st.divider()

        # Statistical summary
        st.subheader("📑 Statistical Summary")
        st.dataframe(
            df[numeric_columns].describe(),
            use_container_width=True
        )

    else:
        st.warning("No numerical columns found in this dataset.")

    # Categorical analysis
    categorical_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    if categorical_columns:

        st.divider()
        st.subheader("📌 Category Analysis")

        selected_category = st.selectbox(
            "Select a categorical variable",
            categorical_columns
        )

        category_counts = (
            df[selected_category]
            .value_counts()
            .head(10)
        )

        st.bar_chart(category_counts)

    # Missing value analysis
    st.divider()

    st.subheader("⚠️ Missing Value Analysis")

    missing_data = df.isnull().sum()
    missing_data = missing_data[missing_data > 0]

    if len(missing_data) > 0:
        st.dataframe(
            missing_data.rename("Missing Values"),
            use_container_width=True
        )
    else:
        st.success("No missing values found!")

    # Final insights
    st.divider()

    st.subheader("💡 Financial Analyst Insights")

    st.write(
        "• The dashboard provides an overview of the telecom dataset."
    )
    st.write(
        "• Numerical variables can be analysed using descriptive statistics."
    )
    st.write(
        "• Categorical variables help identify customer or business patterns."
    )
    st.write(
        "• Missing-value analysis helps improve data quality."
    )
    st.write(
        "• These insights can support better financial and business decisions."
    )

else:

    st.info(
        "👆 Please upload your Telecom Dataset (CSV) to start the analysis."
    )

    st.subheader("📌 Project Objective")

    st.write(
        "This Streamlit dashboard is designed for a Financial Analyst "
        "project to analyse telecom business data and generate useful "
        "financial and business insights."
    )

    st.subheader("📊 Dashboard Features")

    st.write("✅ Dataset overview")
    st.write("✅ Financial/numerical analysis")
    st.write("✅ Statistical summary")
    st.write("✅ Category analysis")
    st.write("✅ Missing value analysis")
    st.write("✅ Business insights")
