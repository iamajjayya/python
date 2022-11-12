# # # #logging
# # # import logging
# # #
# # # logging.basicConfig(
# # #     filename="help.txt",
# # #     filemode="a",
# # #     format='%(asctime)s %(levelname)s-%(message)s',
# # #     datefmt='%Y-%m-%d %H:%M:%S'
# # # )
# # # logging.debug("This is debug message")
# # # logging.info("This is info message")
# # # logging.error("This is error message")
# # # logging.warning("This is warning message")
# # # logging.critical("This is critical message")
# # #
# # # try:
# # #     i=10
# # #     i=i/0
# # # except:
# # # logging.error("Division By error")
# #
# # import  logging
# #
# # logger = logging.getLogger(__name__)
# # #create handler
# # stream_h =logging.StreamHandler()
# # file_h =logging.FileHandler('file.log')
# #
# # #level and  format
# # stream_h.setLevel(logging.WARNING)
# # file_h.setLevel(logging.ERROR)
# #
# #
# # formatter =  logging.Formatter('%(asctime)s %(levelname)s-%(message)s')
# # file_h.setFormatter(formatter)
# # stream_h.setFormatter(formatter)
# #
# #
# # logger.addHandler(stream_h)
# # logger.addHandler(file_h)
# # logger.warning("This is waring")
# # logger.error("This is Error")
# #
# import logging
# try:
#     a=[1,2,3]
#     val=a[4]
# except IndexError as e:
#     logging.error(e , exc_info=True)
import  logging
from logging.handlers  import  RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info("Hello Python..")