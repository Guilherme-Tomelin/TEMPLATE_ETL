# src/configs/logger_settings.py

import logging
import os


class LoggerConfig:
    def __init__(
        self,
        log_level=logging.INFO,
        console_level=logging.DEBUG,
        log_format="[%(asctime)s] - %(levelname)s - %(message)s",
        datefmt="%d/%m/%Y - %H:%M:%S",
        log_file=None,
    ):

        # Remove handlers antigos
        root_logger = logging.getLogger()
        for handler in root_logger.handlers[:]:
            root_logger.removeHandler(handler)

        formatter = logging.Formatter(log_format, datefmt)

        # Configura o console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(console_level)
        console_handler.setFormatter(formatter)
        root_logger.addHandler(console_handler)

        # Configura o file handler, se necessário
        if log_file:
            log_dir = os.path.join(os.getcwd(), "logs")
            os.makedirs(log_dir, exist_ok=True)
            log_file_path = os.path.join(log_dir, "app.log")

            file_handler = logging.FileHandler(log_file_path, mode="a")
            file_handler.setLevel(log_level)
            file_handler.setFormatter(formatter)
            root_logger.addHandler(file_handler)

        # Define o nível base do logger
        root_logger.setLevel(min(log_level, console_level))
