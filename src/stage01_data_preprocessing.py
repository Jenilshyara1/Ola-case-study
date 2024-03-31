import logging
import pandas as pd
from sklearn.model_selection import train_test_split

logger = logging.getLogger()

STAGE_NAME = "Data Preprocessing"


class Data_preprocessing:
    def __init__(self, data_path) -> None:
        self.df = pd.read_csv(data_path)

    def preprocessing(self):
        self.df = self.df.rename(columns={"MMM-YY": "Reporting_Date"})
        # convert to datetime
        self.df["Reporting_Date"] = pd.to_datetime(self.df["Reporting_Date"])
        self.df["Dateofjoining"] = pd.to_datetime(self.df["Dateofjoining"])
        self.df["LastWorkingDate"] = pd.to_datetime(self.df["LastWorkingDate"])
        # Quarterly rating at the beginning
        qrf = self.df.groupby("Driver_ID").agg({"Quarterly Rating": "first"})

        # Quarterly rating at the end
        qrl = self.df.groupby("Driver_ID").agg({"Quarterly Rating": "last"})

        # The dataset which has the employee ids and a bollean value which tells if the rating has increased
        qr = (qrl["Quarterly Rating"] > qrf["Quarterly Rating"]).reset_index()

        qr["Quarterly Rating inc"] = qr["Quarterly Rating"].apply(
            lambda x: 1 if x else 0
        )
        self.df["target"] = (
            self.df["LastWorkingDate"].isna().apply(lambda x: 0 if x else 1)
        )
        # Aggregating the data
        grouped_df = (
            self.df.groupby("Driver_ID")
            .agg(
                {
                    "Reporting_Date": "last",
                    "Education_Level": "last",
                    "Income": "last",
                    "Dateofjoining": "last",
                    "Joining Designation": "last",
                    "Grade": "first",
                    "Total Business Value": "sum",
                    "Quarterly Rating": "last",
                    "target": "sum",
                    "Age": "last",
                    "Gender": "last",
                    "City": "last",
                }
            )
            .reset_index()
        )
        grouped_df = grouped_df.rename(
            columns={"Reporting_Date": "first_reporting_day"}
        )
        grouped_df = grouped_df.drop(columns=["Driver_ID"])
        self.df = pd.concat([grouped_df, qr["Quarterly Rating inc"]], axis=1)

    def convert_age(self, age):
        if 18 <= age <= 30:
            return "young"
        else:
            return "senior"

    def feature_engineering(self):
        self.df["Age_cat"] = self.df["Age"].apply(self.convert_age)
        self.df["joining_year"] = self.df["Dateofjoining"].dt.year
        self.df.drop(columns=["first_reporting_day", "Dateofjoining"],inplace=True)

    def main(self):
        self.preprocessing()
        self.feature_engineering()
        print(self.df)


class Data_preparation_model(Data_preprocessing):
    def __init__(self, data_path) -> None:
        super().__init__(data_path)
        super().main()

    def split_data(
        self,
    ) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        X = self.df.drop(columns=["target"])
        Y = self.df["target"]
        X_train, X_test, y_train, y_test = train_test_split(
            X, Y, test_size=0.20, stratify=Y, random_state=1
        )
        return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    try:
        logger.info(f"****************")
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
        obj = Data_preparation_model()
        X_train, X_test, y_train, y_test = obj.split_data()
        print(X_train.shape)
        print(X_test.shape)
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed<<<<<<")
    except Exception as e:
        logger.error(f'error occurred while running "{STAGE_NAME}"', exc_info=True)
