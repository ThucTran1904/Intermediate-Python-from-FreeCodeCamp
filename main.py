import logging
import logging.config
import traceback

# logging.config.fileConfig('logging.conf')

# logger = logging.getLogger('SimpleExample')
# logger.debug('This is a debug message')
# logger.propagate = False
# logger.info('Hello from helper')

# # Create handler
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler('file.log')

# # Level and the format 
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning('This is a warning ')
# logger.error('This is an error')

try: 
    a = [1,2,3]
    val = a[4]
except IndexError as e:
    logging.error("The error is %s",  traceback.format_exc()  ) 
    