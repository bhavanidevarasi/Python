# this prints the logs in the console
import logging
'''
#this prints the output in console , created loggers obj
logging.basicConfig(level=logging.DEBUG)
loggers = logging.getLogger()
loggers.setLevel(logging.DEBUG)

loggers.debug("just debugging")
loggers.info("juat an info statement")
loggers.warning("Giving you a warning before happening")

#this prints the logs in the console as no filepath is provided
logging.basicConfig(level=logging.DEBUG)
logging.debug("debug")
logging.warning("warning")#
#this prints if no configuration is done,
#as automatically by default it starts from warning and above
logging.info("info")
'''

#stream handlers
logger = logging.getLogger("Stream_handler")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
logger.addHandler(handler)
logger.debug("Debugging")

#file handler
log1 = logging.getLogger("File_handler")
log1.setLevel(logging.DEBUG)
hands = logging.FileHandler("app.log")
log1.addHandler(hands)
log1.debug("Im debugging")
log1.info("FYIII")
'''
logger = logging.getLogger("console_logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

log1 = logging.getLogger("file_logger")
log1.setLevel(logging.DEBUG)
log1.addHandler(logging.FileHandler("app.log"))

logger.debug("Console only")
log1.debug("File only")
'''
