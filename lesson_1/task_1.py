words = ['разработка', 'сокет', 'декоратор']

def get_type(array):
    for i in array:
        print(i, type(i))
    return array

get_type(words)

words_unicode = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', '\u0441\u043e\u043a\u0435\u0442', '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']

get_type(words_unicode)