from socket import *
import sys
import json
import time
import logging
import logs.server_log
import select
from decorators import log


server_logger = logging.getLogger('server_log')


@log
def create_response_to_client(msg_from_client):
    if 'action' in msg_from_client and msg_from_client['action'] == 'presence' and 'time' in msg_from_client:
        if 'mes' in msg_from_client:
            mes = msg_from_client['mes']
            message = f'Message from another client to server: {mes}'
        elif 'account_name' in msg_from_client['user']:
            account_name = msg_from_client['user']['account_name']
            message = f'Hello from server, {account_name}'
        else:
            message = 'Dear Guest, welcome to the server!'

        srv_response = {
            'response': 200,
            'time': time.ctime(time.time()),
            'message': message
        }
    else:
        srv_response = {
            'response': 400,
            'error': 'Bad request',
            'time': time.ctime(time.time()),
            'message': 'Сервер получил некорректные данные'
        }
    return srv_response


def main():

    print(sys.argv)
    try:
        if '-p' in sys.argv and '-a' in sys.argv:
            srv_port = int(sys.argv[sys.argv.index('-p') + 1])
            srv_ip = sys.argv[sys.argv.index('-a') + 1]
            server_logger.info(f'Сервер запущен {srv_ip} : {srv_port}')
        else:
            srv_ip = '127.0.0.1'
            srv_port = 7777
            # print(f'Некорректно указаны порт и адрес. Присвоены стандартные значения. \n Порт: {srv_port}\n, IP-адрес: {srv_ip}')
            server_logger.error(f'Некорректно указаны порт и адрес. Присвоены стандартные значения. \n Порт: {srv_port}\n, IP-адрес: {srv_ip}')
    except IndexError:
        # print('Укажите адрес и порт в виде: "-p 7777 -a 127.0.0.1"')
        server_logger.error('Укажите адрес и порт в виде: "-p 7777 -a 127.0.0.1"')
        sys.exit(1)
    
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((srv_ip, srv_port))
    sock.settimeout(0.2)

    clients_list = []
    messages_list = []

    sock.listen(5)
    # print('Сервер ожидает подключения')
    server_logger.debug('Сервер ожидает подключения')

    
    while True:
        try:
            client, addr = sock.accept()
        except OSError:
            pass
        else:
            clients_list.append(client)
        
        to_read_list = []
        to_send_list = []
        errors_list = []

        try:
            if clients_list:
                to_read_list, to_send_list, errors_list = select.select(clients_list, clients_list, [], 0)
        except OSError:
            pass


        if to_read_list:
            for read_client in to_read_list:
                try:
                    data = client.recv(100000)
                    dec_data = data.decode('utf-8')
                    js_data = json.loads(dec_data)
                    messages_list.append(create_response_to_client(js_data))
                except:
                    clients_list.remove(read_client)
        
        if messages_list and to_send_list:
            message = {
                'message': messages_list[0]['message'],
                'response': messages_list[0]['response'],
                'time': time.time(),
            }
            del messages_list[0]
            for waiting_client in to_send_list:
                try:
                    js_response = json.dumps(message)
                    enc_response = js_response.encode('utf-8')
                    waiting_client.send(enc_response)
                except:
                    clients_list.remove(waiting_client)


if __name__ == '__main__':
    main()