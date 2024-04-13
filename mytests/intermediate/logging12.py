import logging 
# try:
#     a = [1, 2, 3]
#     val = a[4]
# except IndexError as e:
#     # logging.error(e)
#     logging.error(e, exc_info=True) # Gives more error info in prompt

# If we dont know what error wil lappear:import logging 
import traceback
try:
    a = [1, 2, 3]
    val = a[4]
except:
    # logging.error(e)
    logging.error("The error is %s", traceback.format_exc()) 