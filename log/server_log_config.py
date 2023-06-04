import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger('server_logger')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(message)s')
file_handler = TimedRotatingFileHandler('log/server_log/server.log', when='midnight', backupCount=5)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
