import logging
from logging.handlers import RotatingFileHandler


logger = logging.getLogger('client_logger')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(message)s')
file_handler = RotatingFileHandler('log/client_log/client.log', maxBytes=1024, backupCount=5)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
