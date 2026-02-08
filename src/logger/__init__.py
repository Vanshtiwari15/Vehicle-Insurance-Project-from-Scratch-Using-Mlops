import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime
from from_root import from_root

LOG_DIR = "logs"
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5 * 1024 * 1024
BACKUP_COUNT = 3

def configure_logger():
    logger = logging.getLogger("vehicle_insurance")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    logger.handlers.clear()

    log_dir_path = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_dir_path, exist_ok=True)

    log_file_path = os.path.join(log_dir_path, LOG_FILE)

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s | %(filename)s:%(lineno)d | %(message)s"
    )

    file_handler = RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # change to DEBUG if needed
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger