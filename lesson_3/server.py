from socket import *
import sys
import json
import time


def main():

    try:
        if '-p' in sys.argv and '-a' in sys.argv:
            srv_port = int(sys.argv[sys.argv.index('-p') + 1])
            srv_ip = sys.argv[sys.argv.index('-a') + 1]
        else:
            srv_ip = '127.0.0.1'
            srv_port = 7777
            print(f'Некорректно указаны порт и адрес. Присвоены стандартные значения. \n Порт: {srv_port}\n, IP-адрес: {srv_ip}')
    except IndexError:
        print('Укажите адрес и порт в виде: "-p 7777 -a 127.0.0.1"')
        sys.exit(1)
    
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((srv_ip, srv_port))
    sock.listen(5)
    print('Сервер ожидает подключения')

    while True:
        client, addr = sock.accept()
        data = client.recv(100000)
        dec_data = data.decode('utf-8')
        js_data = json.loads(dec_data)
        print(f'Сервер принял сообщение: \n {js_data}')
        if 'action' in js_data and js_data['action'] == 'presence' and 'time' in js_data:
            if 'account_name' in js_data['user']:
                account_name = js_data['user']['account_name']
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
        

        try:
            js_response = json.dumps(srv_response)
            enc_response = js_response.encode('utf-8')
            client.send(enc_response)
            print('Сервер отправил сообщение клиненту')
            client.close()
            print('Сервер ожидает следующего подключения')
        except (ValueError, json.JSONDecodeError):
            print('Принято некорретное сообщение от клиента.')
            client.close()




if __name__ == '__main__':
    main()