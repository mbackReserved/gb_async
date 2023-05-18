import ipaddress
from task1 import host_ping


def host_range_ping():
    while True:
        first_address = input('Укажите начальный адрес: ')
        try:
            last_oct = int(first_address.split('.')[3])
            break
        except Exception as error:
            print(error)
    while True:
        last_ip = input('Укажите число адресов для проверки: ')
        if (last_oct+int(last_ip)) > 254:
            print(f"Заданное кол-во адресов для проверки выходит за границы последнего октета.")
        else:
            break

    ip_addrs = []
    [ip_addrs.append(str(ipaddress.ip_address(first_address)+x)) for x in range(int(last_ip))]
    return host_ping(ip_addrs)


if __name__== "__main__":
    host_range_ping()