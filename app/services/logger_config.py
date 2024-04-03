from logging.handlers import RotatingFileHandler
import logging

# Create a rotating file handler that will log to app.log, keep 5 old log files, and each file will have a maximum size of 1MB
handler = RotatingFileHandler("app.log", maxBytes=1000000, backupCount=5)

# Create a logger and set its level to ERROR
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

formatter = logging.Formatter(
    "%(asctime)s - %(module)s - %(name)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)
