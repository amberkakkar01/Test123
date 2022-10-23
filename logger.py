import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler
import datetime

FORMATTER = logging.Formatter("%(asctime)s %(levelname)s %(name)s:%(lineno)d - %(message)s")
LOG_DIR = "/home/umaid/Documents/logs_tester_v1"
LOG_FILE = LOG_DIR + "/console.log"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler():
    rotation_time = datetime.datetime.strptime('04:00','%H:%M').time()
    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight',atTime=rotation_time,interval=1)
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.propagate = False
    return logger
