import ipaddress
import subprocess


def host_ping(ip_array):
    for ip in ip_array:
        try:
            ip_address = ipaddress.ip_address(ip)
        except ValueError:
            print(f'{ip} нельзя преобразовать с помощью ip_address')
        new_proc = subprocess.call(['ping', '-c', '2', ip], shell=False, stdout=subprocess.PIPE)
        if new_proc:
            print(f'{ip} - Узел недоступен')
        else:
            print(f'{ip} - Узел доступен')
        

if __name__ == '__main__':
    ip_addrs = ['youtube.com', 'gb.ru', '16.10.24.154', '192.168.1.5']
    host_ping(ip_addrs)