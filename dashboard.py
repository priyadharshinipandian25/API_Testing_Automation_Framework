
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="API Testing Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("API Testing & Automation Dashboard")
st.caption("Advanced QA Testing Framework")

# Current project test results
data = {
    "Module": [
        "Authentication",
        "Generated API Tests",
        "Health & Users",
        "Performance"
    ],
    "Passed": [9, 4, 10, 1],
    "Failed": [0, 0, 0, 0]
}

df = pd.DataFrame(data)

total_passed = df["Passed"].sum()
total_failed = df["Failed"].sum()
total_tests = total_passed + total_failed

col1, col2, col3 = st.columns(3)

col1.metric("Total Tests", total_tests)
col2.metric("Passed", total_passed)
col3.metric("Failed", total_failed)

st.subheader("Module-wise Test Results")
st.bar_chart(
    df.set_index("Module")[["Passed", "Failed"]]
)

st.subheader("Detailed Report")
st.dataframe(df, use_container_width=True)

st.success("All recorded tests passed!")
