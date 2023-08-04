""" Setting up loggers one step at a time """
import logging

file_logger = logging.getLogger(__name__)
stream_logger = logging.getLogger(__name__)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s")

file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

file_logger.addHandler(file_handler)

file_logger.info("Info log entry")
