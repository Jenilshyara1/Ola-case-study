import logging
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import MinMaxScaler
import joblib


logger = logging.getLogger()
STAGE_NAME = "Model Training"


class Model_training:
    def __init__(self, X_train, y_train, model_path) -> None:
        self.X_train = X_train
        self.y_train = y_train
        self.model = None
        self.ohe_col = ["City", "Age_cat"]
        self.model_path = model_path

    def training(self):
        col_transformer = make_column_transformer(
            (OneHotEncoder(drop="first", sparse_output=False), self.ohe_col),
            remainder="passthrough",
        )
        self.model = make_pipeline(
            col_transformer,
            MinMaxScaler(),
            RandomForestClassifier(
                class_weight="balanced_subsample",
                max_depth=60,
                max_features="sqrt",
                min_samples_split=2,
                n_estimators=150,
                random_state=1
            ),
        )
        self.model.fit(self.X_train, self.y_train)

    def save_model(self):
        joblib.dump(self.model, self.model_path)

    def main(self):
        self.training()
        self.save_model()
