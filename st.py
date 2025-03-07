import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error, r2_score

# Streamlit App Title
st.title("Engagement Rate Analysis")

# File Uploader
df_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if df_file:
    df = pd.read_excel(df_file)
    st.write("### Dataset Preview")
    st.dataframe(df.head())
    
    # Dataset Information
    st.write("### Dataset Information")
    st.write(df.info())
    st.write("Shape of the dataset:", df.shape)
    st.write("Column Data Types:")
    st.write(df.dtypes)
    
    # Summary Statistics
    st.write("### Summary Statistics")
    st.write(df.describe())
    
    # Handling Missing Values
    st.write("### Missing Values")
    missing_values = df.isnull().sum()
    st.write(missing_values[missing_values > 0])
    
    # Visualization: Correlation Heatmap
    st.write("### Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)
    
    # Visualization: Pairplot
    st.write("### Pairplot")
    pairplot_fig = sns.pairplot(df)
    st.pyplot(pairplot_fig)
    
    # Further Analysis or Model Training (Can be added as per requirement)
    
    st.write("### Additional Analysis Coming Soon!")

# Run the app with: streamlit run app.py
