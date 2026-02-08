# below code is to check the logging config
from src.logger import configure_logger

logger = configure_logger()

# logger.debug("This is a debug message.")
# logger.info("This is an info message.")
# logger.warning("This is a warning message.")
# logger.error("This is an error message.")
# logger.critical("This is a critical message.")

# --------------------------------------------------------------------------------

# # below code is to check the exception config
from src.logger import configure_logger
from src.exception import MyException
import sys

try:
    a = 1+'Z'
except Exception as e:
    logger.info(e)
    raise MyException(e, sys) from e

# --------------------------------------------------------------------------------

# from src.pipline.training_pipeline import TrainPipeline

# pipline = TrainPipeline()
# pipline.run_pipeline()