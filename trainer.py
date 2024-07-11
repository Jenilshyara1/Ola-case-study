from setup_logger import init_logger
import logging
from src.churn.stage01_data_preprocessing import DataPreparationModel
from src.churn.stage02_model_training import ModelTraining
from src.churn.stage03_model_evaluation import ModelEvaluation
from config import Config

# Initialize the logger
init_logger()
logger = logging.getLogger()


def run_stage(stage_name, stage_func):
    """Runs a stage and logs the start and end, as well as any errors."""
    try:
        logger.info("****************")
        logger.info(f">>>>> Stage {stage_name} started <<<<<<<<<<<<")
        stage_func()
        logger.info(f">>>>>>>>>> Stage {stage_name} completed <<<<<<<<<<<<")
    except Exception as e:
        logger.error(f'Error occurred while running "{stage_name}"', exc_info=True)
        raise


def data_preprocessing_stage():
    obj = DataPreparationModel(data_path=Config.DATA_PATH)
    global X_train, X_test, y_train, y_test
    X_train, X_test, y_train, y_test = obj.split_data()
    logger.debug(f"X_train shape: {X_train.shape}, X_test shape: {X_test.shape}")


def model_training_stage():
    obj = ModelTraining(X_train, y_train, Config.MODEL_PATH)
    obj.main()
    global model
    model = obj.model


def model_evaluation_stage():
    obj = ModelEvaluation(
        model,
        X_test,
        y_test,
        Config.CLASSIFICATION_REPORT_PATH,
        Config.CONFUSION_MATRIX_PATH,
        Config.PRECISION_RECALL_CURVE_PATH,
        Config.ROC_AUC_CURVE_PATH,
    )
    obj.evaluate()


if __name__ == "__main__":
    run_stage("Data Preprocessing", data_preprocessing_stage)
    run_stage("Model Training", model_training_stage)
    run_stage("Model Evaluation", model_evaluation_stage)
