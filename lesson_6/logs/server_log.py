import logging
import logging.handlers
import sys


server_formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(message)s')
time_rotate_file_handler = logging.handlers.TimedRotatingFileHandler('server.log', encoding='utf8', interval=1, when='D')
time_rotate_file_handler.setFormatter(server_formatter)
stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setFormatter(server_formatter)
stream_handler.setLevel(logging.ERROR)


server_logger = logging.getLogger('server_log')
server_logger.addHandler(time_rotate_file_handler)
server_logger.addHandler(stream_handler)
server_logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    server_logger.critical('Критическая ошибка')
    server_logger.error('Ошибка')
    server_logger.warning('Предупреждение')
    server_logger.info('Информационное сообщение')
    server_logger.debug('Отладочная информация')
