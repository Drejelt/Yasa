import logging

logging.basicConfig(level=logging.DEBUG, filename='logs.txt', format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]', datefmt='%d/%m/%Y %I:%M:%S',
                    encoding = 'utf-8')

class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

        logging.error(msg)

try:
    raise CustomException("Проверочное сообщение об ошибке.")
except CustomException as e:
    print("Произошла ошибка:", e)