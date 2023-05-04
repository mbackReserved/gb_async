import logging


server_formatter = logging.Formatter('%asctime)s %(levelname)s %(module)s %(message)s')
time_rotate_file_handler = logging.handlers.TimedRotatingFileHandler('server.log', encoding='utf8', interval=1, when='D')

server_logger = logging.getLogger('client_log')
server_logger.addHandler(time_rotate_file_handler)
server_logger.setLevel(logging.INFO)


if __name__ == '__main__':
    server_logger.critical('Критическая ошибка')
    server_logger.error('Ошибка')
    server_logger.warning('Предупреждение')
    server_logger.info('Информационное сообщение')
    server_logger.debug('Отладочная информация')
