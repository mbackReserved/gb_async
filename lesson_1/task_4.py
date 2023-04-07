words = ['разработка', 'администрирования', 'protocol', 'standard']

def encode_decode(array):
    for i in array:
        i = i.encode('utf-8')
        print(i, type(i))
        i = i.decode('utf-8')
        print(i, type(i), '\n')
    return array

encode_decode(words)