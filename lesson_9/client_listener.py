from socket import *
import sys
import json
import time
import logging
import logs.client_log
import threading
from decorators import log

client_logger = logging.getLogger('client_log')


@log
def resp_from_server(sock):
    while True:
        try:
            data = sock.recv(100000)
            dec_data = data.decode('utf-8')
            srv_resp = json.loads(dec_data)
            msg = srv_resp['message']
            status_code = srv_resp['response']
            print(f'Получено сообщение от сервера: "{msg}"')
            client_logger.debug(f'Получено сообщение от сервера: "{msg}"')

        except KeyError:
            error = 'Не получены необходимые данные от сервера'
            print(error)
            client_logger.error(error)
            return error



def send_message_to_server(sock):
    msg_to_srv = {
        'action': 'presence',
        'time': time.ctime(time.time()),
        'user': {
            'account_name': 'Vadim'
        }
    }

    msg_to_srv = json.dumps(msg_to_srv)
    msg_to_srv = msg_to_srv.encode('utf-8')
    sock.send(msg_to_srv)
    #data = sock.recv(100000)

    #return data



@log
def main():
    try:
        srv_ip = sys.argv[1]
        srv_port = int(sys.argv[2])
        client_logger.debug(f'Клиент запущен {srv_ip} : {srv_port}')
    except (TypeError, IndexError):
            srv_ip = '127.0.0.1'
            srv_port = 7777
            # print(f'Некорректно указаны порт и адрес. Присвоены стандартные значения. \n Порт: {srv_port}\n, IP-адрес: {srv_ip}')
            client_logger.error(f'Некорректно указаны порт и адрес. Присвоены стандартные значения. \n Порт: {srv_port}\n, IP-адрес: {srv_ip}')
    
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((srv_ip, srv_port))
    # print('Соединение с сервером установлено')
    client_logger.info('Соединение с сервером установлено')


    try:
        send_message_to_server(sock)
        resp_from_server(sock)
    except:
        sys.exit(1)
    
    else:
        receiver = threading.Thread(target=resp_from_server, args=(sock, ), daemon=True)
        receiver.start()

        while True:
            time.sleep(1)
            if receiver.is_alive():
                continue
            break


if __name__ == '__main__':
    main()

