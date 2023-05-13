import logging
import logs.client_log
import logs.server_log
import sys
import inspect


print(sys.argv[0].find('client'))

if sys.argv[0].find('client') == -1:
    logger = logging.getLogger('server_log')
else:
    logger = logging.getLogger('client_log')


def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.debug(f'Зафиксировано обращение к функции {func.__name__} . Аргументы функции: {args}, {kwargs}.')
        mainf = inspect.stack()[1][3]
        if mainf != '<module>':
            logger.debug(f'Вызов осуществлен из функции {mainf}')
        return result
    return wrapper