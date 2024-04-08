import pytest
import pandas as pd
from src.churn.stage01_data_preprocessing import Data_preprocessing, Data_preparation_model

def test_Data_preprocessing():
    data = Data_preprocessing(data_path="data/Ola.csv")
    
    data.preprocessing()
    assert isinstance(data.df, pd.DataFrame), "data.df should be a DataFrame"
    
    data.feature_engineering()
    assert "Age_cat" in data.df.columns, "Age_cat column should be in the DataFrame"
    assert "joining_year" in data.df.columns, "joining_year column should be in the DataFrame"

def test_Data_preparation_model():
    data = Data_preparation_model(data_path="data/Ola.csv")
    X_train, X_test, y_train, y_test = data.split_data()
    assert isinstance(X_train, pd.DataFrame), "X_train should be a DataFrame"
    assert isinstance(X_test, pd.DataFrame), "X_test should be a DataFrame"
    assert isinstance(y_train, pd.Series), "y_train should be a Series"
    assert isinstance(y_test, pd.Series), "y_test should be a Series"

