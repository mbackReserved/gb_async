import logging


client_formatter = logging.Formatter('%asctime)s %(levelname)s %(module)s %(message)s')
file_handler = logging.FileHandler('client.log')

client_logger = logging.getLogger('client_log')
client_logger.addHandler(file_handler)
client_logger.setLevel(logging.INFO)


if __name__ == '__main__':
    client_logger.critical('Критическая ошибка')
    client_logger.error('Ошибка')
    client_logger.warning('Предупреждение')
    client_logger.info('Информационное сообщение')
    client_logger.debug('Отладочная информация')
