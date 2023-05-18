import tabulate
from task2 import host_range_ping

def host_range_ping_tab():
    res = host_range_ping()
    print(tabulate.tabulate([res], headers='keys', tablefmt='pipe', stralign='center'))


if __name__ == '__main__':
    host_range_ping_tab()