import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit app title
st.title("Engagement Rate Analysis App")

# File uploader
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write("### Data Preview")
    st.dataframe(df.head())
    
    # Display basic statistics
    st.write("### Basic Statistics")
    st.write(df.describe())
    
    # Column selection for visualization
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    if numeric_columns:
        column = st.selectbox("Select a numeric column to visualize", numeric_columns)
        
        # Histogram
        st.write(f"### Distribution of {column}")
        fig, ax = plt.subplots()
        sns.histplot(df[column], bins=20, kde=True, ax=ax)
        st.pyplot(fig)
        
        # Boxplot
        st.write(f"### Boxplot of {column}")
        fig, ax = plt.subplots()
        sns.boxplot(y=df[column], ax=ax)
        st.pyplot(fig)
    else:
        st.write("No numeric columns available for visualization.")
