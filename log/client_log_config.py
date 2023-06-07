import logging
from logging.handlers import TimedRotatingFileHandler
import inspect


logger = logging.getLogger('client_logger')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(message)s')
file_handler = TimedRotatingFileHandler('log/client_log/client.log', when='midnight', backupCount=5)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def log(func):
    def wrapper(*args, **kwargs):
        calling_frame = inspect.currentframe().f_back
        calling_filename = calling_frame.f_code.co_filename
        if calling_filename.endswith('.py'):
            calling_filename = calling_filename[:-3]
        logger.info("Function %s() called from function %s", func.__name__, calling_filename)
        return func(*args, **kwargs)
    return wrapper
