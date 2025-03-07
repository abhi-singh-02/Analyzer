#!/usr/bin/env python
# coding: utf-8

# - Business: Impact or trends of social media on various Technical courses.
#   
# - Objective: Engagement Rate Analysis of various technical courses on
#   social media platform.Here Instagram is used as a platform.
#   
# - Data source:Collected manually by visiting the instagram page of various
#   institute of Hyderabad which provide specially Data Science,Full Stack
#   Development and AWS,Devops,Azure and GCP courses.
#   
# -  Skill:
#   
# -  EDA
# 
#     - Descriptive Analysis
#     - Visual Analisrm.
# 
# 
# 

# <b>1. Data Validation
# **********************

# In[1]:


# Import Base Libraries
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error, r2_score
import streamlit as st

# To Suppress Warnings
import warnings
warnings.filterwarnings("ignore")


# In[4]:


# To Display Graphs In Middle
from IPython.core.display import HTML as Center
Center(""" <style>.output_png {display: table-cell;.text-align: center;vertical-align: middle;}</style> """)


# #### Load the Collected Dataset

# In[6]:


# Data file as pandas df


# In[7]:


#df = pd.read_excel(r'C:\Users\Admin\Nikhat DataSc\InternshipDS\FINAL Files\DSAIDA dataset.xlsx', sheet_name = 'Engagement Rate Analysis ')


# In[8]:


df = pd.read_excel(r"C:\Users\Abhishek Singh\Project 2\DSAIDA_Validated.xlsx")


# In[9]:


display(df)


# In[10]:


df.head()


# **Basic Checks**

# In[12]:


df.columns


# In[13]:


df.shape


# In[14]:


df.dtypes


# In[15]:


df.info()


# In[ ]:





# **EDA**

# Data Validation
# 
#        - We have to check Data types of each and every columns.

# <b>                        Column data validation:

# In[19]:


#Taking a function for column data varification
def colvalidate(df,col):
    print("Column:",col)
    print()
    print(f"Number of unique values in column: {df[col].nunique()}")
    print()
    print("Unique value in column:")
    print(df[col].unique())
    print()
    print("Data type of Column:")
    print(df[col].dtype)
    print("********************************")
    print()


# Applying above function to each and every columns

# In[21]:


for col in df.columns:
    colvalidate(df,col)


# <b>1.column name: Institute Name

# In[23]:


colvalidate(df, 'Institute Name')


# - By Observing the above data  the names belongs to the same columns.
# - The datatype is also object.Means data is validated.

# In[ ]:





# <b>2.column name: CourseName

# In[26]:


colvalidate(df, 'CourseName')


# In[ ]:





# - The data belongs to same column.
# - The datatype is also object.Hece Validated.

# In[ ]:





# <b>3.column name:Platform

# In[29]:


colvalidate(df, 'Platform')


# 
# - Here both the data meaning is same  insta and Insta ,so we need to
#   convert in to one "Insta".

# In[31]:


# Using df replace method

df['Platform'].replace({'insta':'Insta'}, inplace=True)


# In[32]:


colvalidate(df, 'Platform')


# -Now this data is validated.

# <b>4.column name:Followers

# In[35]:


colvalidate(df, 'Followers')


# - Values are valid, belongs to the column
# -
# Col data type i alsos valid

# In[ ]:





# <b>5.column name:type

# In[38]:


colvalidate(df, 'type')


# - By observing the data need to convert in only two types "POST" and "REEL"

# In[40]:


# Using df replace method

df['type'].replace({'post':'POST',
                    'Post':'POST',
                    'reel':'REEL'

                   },

                   inplace=True)


# In[41]:


colvalidate(df, 'type')


# - Now values are valid and belongs to the column
# - Col data type is also valid

# In[ ]:





# <b>6.column name:Likes

# In[44]:


colvalidate(df, 'Likes')


# - Data is valid ,belongs to the column
# - Datatype is also valid.

