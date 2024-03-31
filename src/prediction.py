import joblib
import pandas as pd


class Model:
    def __init__(self, model_path) -> None:
        self.model = joblib.load(model_path)

    def prediction(self, x: pd.DataFrame):
        return self.model.predict(x),self.model.predict_proba(x)

