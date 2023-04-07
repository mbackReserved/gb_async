b_words = ['attrubute', 'класс', 'функция', 'standard']

def str_to_byte(array):
    for i in array:
        try:
            print(bytes(i, 'ascii'))
        except UnicodeEncodeError:
            print(f'Строку "{i}" невозможно записать в байтовом типе')
    return array

str_to_byte(b_words)