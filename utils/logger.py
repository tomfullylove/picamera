import logging

from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler(
    "/home/picamera/app.log",
    maxBytes=1000000,
    backupCount=3
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[handler, logging.StreamHandler()]
)

logger = logging.getLogger("Logger")
