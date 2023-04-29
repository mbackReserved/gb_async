from socket import *
import sys
import json
import time


def resp_from_server(srv_resp):
    try:   
        msg = srv_resp['message']
        status_code = srv_resp['response']
        print(f'Получено сообщение от сервера: "{msg}"')
    except KeyError:
         error = 'Не получены необходимые данные от сервера'
         print(error)
         return error
    return status_code


def main():
    try:
        srv_ip = sys.argv[1]
        srv_port = int(sys.argv[2])
    except TypeError:
            srv_ip = '127.0.0.1'
            srv_port = 7777
            print(f'Некорректно указаны порт и адрес. Присвоены стандартные значения. \n Порт: {srv_port}\n, IP-адрес: {srv_ip}')
    
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((srv_ip, srv_port))
    print('Соединение с сервером установлено')
    

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


    try:
        data = sock.recv(100000)
        dec_data = data.decode('utf-8')
        js_data = json.loads(dec_data)
        resp_from_server(js_data)

    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()