# In[ ]:





# <b>7.column name: Comments

# In[47]:


colvalidate(df, 'Comments')


# - Data is valid ,belongs to the column
# - Datatype is also valid.

# <b>8.column name: Share

# In[50]:


colvalidate(df, 'Share ')


# - Data is valid ,belongs to the column
# - Datatype is also valid.

# In[ ]:





# <b>9.column name: Date

# In[53]:


colvalidate(df, 'Date')


# need to change in a single Datetime format.

# In[55]:


df['Date'] = pd.to_datetime(df['Date'])


# In[56]:


colvalidate(df, 'Date')


# - Now values are valid and belongs to the column
# - Col data type is also valid

# <b>10.column name: Total Engagement

# In[59]:


colvalidate(df, 'Total Engagement')


# - Now values are valid and belongs to the column
# - Col data type is also valid

# In[ ]:





# <b>11.column name: EngagementRate

# In[62]:


colvalidate(df, 'Engagement Rate')


# - Now values are valid and belongs to the column
# - Col data type is also valid

# - Url is also valid and belongs to same cloumn
# - datatype is also valid.

# In[65]:


df.columns


# In[66]:


df.rename(columns={'CourseName': 'Course Name'}, inplace=True)
df.rename(columns={'Share ': 'Share'}, inplace=True)

X = df[['Course Name', 'type', 'Followers', 'Likes', 'Comments', 'Share', 'Total Engagement']]
y = df['Engagement Rate']

categorical_features = ['Course Name', 'type']
numerical_features = ['Followers', 'Likes', 'Comments', 'Share', 'Total Engagement']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])


# In[67]:


df.info()


# In[68]:


sm = df
sm.columns


# In[69]:


sm.drop_duplicates(inplace=True)


# In[70]:


sm.duplicated().sum()


# In[ ]:





# DESCRIPTIVE STATISTICS
# 

# In[ ]:





# In[72]:


sm['Followers'].describe()


# In[73]:


sm['Likes'].describe()


# In[74]:


sm['Comments'].describe()


# In[75]:


sm['Share'].describe()


# In[76]:


sm['Total Engagement'].describe()


# In[77]:


sm['Engagement Rate'].describe()


# In[78]:


sm['Course Name'].describe()


# In[79]:


sm['Date'].describe()


# In[80]:


sm['type'].describe()


# In[81]:


# Univariate Analysis - Distribution of Engagement Rate
plt.figure(figsize=(8, 6))
sns.histplot(sm['Engagement Rate'], kde=True, bins=20)
plt.title('Distribution of Engagement Rate')
plt.xlabel('Engagement Rate')
plt.ylabel('Frequency')

plt.show()


# **Insights
# -Mostly the of engagement rate of courses ranges between 0 & 1**
# 
# 
# 
# 

# In[83]:


# Univariate Analysis - Content Type Frequency
plt.figure(figsize=(8, 6))
sns.countplot(data=sm, x='type')
plt.title('Content Type Distribution')
plt.xlabel('Content Type')
plt.ylabel('Count')

plt.show()


# **Insights - Majority of the content posted on social media is in the for of text/image form i.e Posts**

# In[85]:


# Univariate Analysis -Course Distribution
import numpy as np
plt.figure(figsize=(8, 6))
sns.countplot(data=sm, x='Course Name', order=sm['Course Name'].value_counts().index)
plt.title('Course Distribution')
plt.xlabel('Course Name')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Count')

plt.show()


# **Insights-Content regarding Full Stack Development Courses are uploaded more**

# In[87]:


# Bivariate Analysis - Engagement Rate vs. Total Engagement
plt.figure(figsize=(8, 6))
sns.scatterplot(data=sm, x='Total Engagement', y='Engagement Rate', hue='Platform')
plt.title('Engagement Rate vs. Total Engagement')
plt.xlabel('Total Engagement')
plt.ylabel('Engagement Rate')
plt.show()


