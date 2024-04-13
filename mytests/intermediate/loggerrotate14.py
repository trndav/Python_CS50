# TimedRotatingFileHandler

import logging 
from logging.handlers import TimedRotatingFileHandler 
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# s, m, h, d, midnight, 
handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for i in range(5):
    logger.info(f'{i}. Hi world!')
    time.sleep(5)