from api import app, Data
from fastapi.testclient import TestClient
import pytest

client = TestClient(app)


def test_prediction():
    payload = {
        "Education_Level": 1,
        "Income": 50000,
        "Joining_Designation": 2,
        "Grade": 3,
        "Total_Business_Value": 100000,
        "Quarterly_Rating": 4,
        "Age": 30,
        "Gender": 1,
        "City": "C17",
        "Quarterly_Rating_inc": 1,
        "Age_cat": "senior",
        "joining_year": 2020,
    }

    response = client.post("/prediction", json=payload)
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    data = response.json()
    assert "output" in data
    assert "output_proba" in data
