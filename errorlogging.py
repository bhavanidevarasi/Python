import logging
logging.basicConfig(filename = "app.log", level=logging.DEBUG)
try:
    div = 10/0
except Exception as e:
    logging.debug(e)
    logging.error(e)
#to log full traceback
try:
     n =int(input())
     reyl = 10/n
except Exception as e:
    logging.error("This may show error",e)
    #logging.exception("Miss Calculation")
