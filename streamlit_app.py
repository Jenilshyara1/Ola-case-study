import streamlit as st
import requests
import json
st.title("Streamlit App")
Education_Level = st.selectbox(
    "Education Level", ("0", "1", "2"), placeholder="Select Education Level..."
)
Income = st.text_input("Income",placeholder='Enter your income..')

Joining_Designation = st.selectbox(
    "Joining Designation", ("1", "2", "3","4","5"), placeholder="Select Joining Designation..."
)
Grade = st.selectbox(
    "Grade", ("1", "2", "3","4","5"), placeholder="Select Grade..."
)
Total_Business_Value = st.text_input('Total Business Value',placeholder='Enter Total Business Value')

Quarterly_Rating = st.selectbox(
    "Quarterly Rating", ("1", "2", "3","4"), placeholder="Select Quarterly Rating..."
)
Age = st.text_input('Age',placeholder='Enter Age..')
Gender = st.selectbox(
    "Gender", ("Male","Female"), placeholder="Select Gender..."
)
if Gender=="Male":
    Gender=0
else:
    Gender=1
City = "C14"
Quarterly_Rating_inc = st.selectbox(
    "Quarterly Rating inc", ("0","1"), placeholder="Select Quarterly Rating inc..."
)
Age_cat = st.selectbox(
    "Age cat", ("young","senior"), placeholder="Select age cat..."
)
joining_year = st.selectbox(
    "joining year", ("2020","2019"), placeholder="Select joining year..."
)

if st.button("Submit"):
    data = {
        "Education_Level": Education_Level,
        "Income": Income,
        "Joining_Designation": Joining_Designation,
        "Grade": Grade,
        "Total_Business_Value": Total_Business_Value,
        "Quarterly_Rating": Quarterly_Rating,
        "Age": Age,
        "Gender": Gender,
        "City": City,
        "Quarterly_Rating_inc": Quarterly_Rating_inc,
        "Age_cat": Age_cat,
        "joining_year": joining_year,
    }
    response = requests.post('http://127.0.0.1:8000/prediction',json=data).json()
    res = json.loads(response)
    st.write("output:", (res['output']))
    st.write("output_proba:", (res['output_proba']))
