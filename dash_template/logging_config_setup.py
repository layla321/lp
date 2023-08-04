""" Setting up loggers with a config dict """
import logging

from logging_conf import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)

# Create logger
logger = logging.getLogger("file")

# Use logger
logger.info("testing conf file")
