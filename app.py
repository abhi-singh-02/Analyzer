import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor

# Streamlit UI
st.title("Engagement Rate Analysis App")

# Upload Data
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(df.head())
    
    # Data Cleaning
    df['Platform'].replace({'insta': 'Insta'}, inplace=True)
    df['type'].replace({'post': 'POST', 'Post': 'POST', 'reel': 'REEL'}, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df.rename(columns={'CourseName': 'Course Name', 'Share ': 'Share'}, inplace=True)
    
    # Data Validation Summary
    st.write("### Data Summary")
    st.write(df.describe())
    
    # Visualizations
    st.write("### Visualizations")
    fig, ax = plt.subplots()
    sns.histplot(df['Engagement Rate'], kde=True, bins=20, ax=ax)
    ax.set_title("Distribution of Engagement Rate")
    st.pyplot(fig)
    
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='type', ax=ax)
    ax.set_title("Content Type Distribution")
    st.pyplot(fig)
    
    # Model Training
    X = df[['Course Name', 'type', 'Followers', 'Likes', 'Comments', 'Share', 'Total Engagement']]
    y = df['Engagement Rate']
    
    categorical_features = ['Course Name', 'type']
    numerical_features = ['Followers', 'Likes', 'Comments', 'Share', 'Total Engagement']
    
    preprocessor = ColumnTransformer([
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])
    
    model = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', KNeighborsRegressor(n_neighbors=5))
    ])
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    test_r2 = r2_score(y_test, y_pred)
    st.write(f"Model R² Score: {test_r2:.2f}")
    
    # Prediction
    st.write("### Predict Engagement Rate")
    followers = st.number_input("Followers", min_value=0)
    likes = st.number_input("Likes", min_value=0)
    comments = st.number_input("Comments", min_value=0)
    shares = st.number_input("Shares", min_value=0)
    total_engagement = likes + comments + shares
    course_name = st.selectbox("Course Name", df['Course Name'].unique())
    content_type = st.selectbox("Content Type", df['type'].unique())
    
    if st.button("Predict"):
        input_data = pd.DataFrame([[course_name, content_type, followers, likes, comments, shares, total_engagement]],
                                  columns=['Course Name', 'type', 'Followers', 'Likes', 'Comments', 'Share', 'Total Engagement'])
        predicted_engagement_rate = model.predict(input_data)
        st.write(f"Predicted Engagement Rate: {predicted_engagement_rate[0]:.4f}")
