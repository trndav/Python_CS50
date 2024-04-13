import logging
import logging.config 
logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simpleExample')
logger.debug('this is debug message')

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

# # 5 log levels, debug, info, warning, error, critical
# # logging.debug("This is debug message")
# # logging.info("This is info message")
# # logging.warning("This is warning message")
# # logging.error("This is error message")
# # logging.critical("This is critical message")

# import helper11
# *******************

# logger = logging.getLogger(__name__)
# stream_handler = logging.StreamHandler()
# file_h = logging.FileHandler('file.log')
# # Level and format
# stream_handler.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)
# formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# stream_handler.setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_handler)
# logger.addHandler(file_h)
# logger.warning('This is a warning')
# logger.error('This is an error')