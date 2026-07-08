import logging
import os

class CustomLogger:
    @staticmethod
    def get_logger():
        if not os.path.exists("Logs"):
            os.makedirs("Logs")
            
        logger = logging.getLogger("FullStackFramework")
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            
            # File Handler
            file_handler = logging.FileHandler("Logs/automation_run.log", mode="a")
            formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            
            # Console Handler
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)
            
        return logger