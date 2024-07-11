import pytest
from config import Config
from src.churn.stage01_data_preprocessing import DataPreparationModel
obj = DataPreparationModel(data_path=Config.DATA_PATH)
X_train, X_test, y_train, y_test = obj.split_data()

from src.churn.stage02_model_training import ModelTraining

def test_training():
    model = ModelTraining(X_train,y_train,Config.MODEL_PATH)
    model.training()
    