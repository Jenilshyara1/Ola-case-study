from src.setup_logger import init_logger
import logging
from src.stage01_data_preprocessing import Data_preparation_model
from src.stage02_model_training import Model_training
from src.stage03_model_evaluation import Model_evaluation
from config import Config

logger = logging.getLogger()
init_logger()
STAGE_NAME = "Data Preprocessing"

try:
    logger.info(f"****************")
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    obj = Data_preparation_model(data_path=Config.DATA_PATH)
    X_train, X_test, y_train, y_test = obj.split_data()
    print(X_train.shape)
    print(X_test.shape)
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed<<<<<<")
except Exception as e:
    logger.error(f'error occurred while running "{STAGE_NAME}"', exc_info=True)

STAGE_NAME = "Model Training"

try:
    logger.info(f"****************")
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    obj = Model_training(X_train, y_train, Config.MODEL_PATH)
    obj.main()
    model = obj.model
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed<<<<<<")
except Exception as e:
    logger.error(f'error occurred while running "{STAGE_NAME}"', exc_info=True)

STAGE_NAME = "Model evaluation"

try:
    logger.info(f"****************")
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    obj = Model_evaluation(
        model,
        X_test,
        y_test,
        Config.CLASSIFICATION_REPORT_PATH,
        Config.CONFUSION_MATRIX_PATH,
        Config.PRECISION_RECALL_CURVE_PATH,
        Config.ROC_AUC_CURVE_PATH,
    )
    obj.evaluate()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed<<<<<<")
except Exception as e:
    logger.error(f'error occurred while running "{STAGE_NAME}"', exc_info=True)
