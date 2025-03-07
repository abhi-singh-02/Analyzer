{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "4b793c7a-c138-45ed-a139-834d64689dc9",
   "metadata": {
    "id": "4b793c7a-c138-45ed-a139-834d64689dc9"
   },
   "source": [
    "- Business: Impact or trends of social media on various Technical courses.\n",
    "  \n",
    "- Objective: Engagement Rate Analysis of various technical courses on\n",
    "  social media platform.Here Instagram is used as a platform.\n",
    "  \n",
    "- Data source:Collected manually by visiting the instagram page of various\n",
    "  institute of Hyderabad which provide specially Data Science,Full Stack\n",
    "  Development and AWS,Devops,Azure and GCP courses.\n",
    "  \n",
    "-  Skill:\n",
    "  \n",
    "-  EDA\n",
    "\n",
    "    - Descriptive Analysis\n",
    "    - Visual Analisrm.\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "09a6a7a5-c333-40a2-a29d-c3ff65038aa3",
   "metadata": {
    "id": "09a6a7a5-c333-40a2-a29d-c3ff65038aa3"
   },
   "source": [
    "<b>1. Data Validation\n",
    "**********************"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e7fcf5a5-964d-43d1-9072-bdaa25f93c35",
   "metadata": {
    "id": "e7fcf5a5-964d-43d1-9072-bdaa25f93c35"
   },
   "outputs": [],
   "source": [
    "# Import Base Libraries\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import OneHotEncoder, StandardScaler\n",
    "from sklearn.pipeline import Pipeline\n",
    "from sklearn.compose import ColumnTransformer\n",
    "from sklearn.metrics import mean_squared_error, r2_score\n",
    "\n",
    "# To Suppress Warnings\n",
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "501e1264-0e0d-45c7-a118-5cd1d6d502de",
   "metadata": {
    "id": "501e1264-0e0d-45c7-a118-5cd1d6d502de",
    "outputId": "ca72e438-f797-480b-9134-4d6a97d743d2"
   },
   "outputs": [],
   "source": [
    "# To Display Graphs In Middle\n",
    "from IPython.core.display import HTML as Center\n",
    "Center(\"\"\" <style>.output_png {display: table-cell;.text-align: center;vertical-align: middle;}</style> \"\"\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a08c1ae6-4b9b-4754-8816-c812ebdbdc90",
   "metadata": {
    "id": "a08c1ae6-4b9b-4754-8816-c812ebdbdc90"
   },
   "source": [
    "#### Load the Collected Dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f22df92a-cde6-4d8a-b395-c44819133561",
   "metadata": {
    "id": "f22df92a-cde6-4d8a-b395-c44819133561"
   },
   "outputs": [],
   "source": [
    "# Data file as pandas df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6aa7557f-d1eb-4ef2-9913-9fed214b23e2",
   "metadata": {
    "id": "6aa7557f-d1eb-4ef2-9913-9fed214b23e2"
   },
   "outputs": [],
   "source": [
    "#df = pd.read_excel(r'C:\\Users\\Admin\\Nikhat DataSc\\InternshipDS\\FINAL Files\\DSAIDA dataset.xlsx', sheet_name = 'Engagement Rate Analysis ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ae359b1a-072b-4619-94c1-c2882169a4ee",
   "metadata": {
    "id": "ae359b1a-072b-4619-94c1-c2882169a4ee"
   },
   "outputs": [],
   "source": [
    "df = pd.read_excel(r\"C:\\Users\\Abhishek Singh\\Project 2\\DSAIDA_Validated.xlsx\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "559b75a4-c2b7-4624-80d2-21e8a4567e8e",
   "metadata": {
    "id": "559b75a4-c2b7-4624-80d2-21e8a4567e8e",
    "outputId": "83e6c103-88e1-4d18-ea38-9bd747e70f14"
   },
   "outputs": [],
   "source": [
    "display(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "35d74ecd-abf8-4642-90cf-2d0e71e061ca",
   "metadata": {
    "id": "35d74ecd-abf8-4642-90cf-2d0e71e061ca",
    "outputId": "4e676de9-c8d0-4d8b-9888-825dd66e12c5"
   },
   "outputs": [],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3998a2c0-2ac1-4fcd-abdd-32f1fa12e158",
   "metadata": {
    "id": "3998a2c0-2ac1-4fcd-abdd-32f1fa12e158"
   },
   "source": [
    "**Basic Checks**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5d8f34ec-938a-45ea-a658-3eca2934324b",
   "metadata": {
    "id": "5d8f34ec-938a-45ea-a658-3eca2934324b",
    "outputId": "7cefbb23-09ec-4b37-9521-917e3538598b"
   },
   "outputs": [],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b95a3c1d-70a1-4314-84d0-3e8dff7991c3",
   "metadata": {
    "id": "b95a3c1d-70a1-4314-84d0-3e8dff7991c3",
    "outputId": "580977b9-dadb-46b4-90a2-bb1a11b1e368"
   },
   "outputs": [],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "36fec441-3b94-4520-bc53-f4daf46a06ed",
   "metadata": {
    "id": "36fec441-3b94-4520-bc53-f4daf46a06ed",
    "outputId": "ae28e9ad-1bf8-49af-9f5e-e15049805208"
   },
   "outputs": [],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3cb21443-c2d8-4006-beab-6ecb4752d98d",
   "metadata": {
    "id": "3cb21443-c2d8-4006-beab-6ecb4752d98d",
    "outputId": "faae1a51-bca6-4a89-9522-d59ffc92e2b0"
   },
   "outputs": [],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "35cbe084-c8f6-478d-9d73-b30d6c0e7be3",
   "metadata": {
    "id": "35cbe084-c8f6-478d-9d73-b30d6c0e7be3"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "c6b4eb53-e2b5-4cbe-8bab-6d4109d6985f",
   "metadata": {
    "id": "c6b4eb53-e2b5-4cbe-8bab-6d4109d6985f"
   },
   "source": [
    "**EDA**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c9fd4ef1-c4f8-4cc4-a544-660cdac0a8af",
   "metadata": {
    "id": "c9fd4ef1-c4f8-4cc4-a544-660cdac0a8af"
   },
   "source": [
    "Data Validation\n",
    "\n",
    "       - We have to check Data types of each and every columns."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a3838291-503f-400c-95d8-95b413cefea6",
   "metadata": {
    "id": "a3838291-503f-400c-95d8-95b413cefea6"
   },
   "source": [
    "<b>                        Column data validation:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8eee6dbd-3464-4aab-b761-dca3a9e26afd",
   "metadata": {
    "id": "8eee6dbd-3464-4aab-b761-dca3a9e26afd"
   },
   "outputs": [],
   "source": [
    "#Taking a function for column data varification\n",
    "def colvalidate(df,col):\n",
    "    print(\"Column:\",col)\n",
    "    print()\n",
    "    print(f\"Number of unique values in column: {df[col].nunique()}\")\n",
    "    print()\n",
    "    print(\"Unique value in column:\")\n",
    "    print(df[col].unique())\n",
    "    print()\n",
    "    print(\"Data type of Column:\")\n",
    "    print(df[col].dtype)\n",
    "    print(\"********************************\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "17195d67-81f5-4db2-b645-17bd1e0e895b",
   "metadata": {
    "id": "17195d67-81f5-4db2-b645-17bd1e0e895b"
   },
   "source": [
    "Applying above function to each and every columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d2eeb1f1-56b2-4257-853a-d35c2c1bf0b3",
   "metadata": {
    "id": "d2eeb1f1-56b2-4257-853a-d35c2c1bf0b3",
    "outputId": "e44c2c4c-acb7-4f20-ecbf-d52f42eeedf3"
   },
   "outputs": [],
   "source": [
    "for col in df.columns:\n",
    "    colvalidate(df,col)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "52449010-012b-41d9-b877-07b2b7186e5c",
   "metadata": {
    "id": "52449010-012b-41d9-b877-07b2b7186e5c"
   },
   "source": [
    "<b>1.column name: Institute Name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bae0412a-ae2a-4591-ad5e-d221e6819cca",
   "metadata": {
    "id": "bae0412a-ae2a-4591-ad5e-d221e6819cca",
    "outputId": "8ffdbe84-0e88-457b-d1bb-83273b5e5055"
   },
   "outputs": [],
   "source": [
    "colvalidate(df, 'Institute Name')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ccae44e5-0852-4586-86fa-e4339b2c48cc",
   "metadata": {
    "id": "ccae44e5-0852-4586-86fa-e4339b2c48cc"
   },
   "source": [
    "- By Observing the above data  the names belongs to the same columns.\n",
    "- The datatype is also object.Means data is validated."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ed5305a7-1488-4801-99cc-691e3b259fde",
   "metadata": {
    "id": "ed5305a7-1488-4801-99cc-691e3b259fde"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "e8da764e-6cbd-48ee-b322-c45444b69b54",
   "metadata": {
    "id": "e8da764e-6cbd-48ee-b322-c45444b69b54"
   },
   "source": [
    "<b>2.column name: CourseName"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eaf14d4a-8db1-47aa-8267-d44cd566629a",
   "metadata": {
    "id": "eaf14d4a-8db1-47aa-8267-d44cd566629a",
    "outputId": "81d5c575-72ab-48a0-bdb3-4308575c1172"
   },
   "outputs": [],
   "source": [
    "colvalidate(df, 'CourseName')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b258a153-1d05-457c-b6db-ef32165be475",
   "metadata": {
    "id": "b258a153-1d05-457c-b6db-ef32165be475"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "436dc802-c3c4-4872-9baf-eac5c725d32c",
   "metadata": {
    "id": "436dc802-c3c4-4872-9baf-eac5c725d32c"
   },
   "source": [
    "- The data belongs to same column.\n",
    "- The datatype is also object.Hece Validated."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "90fe59fc-3512-4f93-8664-54c9d69b03c5",
   "metadata": {
    "id": "90fe59fc-3512-4f93-8664-54c9d69b03c5"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "3fcc8ce0-1275-48f8-8c41-85094a4bb99f",
   "metadata": {
    "id": "3fcc8ce0-1275-48f8-8c41-85094a4bb99f"
   },
   "source": [
    "<b>3.column name:Platform"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6705d430-e606-47cf-a6cd-e67f01581f41",
   "metadata": {
    "id": "6705d430-e606-47cf-a6cd-e67f01581f41",
    "outputId": "b7c42735-bee5-49e8-d41f-3dbf6c299307"
   },
   "outputs": [],
   "source": [
    "colvalidate(df, 'Platform')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fe1c356d-0b5e-42bd-b0d8-e39b9892a007",
   "metadata": {
    "id": "fe1c356d-0b5e-42bd-b0d8-e39b9892a007"
   },
   "source": [
    "\n",
    "- Here both the data meaning is same  insta and Insta ,so we need to\n",
    "  convert in to one \"Insta\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f90874a-c6fb-41dc-b819-0a442e5c9dd5",
   "metadata": {
    "id": "2f90874a-c6fb-41dc-b819-0a442e5c9dd5"
   },
   "outputs": [],
   "source": [
    "# Using df replace method\n",
    "\n",
    "df['Platform'].replace({'insta':'Insta'}, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "84bb881e-44bb-4847-9dd1-6254f9697aec",
   "metadata": {
    "id": "84bb881e-44bb-4847-9dd1-6254f9697aec",
    "outputId": "9c0e8dd0-62c0-4741-ae52-939d1048d903"
   },
   "outputs": [],
   "source": [
    "colvalidate(df, 'Platform')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fc2b849e-dffe-4c48-a277-4f661fc70654",
   "metadata": {
    "id": "fc2b849e-dffe-4c48-a277-4f661fc70654"
   },
   "source": [
    "-Now this data is validated."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3ad5b056-fe64-4c8f-a625-c1a9f356fd17",
   "metadata": {
    "id": "3ad5b056-fe64-4c8f-a625-c1a9f356fd17"
   },
   "source": [
    "<b>4.column name:Followers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b0e5038-cf9b-4a6f-b2be-562f6680fc43",
   "metadata": {
    "id": "3b0e5038-cf9b-4a6f-b2be-562f6680fc43",
    "outputId": "2e2697d6-7da9-4113-d315-16a6283f0ae5"
   },
   "outputs": [],
   "source": [
    "colvalidate(df, 'Followers')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ca78a0d8-f9b3-495c-9a60-8cef4feb1194",
   "metadata": {
    "id": "ca78a0d8-f9b3-495c-9a60-8cef4feb1194"
   },
   "source": [
    "- Values are valid, belongs to the column\n",
    "-\n",
    "Col data type i alsos valid"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d7b4ebbd-33ba-4532-8d51-778ba877416e",
   "metadata": {
    "id": "d7b4ebbd-33ba-4532-8d51-778ba877416e"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "f8aadbd6-688f-4216-b6d6-003d7dfeab26",
   "metadata": {
    "id": "f8aadbd6-688f-4216-b6d6-003d7dfeab26"
   },
   "source": [
    "<b>5.column name:type"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8c138407-cb52-4fa1-9426-0a5b40efef38",
   "metadata": {
    "id": "8c138407-cb52-4fa1-9426-0a5b40efef38",
    "outputId": "63711f83-8a46-4542-98e8-4a6baa270bc3"
   },
   "outputs": [],
   "source": [
    "colvalidate(df, 'type')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "76ba2014-b5ec-469e-bfdf-6ce7f8f4f8c9",
   "metadata": {
    "id": "76ba2014-b5ec-469e-bfdf-6ce7f8f4f8c9"
   },
   "source": [
    "- By observing the data need to convert in only two types \"POST\" and \"REEL\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "90daad5a-6d1f-4322-86b9-3c7637f3a228",
   "metadata": {
    "id": "90daad5a-6d1f-4322-86b9-3c7637f3a228"
   },
   "outputs": [],
   "source": [
    "# Using df replace method\n",
    "\n",
    "df['type'].replace({'post':'POST',\n",
    "                    'Post':'POST',\n",
    "                    'reel':'REEL'\n",
    "\n",
    "                   },\n",
    "\n",
    "                   inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ee927ed-627d-42ec-8a3e-d7d15db27b8c",
   "metadata": {
    "id": "7ee927ed-627d-42ec-8a3e-d7d15db27b8c",
    "outputId": "943e2036-1619-4c7f-989e-d5656f81c613"
   },
   "outputs": [],
   "source": [
    "colvalidate(df, 'type')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "66c6c24b-66eb-429c-8c40-f66f2ea00b3c",
   "metadata": {
    "id": "66c6c24b-66eb-429c-8c40-f66f2ea00b3c"
   },
   "source": [
    "- Now values are valid and belongs to the column\n",
    "- Col data type is also valid"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b8526ad5-0273-462d-9e8b-b4e1d41548bf",
   "metadata": {
    "id": "b8526ad5-0273-462d-9e8b-b4e1d41548bf"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "c494b806-355b-41df-aa2f-7554d08fe9c1",
   "metadata": {
    "id": "4b175994-cf95-4bec-baa6-629f382ad9ad"
   },
   "source": [
    "<b>6.column name:Likes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "72198bd9-f2ec-4648-a912-eeb14f793079",
   "metadata": {
    "id": "72198bd9-f2ec-4648-a912-eeb14f793079",
    "outputId": "5f85b540-95f8-4ea6-d38b-36113aa00a58"
   },
   "outputs": [],
   "source": [
    "colvalidate(df, 'Likes')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "98487505-e01b-4f92-9362-bffb0c81be55",
   "metadata": {
    "id": "98487505-e01b-4f92-9362-bffb0c81be55"
   },
   "source": [
    "- Data is valid ,belongs to the column\n",
    "- Datatype is also valid."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5d5ef076-41d2-4405-b1fe-e378a5ae0ad4",
   "metadata": {
    "id": "5d5ef076-41d2-4405-b1fe-e378a5ae0ad4"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "62d42364-8ecd-4dc2-a622-7e4637fef639",
   "metadata": {
    "id": "e0465a6c-5cd5-45ec-b7bc-12652e7ab7a6"
   },
   "source": [
    "<b>7.column name: Comments"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "61c17043-29ac-4cd7-bb64-3a710edd2810",
   "metadata": {
    "id": "61c17043-29ac-4cd7-bb64-3a710edd2810",
    "outputId": "79556cca-2a47-4c96-8ce9-e7250f4eae9d"
   },
   "outputs": [],
   "source": [
    "colvalidate(df, 'Comments')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2f77929b-acc1-4163-951a-7d2ce79aaa4a",
   "metadata": {
    "id": "2f77929b-acc1-4163-951a-7d2ce79aaa4a"
   },
   "source": [
    "- Data is valid ,belongs to the column\n",
    "- Datatype is also valid."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e4bccd15-d324-4812-8568-14de3ce0f1b5",
   "metadata": {
    "id": "ad034a1a-bbec-4772-8187-3244ed5d8d93"
   },
   "source": [
    "<b>8.column name: Share"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8e62b0e3-587e-490c-af32-5221757203fc",
   "metadata": {
    "id": "8e62b0e3-587e-490c-af32-5221757203fc",
    "outputId": "ad5144e2-92c1-460b-8d4d-0add9457318c"
   },
   "outputs": [],
   "source": [
    "colvalidate(df, 'Share ')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e4da5b50-0daa-4f90-b558-d17dda495793",
   "metadata": {
    "id": "3853fe5c-f61b-4da9-92a7-c5b3320bcfb5"
   },
   "source": [
    "- Data is valid ,belongs to the column\n",
    "- Datatype is also valid."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "afdf00c3-195f-4331-bc5b-9592c83e5353",
   "metadata": {
    "id": "afdf00c3-195f-4331-bc5b-9592c83e5353"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "653c3942-a985-43dd-a509-ca60ec263da5",
   "metadata": {
    "id": "33b82441-8849-46fb-b4b0-a5e0d7cce515"
   },
   "source": [
    "<b>9.column name: Date"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0bc59ae0-ae4a-4afa-9cc2-c27c81a81c92",
   "metadata": {
    "id": "0bc59ae0-ae4a-4afa-9cc2-c27c81a81c92",
    "outputId": "4086b9be-8005-4390-eb84-fcc5bf3735eb"
   },
   "outputs": [],
   "source": [
    "colvalidate(df, 'Date')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "65fa4a0c-0a6e-49f4-9831-9e5e805e2d1f",
   "metadata": {
    "id": "65fa4a0c-0a6e-49f4-9831-9e5e805e2d1f"
   },
   "source": [
    "need to change in a single Datetime format."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01c80b43-681a-45ab-b324-6daf84d0dd10",
   "metadata": {
    "id": "01c80b43-681a-45ab-b324-6daf84d0dd10"
   },
   "outputs": [],
   "source": [
    " df['Date'] = pd.to_datetime(df['Date'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b5492749-ba7a-4eef-a360-630286d53f2b",
   "metadata": {
    "id": "b5492749-ba7a-4eef-a360-630286d53f2b",
    "outputId": "ac7cbbe7-0457-493e-c4b3-72afc0bf48f4"
   },
   "outputs": [],
   "source": [
    "colvalidate(df, 'Date')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "413ecbfc-9e16-4e4d-a989-f1ef6b1cf596",
   "metadata": {
    "id": "413ecbfc-9e16-4e4d-a989-f1ef6b1cf596"
   },
   "source": [
    "- Now values are valid and belongs to the column\n",
    "- Col data type is also valid"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8953160d-377b-44dc-a60b-a0e9fc94f4c5",
   "metadata": {
    "id": "8139b0a7-83cb-46e1-9f91-eb1ea137c576"
   },
   "source": [
    "<b>10.column name: Total Engagement"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "67303e5f-256f-40e4-a491-5aa169380429",
   "metadata": {
    "id": "67303e5f-256f-40e4-a491-5aa169380429",
    "outputId": "0676bee1-b4da-43c6-8c6c-c0615bf35b6d"
   },
   "outputs": [],
   "source": [
    "colvalidate(df, 'Total Engagement')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "af5305bc-85c6-41a2-95ce-3a058dcb7ce9",
   "metadata": {
    "id": "af5305bc-85c6-41a2-95ce-3a058dcb7ce9"
   },
   "source": [
    "- Now values are valid and belongs to the column\n",
    "- Col data type is also valid"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "280d84b2-afbc-4f4a-be6f-d06f9dc35798",
   "metadata": {
    "id": "280d84b2-afbc-4f4a-be6f-d06f9dc35798"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "517f86b7-8553-44b8-b40b-a636326609cf",
   "metadata": {
    "id": "fdb392ad-5a6c-4169-bf96-ffb419ae0cdb"
   },
   "source": [
    "<b>11.column name: EngagementRate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38d5fccf-c296-42c0-99f9-b08037400f44",
   "metadata": {
    "id": "38d5fccf-c296-42c0-99f9-b08037400f44",
    "outputId": "ddd6d9d0-32eb-44c8-92ee-547b745a0007"
   },
   "outputs": [],
   "source": [
    "colvalidate(df, 'Engagement Rate')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "36b147cd-9b1c-46dd-92ab-24bf3913a4eb",
   "metadata": {
    "id": "36b147cd-9b1c-46dd-92ab-24bf3913a4eb"
   },
   "source": [
    "- Now values are valid and belongs to the column\n",
    "- Col data type is also valid"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "22e66349-6403-4ce5-9dbe-8df3ec476a3c",
   "metadata": {
    "id": "22e66349-6403-4ce5-9dbe-8df3ec476a3c"
   },
   "source": [
    "- Url is also valid and belongs to same cloumn\n",
    "- datatype is also valid."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62128022-ce5d-4156-b9a3-f39491eae4a9",
   "metadata": {
    "id": "62128022-ce5d-4156-b9a3-f39491eae4a9",
    "outputId": "9c083fff-3d6f-4a10-c2e3-f9d78f28398a"
   },
   "outputs": [],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c3be2100-0f8b-4e56-b134-c4c626820c43",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.rename(columns={'CourseName': 'Course Name'}, inplace=True)\n",
    "df.rename(columns={'Share ': 'Share'}, inplace=True)\n",
    "\n",
    "X = df[['Course Name', 'type', 'Followers', 'Likes', 'Comments', 'Share', 'Total Engagement']]\n",
    "y = df['Engagement Rate']\n",
    "\n",
    "categorical_features = ['Course Name', 'type']\n",
    "numerical_features = ['Followers', 'Likes', 'Comments', 'Share', 'Total Engagement']\n",
    "\n",
    "preprocessor = ColumnTransformer(\n",
    "    transformers=[\n",
    "        ('num', StandardScaler(), numerical_features),\n",
    "        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)\n",
    "    ])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a92f0608-d594-4736-9a60-f719c2385bbd",
   "metadata": {
    "id": "a92f0608-d594-4736-9a60-f719c2385bbd",
    "outputId": "a114b649-fe4e-46ce-a977-c9ab14087b1d"
   },
   "outputs": [],
   "source": [
    "df.info()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7bcc1081-da06-445b-8b21-c421f34749bc",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "7bcc1081-da06-445b-8b21-c421f34749bc",
    "outputId": "f9d81a94-a654-4126-924c-72fd69e02d55"
   },
   "outputs": [],
   "source": [
    "\n",
    "sm = df\n",
    "sm.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4fc0dd50-a98c-4156-b20d-127e5fac57cc",
   "metadata": {
    "id": "4fc0dd50-a98c-4156-b20d-127e5fac57cc"
   },
   "outputs": [],
   "source": [
    "sm.drop_duplicates(inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d69e50db-a061-42ce-b4e1-3697dd8f19c3",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "d69e50db-a061-42ce-b4e1-3697dd8f19c3",
    "outputId": "f4b71446-9302-4b5f-d6ee-dfb6d9d3f2ae"
   },
   "outputs": [],
   "source": [
    "sm.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "BMiovK1oVtiy",
   "metadata": {
    "id": "BMiovK1oVtiy"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "19QWrwZuXlPX",
   "metadata": {
    "id": "19QWrwZuXlPX"
   },
   "source": [
    "DESCRIPTIVE STATISTICS\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4-waWFYBVtlh",
   "metadata": {
    "id": "4-waWFYBVtlh"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ItMWv6bGVtor",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 335
    },
    "id": "ItMWv6bGVtor",
    "outputId": "0edc4684-e36e-4bc9-deba-0bce3789bf54"
   },
   "outputs": [],
   "source": [
    "sm['Followers'].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "lxbCxcwrVtrf",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 335
    },
    "id": "lxbCxcwrVtrf",
    "outputId": "c03c1e0f-7cbd-40d5-e08e-2ab4760f941d"
   },
   "outputs": [],
   "source": [
    "sm['Likes'].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "EjVJz7w0Vtum",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 335
    },
    "id": "EjVJz7w0Vtum",
    "outputId": "6edd81b2-94cd-4abb-e02f-9cd873960dab"
   },
   "outputs": [],
   "source": [
    "sm['Comments'].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "WaM9a5swVtxs",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 335
    },
    "id": "WaM9a5swVtxs",
    "outputId": "6ef770fe-95f2-484b-8bff-194f3d285ed8"
   },
   "outputs": [],
   "source": [
    "sm['Share'].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "86fwj0U2Vt0O",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 335
    },
    "id": "86fwj0U2Vt0O",
    "outputId": "b202fb84-4b19-4c65-f21f-13e19dd93ff7"
   },
   "outputs": [],
   "source": [
    "sm['Total Engagement'].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "RwycdR-6Vt2O",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 335
    },
    "id": "RwycdR-6Vt2O",
    "outputId": "04b3d17e-6956-4f41-abe9-eb45e8bddfbc"
   },
   "outputs": [],
   "source": [
    "sm['Engagement Rate'].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5NirpjC6Vt5B",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 210
    },
    "id": "5NirpjC6Vt5B",
    "outputId": "040b122d-525f-49d2-acda-50f8c11996ef"
   },
   "outputs": [],
   "source": [
    "sm['Course Name'].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "uiFUQ9LRyStZ",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 304
    },
    "id": "uiFUQ9LRyStZ",
    "outputId": "581d7f72-9af1-434c-a186-76baa15bda17"
   },
   "outputs": [],
   "source": [
    "sm['Date'].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8SvfCfsVVt7t",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 210
    },
    "id": "8SvfCfsVVt7t",
    "outputId": "47fb6fa6-9c56-4844-ab42-70c5858c386a"
   },
   "outputs": [],
   "source": [
    "sm['type'].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "XOVadMRFb8Sz",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 569
    },
    "id": "XOVadMRFb8Sz",
    "outputId": "2e08d8b2-600a-413c-8961-877d8e0a7410"
   },
   "outputs": [],
   "source": [
    "# Univariate Analysis - Distribution of Engagement Rate\n",
    "plt.figure(figsize=(8, 6))\n",
    "sns.histplot(sm['Engagement Rate'], kde=True, bins=20)\n",
    "plt.title('Distribution of Engagement Rate')\n",
    "plt.xlabel('Engagement Rate')\n",
    "plt.ylabel('Frequency')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2CKWxproJVXa",
   "metadata": {
    "id": "2CKWxproJVXa"
   },
   "source": [
    "**Insights\n",
    "-Mostly the of engagement rate of courses ranges between 0 & 1**\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4VITudLTb8Vz",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 569
    },
    "id": "4VITudLTb8Vz",
    "outputId": "4a8d0d63-e457-467f-d756-f6b54bf207ba"
   },
   "outputs": [],
   "source": [
    "# Univariate Analysis - Content Type Frequency\n",
    "plt.figure(figsize=(8, 6))\n",
    "sns.countplot(data=sm, x='type')\n",
    "plt.title('Content Type Distribution')\n",
    "plt.xlabel('Content Type')\n",
    "plt.ylabel('Count')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "DKzxxJNUKHHQ",
   "metadata": {
    "id": "DKzxxJNUKHHQ"
   },
   "source": [
    "**Insights - Majority of the content posted on social media is in the for of text/image form i.e Posts**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "KS7oJPw6b8Yh",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 681
    },
    "id": "KS7oJPw6b8Yh",
    "outputId": "fe417447-7078-4452-9758-b194e1c05781"
   },
   "outputs": [],
   "source": [
    "# Univariate Analysis -Course Distribution\n",
    "import numpy as np\n",
    "plt.figure(figsize=(8, 6))\n",
    "sns.countplot(data=sm, x='Course Name', order=sm['Course Name'].value_counts().index)\n",
    "plt.title('Course Distribution')\n",
    "plt.xlabel('Course Name')\n",
    "plt.xticks(rotation=45, ha='right')\n",
    "plt.ylabel('Count')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "yr48y9b6Kp4h",
   "metadata": {
    "id": "yr48y9b6Kp4h"
   },
   "source": [
    "**Insights-Content regarding Full Stack Development Courses are uploaded more**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "JYpJvC9Tb8b_",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 569
    },
    "id": "JYpJvC9Tb8b_",
    "outputId": "bfaed06a-275c-40c1-8a4a-962c34f00b24"
   },
   "outputs": [],
   "source": [
    "# Bivariate Analysis - Engagement Rate vs. Total Engagement\n",
    "plt.figure(figsize=(8, 6))\n",
    "sns.scatterplot(data=sm, x='Total Engagement', y='Engagement Rate', hue='Platform')\n",
    "plt.title('Engagement Rate vs. Total Engagement')\n",
    "plt.xlabel('Total Engagement')\n",
    "plt.ylabel('Engagement Rate')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ENR-4jXWLXho",
   "metadata": {
    "id": "ENR-4jXWLXho"
   },
   "source": [
    "**Insights- As the total engagement increases the engagement rate also increases and clustering indicates most of total engagement values are under 200 and engagement rate is under 1**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4IGZkEr1b8dw",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 569
    },
    "id": "4IGZkEr1b8dw",
    "outputId": "407d0533-7349-4f85-e64e-44065af0bb41"
   },
   "outputs": [],
   "source": [
    "# Bivariate Analysis - Likes vs. Comments by Content Type\n",
    "plt.figure(figsize=(8, 6))\n",
    "sns.scatterplot(data=sm, x='Likes', y='Comments', hue='type')\n",
    "plt.title('Likes vs. Comments by Content Type')\n",
    "plt.xlabel('Likes')\n",
    "plt.ylabel('Comments')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "_1XJFDUZQdL3",
   "metadata": {
    "id": "_1XJFDUZQdL3"
   },
   "source": [
    "**Insights- Majority of likes are more on posts and it indicates that post might have more likes but reels may get more comments**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "rwusUHQbb8ga",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 569
    },
    "id": "rwusUHQbb8ga",
    "outputId": "8a5d5c26-2847-4fae-fcb4-d4baa2ae4395"
   },
   "outputs": [],
   "source": [
    "content_type_engagement_rate = sm.groupby('type')['Engagement Rate'].mean().reset_index()\n",
    "\n",
    "plt.figure(figsize=(8, 6))\n",
    "sns.barplot(data=content_type_engagement_rate, x='type', y='Engagement Rate')\n",
    "plt.title('Average Engagement Rate by Content Type')\n",
    "plt.xlabel('Content Type')\n",
    "plt.ylabel('Average Engagement Rate')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "akD76ZFKRWI8",
   "metadata": {
    "id": "akD76ZFKRWI8"
   },
   "source": [
    "**Insights-Info about courses uploaded in video format i.e Reels may get more engagement**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "Bfhat1dUb8jQ",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 589
    },
    "id": "Bfhat1dUb8jQ",
    "outputId": "3e824cfa-6078-4159-bb81-43dcef0b1df2"
   },
   "outputs": [],
   "source": [
    "# Multivariate Analysis - Engagement Rate by Platform and Content Type\n",
    "plt.figure(figsize=(12, 6))\n",
    "sns.barplot(data=sm, x='Platform', y='Engagement Rate', hue='type')\n",
    "plt.title('Engagement Rate by Platform and Content Type')\n",
    "plt.xlabel('Platform')\n",
    "plt.ylabel('Engagement Rate')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "CBO7T39KRrwk",
   "metadata": {
    "id": "CBO7T39KRrwk"
   },
   "source": [
    "**Insights-The engagement rate for Reels is  higher than posts even though most of post and reels have engagement rate ranging between 0&1**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2-vL8xH0b8ls",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 657
    },
    "id": "2-vL8xH0b8ls",
    "outputId": "2cad42e4-152c-40ee-8a24-63b27f920309"
   },
   "outputs": [],
   "source": [
    "# Multivariate Analysis - Correlation Heatmap for Numerical Variables\n",
    "plt.figure(figsize=(10, 6))\n",
    "corr = sm[['Followers', 'Likes', 'Comments', 'Share', 'Total Engagement', 'Engagement Rate']].corr()\n",
    "sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=\".2f\")\n",
    "plt.title('Correlation Heatmap')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "_xX8D-Fmb8oC",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 589
    },
    "id": "_xX8D-Fmb8oC",
    "outputId": "bd25d281-34b5-482c-98b6-326f16093acd"
   },
   "outputs": [],
   "source": [
    "# Multivariate Analysis - Engagement Rate by courses and Content Type\n",
    "plt.figure(figsize=(12, 6))\n",
    "sns.barplot(data=sm, x='Course Name', y='Engagement Rate', hue='type')\n",
    "plt.title('Engagement Rate by Platform and Content Type')\n",
    "plt.xlabel('CourseName')\n",
    "plt.ylabel('Engagement Rate')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3yF7QkpFTEB9",
   "metadata": {
    "id": "3yF7QkpFTEB9"
   },
   "source": [
    "**Insights - Most of the courses have similiar engagement rate but few courses reels(outliers) got high engagement rate i.e reels became viral**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "QrIPSBY4b8zm",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 569
    },
    "id": "QrIPSBY4b8zm",
    "outputId": "3ff6c18b-147a-49cd-abf3-1cdd0e61074b"
   },
   "outputs": [],
   "source": [
    "# Multivariate Analysis - Total Engagement  by Likes Cmments Share and Content Type\n",
    "content_type_engagement = sm.groupby('type')[['Likes', 'Comments', 'Share', 'Total Engagement']].sum().reset_index()\n",
    "content_type_engagement = content_type_engagement.melt(id_vars='type', var_name='Metric', value_name='Total')\n",
    "\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.barplot(data=content_type_engagement, x='type', y='Total', hue='Metric')\n",
    "plt.title('Engagement by Content Type')\n",
    "plt.ylabel('Total Engagement')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2vFcFb0eTubs",
   "metadata": {
    "id": "2vFcFb0eTubs"
   },
   "source": [
    "**Insights- Likes are more on reels compared to posts indicating reels have higher total engagement**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a634b6c1-199c-4a66-9cdc-9fbe6f831c79",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 831
    },
    "id": "a634b6c1-199c-4a66-9cdc-9fbe6f831c79",
    "outputId": "ed0f5ea8-01c2-437c-c773-c8023301d8d1"
   },
   "outputs": [],
   "source": [
    "course_engagement = sm.groupby(\"Course Name\")[\"Total Engagement\"].sum().reset_index()\n",
    "course_engagement = course_engagement.sort_values(by=\"Total Engagement\", ascending=False)\n",
    "\n",
    "plt.figure(figsize=(12, 8))\n",
    "sns.barplot(x=\"Total Engagement\", y=\"Course Name\", data=course_engagement, palette=\"Blues_r\")\n",
    "plt.title(\"Most Engaging Courses\", fontsize=16)\n",
    "plt.xlabel(\"Total Engagement\", fontsize=12)\n",
    "plt.ylabel(\"Courses\", fontsize=12)\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "iVB4ldmeUCvE",
   "metadata": {
    "id": "iVB4ldmeUCvE"
   },
   "source": [
    "**Insights-Full Stack Development courses have higher total engagement**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "O5q3Yc-fNB00",
   "metadata": {
    "id": "O5q3Yc-fNB00"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "5QkinBk0UMSi",
   "metadata": {
    "id": "5QkinBk0UMSi"
   },
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cvjt1kz_NB3b",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 831
    },
    "id": "cvjt1kz_NB3b",
    "outputId": "d39bfafb-de39-40c1-9240-fce32bb43901"
   },
   "outputs": [],
   "source": [
    "institute_engagement = sm.groupby(\"Institute Name\")[\"Total Engagement\"].sum().reset_index()\n",
    "institute_engagement = institute_engagement.sort_values(by=\"Total Engagement\", ascending=False)\n",
    "\n",
    "plt.figure(figsize=(12, 8))\n",
    "sns.barplot(x=\"Total Engagement\", y=\"Institute Name\", data=institute_engagement, palette=\"magma\")\n",
    "plt.title(\"Engagement by Institutes\", fontsize=16)\n",
    "plt.xlabel(\"Total Engagement\", fontsize=12)\n",
    "plt.ylabel(\"Institutes\", fontsize=12)\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8R8tsXdcUOnx",
   "metadata": {
    "id": "8R8tsXdcUOnx"
   },
   "source": [
    "**Insights-The institute \"Naresh i Technologies\" has higher total engagement i.e Likes+Comments+Shares**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "52Ga1b8YNB6N",
   "metadata": {
    "id": "52Ga1b8YNB6N"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "FW437pNMNB8_",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 569
    },
    "id": "FW437pNMNB8_",
    "outputId": "40afebf8-0280-49ad-81d2-25d87ae0563f"
   },
   "outputs": [],
   "source": [
    "sm['Day of Week'] = sm['Date'].dt.day_name()\n",
    "day_engagement = sm.groupby('Day of Week')[['Total Engagement']].mean().reindex(\n",
    "    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']\n",
    ")\n",
    "\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.barplot(x=day_engagement.index, y=day_engagement['Total Engagement'])\n",
    "plt.title('Average Engagement by Day of the Week')\n",
    "plt.xlabel('Day of Week')\n",
    "plt.ylabel('Average Engagement')\n",
    "\n",
    "plt.show()\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "OXH6A4I9Uk01",
   "metadata": {
    "id": "OXH6A4I9Uk01"
   },
   "source": [
    "**Insights-Content posted on Wednesday have higher engagement compared to content posted on other days of the week**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "atdW4uDCNCCX",
   "metadata": {
    "id": "atdW4uDCNCCX"
   },
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "F9IU6RTsNCFD",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 653
    },
    "id": "F9IU6RTsNCFD",
    "outputId": "b6ec4470-d7a8-42df-f543-d4057c5f7d58"
   },
   "outputs": [],
   "source": [
    "classes=sm['Course Name'].value_counts().sort_values(ascending=False)[0:10]\n",
    "vals=sm['Course Name'].value_counts().sort_values(ascending=False)[0:10].values\n",
    "plt.style.use('ggplot')\n",
    "plt.figure(figsize=(8,8))\n",
    "plt.pie(x=vals,labels=classes.index,autopct=lambda p:f'{p:.2f}%,({p*sum(vals)})')\n",
    "plt.legend()\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "pED4RIUZVGcx",
   "metadata": {
    "id": "pED4RIUZVGcx"
   },
   "source": [
    "**Insights-Full Stack Develppment courses have majority share in instagram platform engagement**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38e96137-7d3f-48b2-80d3-378899026b58",
   "metadata": {},
   "outputs": [],
   "source": [
    "###### Linear Regression ########\n",
    "\n",
    "from sklearn.linear_model import LinearRegression\n",
    "\n",
    "model = Pipeline(steps=[\n",
    "    ('preprocessor', preprocessor),\n",
    "    ('regressor', LinearRegression())\n",
    "])\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "y_train_pred = model.predict(X_train)\n",
    "y_test_pred = model.predict(X_test)\n",
    "\n",
    "train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))\n",
    "test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))\n",
    "train_r2 = r2_score(y_train, y_train_pred)\n",
    "test_r2 = r2_score(y_test, y_test_pred)\n",
    "\n",
    "print(f\"Train RMSE: {train_rmse}\")\n",
    "print(f\"Test RMSE: {test_rmse}\")\n",
    "print(f\"Train R2 Score: {train_r2}\")\n",
    "print(f\"Test R2 Score: {test_r2}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7bd0c3b3-7fb5-420e-82fd-fdae25e9c3d3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fbba8063-de67-49f4-86a7-4158905283f4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "15a6782d-4e14-4def-9386-657d95968eb1",
   "metadata": {},
   "outputs": [],
   "source": [
    "###### POlynomial Regression #######\n",
    "\n",
    "from sklearn.preprocessing import PolynomialFeatures\n",
    "\n",
    "\n",
    "poly = PolynomialFeatures(degree=2, include_bias=False)\n",
    "\n",
    "model = Pipeline(steps=[\n",
    "    ('preprocessor', preprocessor),\n",
    "    ('poly', poly),\n",
    "    ('regressor', LinearRegression())\n",
    "])\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "y_train_pred = model.predict(X_train)\n",
    "y_test_pred = model.predict(X_test)\n",
    "\n",
    "train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))\n",
    "test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))\n",
    "train_r2 = r2_score(y_train, y_train_pred)\n",
    "test_r2 = r2_score(y_test, y_test_pred)\n",
    "\n",
    "print(f\"Train RMSE: {train_rmse}\")\n",
    "print(f\"Test RMSE: {test_rmse}\")\n",
    "print(f\"Train R2 Score: {train_r2}\")\n",
    "print(f\"Test R2 Score: {test_r2}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "92fce661-40b9-40dd-b9b8-0eb9555209f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "####### Lasso Regression #######\n",
    "\n",
    "from sklearn.linear_model import Lasso\n",
    "\n",
    "\n",
    "\n",
    "model = Pipeline(steps=[\n",
    "    ('preprocessor', preprocessor),\n",
    "    ('regressor', Lasso(alpha=0.1))\n",
    "])\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "y_train_pred = model.predict(X_train)\n",
    "y_test_pred = model.predict(X_test)\n",
    "\n",
    "train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))\n",
    "test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))\n",
    "train_r2 = r2_score(y_train, y_train_pred)\n",
    "test_r2 = r2_score(y_test, y_test_pred)\n",
    "\n",
    "print(f\"Train RMSE: {train_rmse}\")\n",
    "print(f\"Test RMSE: {test_rmse}\")\n",
    "print(f\"Train R2 Score: {train_r2}\")\n",
    "print(f\"Test R2 Score: {test_r2}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "79648524-07d7-4ec8-b994-fdac3f43791e",
   "metadata": {},
   "outputs": [],
   "source": [
    "####### Ridge Regression #####\n",
    "\n",
    "from sklearn.linear_model import Ridge\n",
    "\n",
    "\n",
    "model = Pipeline(steps=[\n",
    "    ('preprocessor', preprocessor),\n",
    "    ('regressor', Ridge(alpha=0.1))\n",
    "])\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "y_train_pred = model.predict(X_train)\n",
    "y_test_pred = model.predict(X_test)\n",
    "\n",
    "train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))\n",
    "test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))\n",
    "train_r2 = r2_score(y_train, y_train_pred)\n",
    "test_r2 = r2_score(y_test, y_test_pred)\n",
    "\n",
    "print(f\"Train RMSE: {train_rmse}\")\n",
    "print(f\"Test RMSE: {test_rmse}\")\n",
    "print(f\"Train R2 Score: {train_r2}\")\n",
    "print(f\"Test R2 Score: {test_r2}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c119b3c3-760c-4b66-a738-69f731a98809",
   "metadata": {},
   "outputs": [],
   "source": [
    "####### Decision Tree #########\n",
    "\n",
    "from sklearn.tree import DecisionTreeRegressor, plot_tree\n",
    "\n",
    "model = Pipeline(steps=[\n",
    "    ('preprocessor', preprocessor),\n",
    "    ('regressor', DecisionTreeRegressor(random_state=42))\n",
    "])\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "regressor = model.named_steps['regressor']\n",
    "\n",
    "y_train_pred = model.predict(X_train)\n",
    "y_test_pred = model.predict(X_test)\n",
    "\n",
    "train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))\n",
    "test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))\n",
    "train_r2 = r2_score(y_train, y_train_pred)\n",
    "test_r2 = r2_score(y_test, y_test_pred)\n",
    "\n",
    "print(f\"Train RMSE: {train_rmse}\")\n",
    "print(f\"Test RMSE: {test_rmse}\")\n",
    "print(f\"Train R2 Score: {train_r2}\")\n",
    "print(f\"Test R2 Score: {test_r2}\")\n",
    "\n",
    "tree_fig, ax = plt.subplots(figsize=(300, 50))\n",
    "plot_tree(regressor, filled=True, feature_names=numerical_features + list(model.named_steps['preprocessor'].named_transformers_['cat'].get_feature_names_out()), ax=ax)\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e43cd0e9-83f0-40e8-b6ef-653641ee8101",
   "metadata": {},
   "outputs": [],
   "source": [
    "####### XGBoost Regressor #######\n",
    "\n",
    "from xgboost import XGBRegressor\n",
    "\n",
    "model = Pipeline(steps=[\n",
    "    ('preprocessor', preprocessor),\n",
    "    ('regressor', XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42))\n",
    "])\n",
    "\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "\n",
    "y_train_pred = model.predict(X_train)\n",
    "y_test_pred = model.predict(X_test)\n",
    "\n",
    "\n",
    "train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))\n",
    "test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))\n",
    "train_r2 = r2_score(y_train, y_train_pred)\n",
    "test_r2 = r2_score(y_test, y_test_pred)\n",
    "\n",
    "print(f\"Train RMSE: {train_rmse}\")\n",
    "print(f\"Test RMSE: {test_rmse}\")\n",
    "print(f\"Train R2 Score: {train_r2}\")\n",
    "print(f\"Test R2 Score: {test_r2}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0bf8c7ec-aedb-4031-9234-1c10045f4323",
   "metadata": {},
   "outputs": [],
   "source": [
    "####### SVM #######\n",
    "\n",
    "\n",
    "from sklearn.svm import SVR\n",
    "\n",
    "model = Pipeline(steps=[\n",
    "    ('preprocessor', preprocessor),\n",
    "    ('regressor', SVR(kernel='rbf', C=1.0, epsilon=0.1))\n",
    "])\n",
    "\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "\n",
    "y_train_pred = model.predict(X_train)\n",
    "y_test_pred = model.predict(X_test)\n",
    "\n",
    "\n",
    "train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))\n",
    "test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))\n",
    "train_r2 = r2_score(y_train, y_train_pred)\n",
    "test_r2 = r2_score(y_test, y_test_pred)\n",
    "\n",
    "print(f\"Train RMSE: {train_rmse}\")\n",
    "print(f\"Test RMSE: {test_rmse}\")\n",
    "print(f\"Train R2 Score: {train_r2}\")\n",
    "print(f\"Test R2 Score: {test_r2}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "93a41080-e059-4376-9b46-1707d7ddabe3",
   "metadata": {},
   "outputs": [],
   "source": [
    "### RANDOM FOREST #####\n",
    "\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "\n",
    "model = Pipeline(steps=[\n",
    "    ('preprocessor', preprocessor),\n",
    "    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))\n",
    "])\n",
    "\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "\n",
    "y_train_pred = model.predict(X_train)\n",
    "y_test_pred = model.predict(X_test)\n",
    "\n",
    "\n",
    "train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))\n",
    "test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))\n",
    "train_r2 = r2_score(y_train, y_train_pred)\n",
    "test_r2 = r2_score(y_test, y_test_pred)\n",
    "\n",
    "print(f\"Train RMSE: {train_rmse}\")\n",
    "print(f\"Test RMSE: {test_rmse}\")\n",
    "print(f\"Train R2 Score: {train_r2}\")\n",
    "print(f\"Test R2 Score: {test_r2}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "946d4113-84a4-42c4-95b1-c5f630f23fc3",
   "metadata": {},
   "outputs": [],
   "source": [
    "#KNN Regression\n",
    "\n",
    "from sklearn.neighbors import KNeighborsRegressor\n",
    "\n",
    "model = Pipeline(steps=[\n",
    "    ('preprocessor', preprocessor),\n",
    "    ('regressor', KNeighborsRegressor(n_neighbors=5))\n",
    "])\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "y_train_pred = model.predict(X_train)\n",
    "y_test_pred = model.predict(X_test)\n",
    "\n",
    "train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))\n",
    "test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))\n",
    "train_r2 = r2_score(y_train, y_train_pred)\n",
    "test_r2 = r2_score(y_test, y_test_pred)\n",
    "\n",
    "print(f\"Train RMSE: {train_rmse}\")\n",
    "print(f\"Test RMSE: {test_rmse}\")\n",
    "print(f\"Train R2 Score: {train_r2}\")\n",
    "print(f\"Test R2 Score: {test_r2}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4067177c-6392-4599-8942-eaa69a7dde99",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# Models to evaluate\n",
    "models = {\n",
    "    'Linear Regression': LinearRegression(),\n",
    "    'Polynomial Regression': Pipeline([\n",
    "        ('poly', PolynomialFeatures(degree=2, include_bias=False)),\n",
    "        ('regressor', LinearRegression())\n",
    "    ]),\n",
    "    'Lasso Regression': Lasso(alpha=0.1),\n",
    "    'Ridge Regression': Ridge(alpha=0.1),\n",
    "    'Decision Tree': DecisionTreeRegressor(random_state=42),\n",
    "    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),\n",
    "    'Support Vector Machine': SVR(),\n",
    "    'K-Nearest Neighbors': KNeighborsRegressor(n_neighbors=5),\n",
    "    'XGBoost': XGBRegressor(objective='reg:squarederror', n_estimators=100, random_state=42)\n",
    "}\n",
    "\n",
    "results = {}\n",
    "\n",
    "# Train and evaluate models\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "for name, model in models.items():\n",
    "    pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('regressor', model)])\n",
    "    pipeline.fit(X_train, y_train)\n",
    "    \n",
    "    y_train_pred = pipeline.predict(X_train)\n",
    "    y_test_pred = pipeline.predict(X_test)\n",
    "    \n",
    "    train_r2 = r2_score(y_train, y_train_pred)\n",
    "    test_r2 = r2_score(y_test, y_test_pred)\n",
    "    \n",
    "    results[name] = {'train_r2': train_r2, 'test_r2': test_r2, 'difference': abs(train_r2 - test_r2)}\n",
    "\n",
    "# Find the best model with rules: R² (train & test) between 70-90% and difference ≤ 10%\n",
    "best_model = None\n",
    "best_r2 = 0\n",
    "for model, scores in results.items():\n",
    "    if (0.70 <= scores['train_r2'] <= 0.90 and 0.70 <= scores['test_r2'] <= 0.90 and scores['difference'] <= 0.10):\n",
    "        if scores['test_r2'] > best_r2:\n",
    "            best_model = model\n",
    "            best_r2 = scores['test_r2']\n",
    "\n",
    "print(\"Best Model within rules:\", best_model, \"with Test R² Score:\", best_r2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f758a7b2-4c18-43ec-a47c-59be26ac0e39",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "import joblib\n",
    "\n",
    "def predict_engagement(KNN):\n",
    "    followers = float(input(\"Enter number of Followers: \"))\n",
    "    likes = float(input(\"Enter number of Likes: \"))\n",
    "    comments = float(input(\"Enter number of Comments: \"))\n",
    "    shares = float(input(\"Enter number of Shares: \"))\n",
    "    total_engagement = float(likes+comments+shares)\n",
    "    print(\"Total Engagement: \", total_engagement)\n",
    "\n",
    "    course_name = input(\"Enter Course Name: \")\n",
    "    content_type = input(\"Enter Content Type: \")\n",
    "\n",
    "    input_data = pd.DataFrame([[course_name, content_type, followers, likes, comments, shares, total_engagement]],\n",
    "                              columns=['CourseName', 'type', 'Followers', 'Likes', 'Comments', 'Share', 'Total Engagement'])\n",
    "\n",
    "    predicted_engagement_rate = KNN.predict(input_data)\n",
    "\n",
    "    print(f\"Predicted Engagement Rate: {predicted_engagement_rate[0]}\")\n",
    "\n",
    "KNN = joblib.load('knn_model.pkl')\n",
    "predict_engagement(KNN)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb1b3000-a1b3-481c-9cad-71b4ba6e2488",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "03af293e-fe52-48e4-ac3f-a02251b84f8a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fa463211-466c-4dae-a1ba-b997d3d3e8cb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