# **Insights- As the total engagement increases the engagement rate also increases and clustering indicates most of total engagement values are under 200 and engagement rate is under 1**

# In[89]:


# Bivariate Analysis - Likes vs. Comments by Content Type
plt.figure(figsize=(8, 6))
sns.scatterplot(data=sm, x='Likes', y='Comments', hue='type')
plt.title('Likes vs. Comments by Content Type')
plt.xlabel('Likes')
plt.ylabel('Comments')

plt.show()


# **Insights- Majority of likes are more on posts and it indicates that post might have more likes but reels may get more comments**

# In[91]:


content_type_engagement_rate = sm.groupby('type')['Engagement Rate'].mean().reset_index()

plt.figure(figsize=(8, 6))
sns.barplot(data=content_type_engagement_rate, x='type', y='Engagement Rate')
plt.title('Average Engagement Rate by Content Type')
plt.xlabel('Content Type')
plt.ylabel('Average Engagement Rate')

plt.show()


# **Insights-Info about courses uploaded in video format i.e Reels may get more engagement**

# In[93]:


# Multivariate Analysis - Engagement Rate by Platform and Content Type
plt.figure(figsize=(12, 6))
sns.barplot(data=sm, x='Platform', y='Engagement Rate', hue='type')
plt.title('Engagement Rate by Platform and Content Type')
plt.xlabel('Platform')
plt.ylabel('Engagement Rate')

plt.show()


# **Insights-The engagement rate for Reels is  higher than posts even though most of post and reels have engagement rate ranging between 0&1**

# In[95]:


# Multivariate Analysis - Correlation Heatmap for Numerical Variables
plt.figure(figsize=(10, 6))
corr = sm[['Followers', 'Likes', 'Comments', 'Share', 'Total Engagement', 'Engagement Rate']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()


# In[96]:


# Multivariate Analysis - Engagement Rate by courses and Content Type
plt.figure(figsize=(12, 6))
sns.barplot(data=sm, x='Course Name', y='Engagement Rate', hue='type')
plt.title('Engagement Rate by Platform and Content Type')
plt.xlabel('CourseName')
plt.ylabel('Engagement Rate')
plt.show()


# **Insights - Most of the courses have similiar engagement rate but few courses reels(outliers) got high engagement rate i.e reels became viral**

# In[98]:


# Multivariate Analysis - Total Engagement  by Likes Cmments Share and Content Type
content_type_engagement = sm.groupby('type')[['Likes', 'Comments', 'Share', 'Total Engagement']].sum().reset_index()
content_type_engagement = content_type_engagement.melt(id_vars='type', var_name='Metric', value_name='Total')

plt.figure(figsize=(10, 6))
sns.barplot(data=content_type_engagement, x='type', y='Total', hue='Metric')
plt.title('Engagement by Content Type')
plt.ylabel('Total Engagement')

plt.show()


# **Insights- Likes are more on reels compared to posts indicating reels have higher total engagement**

# In[100]:


course_engagement = sm.groupby("Course Name")["Total Engagement"].sum().reset_index()
course_engagement = course_engagement.sort_values(by="Total Engagement", ascending=False)

plt.figure(figsize=(12, 8))
sns.barplot(x="Total Engagement", y="Course Name", data=course_engagement, palette="Blues_r")
plt.title("Most Engaging Courses", fontsize=16)
plt.xlabel("Total Engagement", fontsize=12)
plt.ylabel("Courses", fontsize=12)
plt.show()


# **Insights-Full Stack Development courses have higher total engagement**

# In[ ]:





# 

# In[103]:


institute_engagement = sm.groupby("Institute Name")["Total Engagement"].sum().reset_index()
institute_engagement = institute_engagement.sort_values(by="Total Engagement", ascending=False)

plt.figure(figsize=(12, 8))
sns.barplot(x="Total Engagement", y="Institute Name", data=institute_engagement, palette="magma")
plt.title("Engagement by Institutes", fontsize=16)
plt.xlabel("Total Engagement", fontsize=12)
plt.ylabel("Institutes", fontsize=12)
plt.show()


# **Insights-The institute "Naresh i Technologies" has higher total engagement i.e Likes+Comments+Shares**

# In[ ]:





# In[105]:


sm['Day of Week'] = sm['Date'].dt.day_name()
day_engagement = sm.groupby('Day of Week')[['Total Engagement']].mean().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
)

