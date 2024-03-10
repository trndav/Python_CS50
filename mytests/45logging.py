# https://www.youtube.com/watch?v=AU9pI0yIEWw

# DEBUG INFO WARNING ERROR CRITICAL
# See only highest logging message

import logging

logging.basicConfig(level=logging.INFO) # Set logging level

# logging.info("You have 20 emails in inbox!")
# logging.critical("All components fail!")

logger = logging.getLogger("NeuralNine Logger") # Name of logger
logger.setLevel(logging.DEBUG)

# logger.info("The best logger!")
# logger.critical("Critical logger message!")
# logger.log(logging.ERROR, "An error occured")

handler = logging.FileHandler("mylog.log")
handler.setLevel(logging.INFO)

# Add additional info to logger
formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.debug("This is a debug message!")
logger.info("Important message")