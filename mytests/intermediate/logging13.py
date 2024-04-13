# RotatingFileHandler

import logging 
from logging.handlers import RotatingFileHandler 

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = RotatingFileHandler('app.log', maxBytes=200, backupCount=5)
logger.addHandler(handler)

for i in range(100):
    logger.info(f'{i}. Hi world!')