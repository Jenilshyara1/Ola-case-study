import joblib
import pandas as pd


class Model:
    def __init__(self, model_path:str) -> None:
        self.model = joblib.load(model_path)

    def predict(self, x: pd.DataFrame):
        return self.model.predict(x),self.model.predict_proba(x)