plt.figure(figsize=(10, 6))
sns.barplot(x=day_engagement.index, y=day_engagement['Total Engagement'])
plt.title('Average Engagement by Day of the Week')
plt.xlabel('Day of Week')
plt.ylabel('Average Engagement')

plt.show()




# **Insights-Content posted on Wednesday have higher engagement compared to content posted on other days of the week**

# In[ ]:





# In[107]:


classes=sm['Course Name'].value_counts().sort_values(ascending=False)[0:10]
vals=sm['Course Name'].value_counts().sort_values(ascending=False)[0:10].values
plt.style.use('ggplot')
plt.figure(figsize=(8,8))
plt.pie(x=vals,labels=classes.index,autopct=lambda p:f'{p:.2f}%,({p*sum(vals)})')
plt.legend()
plt.show()


# **Insights-Full Stack Develppment courses have majority share in instagram platform engagement**

# In[109]:


###### Linear Regression ########

from sklearn.linear_model import LinearRegression

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model.fit(X_train, y_train)

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print(f"Train RMSE: {train_rmse}")
print(f"Test RMSE: {test_rmse}")
print(f"Train R2 Score: {train_r2}")
print(f"Test R2 Score: {test_r2}")


# In[ ]:





# In[ ]:





# In[110]:


###### POlynomial Regression #######

from sklearn.preprocessing import PolynomialFeatures


poly = PolynomialFeatures(degree=2, include_bias=False)

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('poly', poly),
    ('regressor', LinearRegression())
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model.fit(X_train, y_train)

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print(f"Train RMSE: {train_rmse}")
print(f"Test RMSE: {test_rmse}")
print(f"Train R2 Score: {train_r2}")
print(f"Test R2 Score: {test_r2}")


# In[111]:


####### Lasso Regression #######

from sklearn.linear_model import Lasso



model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', Lasso(alpha=0.1))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model.fit(X_train, y_train)

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print(f"Train RMSE: {train_rmse}")
print(f"Test RMSE: {test_rmse}")
print(f"Train R2 Score: {train_r2}")
print(f"Test R2 Score: {test_r2}")


# In[112]:


####### Ridge Regression #####

from sklearn.linear_model import Ridge


model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', Ridge(alpha=0.1))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model.fit(X_train, y_train)

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print(f"Train RMSE: {train_rmse}")
print(f"Test RMSE: {test_rmse}")
print(f"Train R2 Score: {train_r2}")
print(f"Test R2 Score: {test_r2}")


# In[113]:


####### Decision Tree #########

from sklearn.tree import DecisionTreeRegressor, plot_tree

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', DecisionTreeRegressor(random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model.fit(X_train, y_train)

regressor = model.named_steps['regressor']

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print(f"Train RMSE: {train_rmse}")
print(f"Test RMSE: {test_rmse}")
print(f"Train R2 Score: {train_r2}")
print(f"Test R2 Score: {test_r2}")

tree_fig, ax = plt.subplots(figsize=(300, 50))
plot_tree(regressor, filled=True, feature_names=numerical_features + list(model.named_steps['preprocessor'].named_transformers_['cat'].get_feature_names_out()), ax=ax)
plt.show()


# In[114]:


####### XGBoost Regressor #######

from xgboost import XGBRegressor

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42))
])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model.fit(X_train, y_train)


y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)


train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print(f"Train RMSE: {train_rmse}")
print(f"Test RMSE: {test_rmse}")
print(f"Train R2 Score: {train_r2}")
print(f"Test R2 Score: {test_r2}")


