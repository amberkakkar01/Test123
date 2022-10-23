import time

import logger

log = logger.get_logger(__name__)
log_counter = 0
while(True):
    log.info(f"logging {log_counter} at {time.time()}")
    log_counter+=1
    time.sleep(1)