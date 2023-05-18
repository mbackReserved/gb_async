import subprocess

procs_list = []


while True:
    mode = input('Чтобы запустить сервер и  клиентов, введите "start", чтобы закрыть - "kill"')

    if mode == 'start':
        procs_list.append(subprocess.Popen('python3 server.py', shell=True))
        count_of_client = int(input('Укажите количество клиентов'))

        for i in range(1, count_of_client+1):
            procs_list.append(subprocess.Popen(f'python3 client_listener.py', shell=True))
    
    elif mode == 'kill':
        while procs_list:
            to_kill = procs_list.pop()
            to_kill.kill()

        break
