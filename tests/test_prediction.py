import pytest
import pandas as pd
from src.churn.prediction import Model
from config import Config
def test_model_load():
    model = Model(r'models\model.joblib')

def test_model_predict():
    data = {
        "Education_Level": 1,
        "Income": 50000,
        "Joining Designation": 2,
        "Grade": 3,
        "Total Business Value": 100000,
        "Quarterly Rating": 4,
        "Age": 30,
        "Gender": 1,
        "City": "C17",
        "Quarterly Rating inc": 1,
        "Age_cat": "senior",
        "joining_year": 2020,
    }
    x = pd.DataFrame(data, index=[0])
    model = Model(r'models\model.joblib')
    pred = model.predict(x)
    assert len(pred)==2
