"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet
"""

import subprocess
import chardet


def ping(url):
    ARGS = ['ping']
    ARGS.append(url)
    PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
    for line in PING.stdout:
        result = chardet.detect(line)
        print(result)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
    return url

ping('yandex.ru')
ping('youtube.com')