bwords = [b'class', b'function', b'method']

def get_info(array):
    for i in array:
        print(f'Содержимое: {i}, тип: {type(i)}, длина: {len(i)}')
    return array

get_info(bwords)