# In[115]:


####### SVM #######


from sklearn.svm import SVR

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', SVR(kernel='rbf', C=1.0, epsilon=0.1))
])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model.fit(X_train, y_train)


y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)


train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print(f"Train RMSE: {train_rmse}")
print(f"Test RMSE: {test_rmse}")
print(f"Train R2 Score: {train_r2}")
print(f"Test R2 Score: {test_r2}")


# In[116]:


### RANDOM FOREST #####

from sklearn.ensemble import RandomForestRegressor

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model.fit(X_train, y_train)


y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)


train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print(f"Train RMSE: {train_rmse}")
print(f"Test RMSE: {test_rmse}")
print(f"Train R2 Score: {train_r2}")
print(f"Test R2 Score: {test_r2}")


# In[117]:


#KNN Regression

from sklearn.neighbors import KNeighborsRegressor

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', KNeighborsRegressor(n_neighbors=5))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model.fit(X_train, y_train)

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print(f"Train RMSE: {train_rmse}")
print(f"Test RMSE: {test_rmse}")
print(f"Train R2 Score: {train_r2}")
print(f"Test R2 Score: {test_r2}")


# In[118]:


# Models to evaluate
models = {
    'Linear Regression': LinearRegression(),
    'Polynomial Regression': Pipeline([
        ('poly', PolynomialFeatures(degree=2, include_bias=False)),
        ('regressor', LinearRegression())
    ]),
    'Lasso Regression': Lasso(alpha=0.1),
    'Ridge Regression': Ridge(alpha=0.1),
    'Decision Tree': DecisionTreeRegressor(random_state=42),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
    'Support Vector Machine': SVR(),
    'K-Nearest Neighbors': KNeighborsRegressor(n_neighbors=5),
    'XGBoost': XGBRegressor(objective='reg:squarederror', n_estimators=100, random_state=42)
}

results = {}

# Train and evaluate models
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
for name, model in models.items():
    pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('regressor', model)])
    pipeline.fit(X_train, y_train)
    
    y_train_pred = pipeline.predict(X_train)
    y_test_pred = pipeline.predict(X_test)
    
    train_r2 = r2_score(y_train, y_train_pred)
    test_r2 = r2_score(y_test, y_test_pred)
    
    results[name] = {'train_r2': train_r2, 'test_r2': test_r2, 'difference': abs(train_r2 - test_r2)}

# Find the best model with rules: R² (train & test) between 70-90% and difference ≤ 10%
best_model = None
best_r2 = 0
for model, scores in results.items():
    if (0.70 <= scores['train_r2'] <= 0.90 and 0.70 <= scores['test_r2'] <= 0.90 and scores['difference'] <= 0.10):
        if scores['test_r2'] > best_r2:
            best_model = model
            best_r2 = scores['test_r2']

print("Best Model within rules:", best_model, "with Test R² Score:", best_r2)


# In[119]:


import joblib

def predict_engagement(KNN):
    followers = float(input("Enter number of Followers: "))
    likes = float(input("Enter number of Likes: "))
    comments = float(input("Enter number of Comments: "))
    shares = float(input("Enter number of Shares: "))
    total_engagement = float(likes+comments+shares)
    print("Total Engagement: ", total_engagement)

    course_name = input("Enter Course Name: ")
    content_type = input("Enter Content Type: ")

    input_data = pd.DataFrame([[course_name, content_type, followers, likes, comments, shares, total_engagement]],
                              columns=['CourseName', 'type', 'Followers', 'Likes', 'Comments', 'Share', 'Total Engagement'])

    predicted_engagement_rate = KNN.predict(input_data)

    print(f"Predicted Engagement Rate: {predicted_engagement_rate[0]}")

KNN = joblib.load('knn_model.pkl')
predict_engagement(KNN)


# In[ ]:





# In[ ]:





# In[ ]:




