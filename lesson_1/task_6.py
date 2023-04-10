lines = ['сетевое программирование', 'сокет', 'декоратор']
newfile = 'test_file.txt'


with open(newfile, 'w', encoding='cp1251') as file:
    for line in lines:
        file.write(f'{line} \n')
    default_encoding = file.encoding
    print(f'Первоначальная кодировка файла {default_encoding} \n')


with open(newfile, encoding='utf-8') as file:
    try:
        for line in file:
            print(line)
    except UnicodeDecodeError:
        print(f'Файл, изначально закодированный в {default_encoding} не может быть прочитан в utf-8 \n')


def read_by_line_utf8(filename):
    #Построчное кодирование/декодирование файла, для чтения в формате Unicode
    with open(filename) as file:
        for line in file:
            line = line.decode(default_encoding).encode('utf-8')
            line = line.decode('utf-8')
            print(line)
    return filename

read_by_line_utf8(newfile)