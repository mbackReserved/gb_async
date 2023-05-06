import logging
import logs.client_log
import logs.server_log
import sys


if sys.argv[0].find('client') == -1:
    logger = logging.getLogger('server_log')
else:
    logger = logging.getLogger('client-log')


def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.debug(f'Зафиксировано обращение к функции {func.__name__} . Аргументы функции: {args}, {kwargs} ')
        return result
    return wrapper