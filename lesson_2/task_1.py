import os
import re
import csv


def get_data():
    os_prod_list, os_name_list, os_code_list, os_type_list = (list() for _ in range(4))
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for file in os.listdir(path='.'):
        if re.search('.txt', file):
            with open(file, encoding='cp1251') as f:
                for line in f:
                    if re.match('Изготовитель системы:', line):
                        os_prod_list.append(re.split('Изготовитель системы:', line)[1].lstrip().rstrip())
                    elif re.match('Название ОС:', line):
                        os_name_list.append(re.split('Название ОС:', line)[1].lstrip().rstrip())
                    elif re.match('Код продукта:', line):
                        os_code_list.append(re.split('Код продукта:', line)[1].lstrip().rstrip())
                    elif re.match('Тип системы:', line):
                        os_type_list.append(re.split('Тип системы:', line)[1].lstrip().rstrip())
            values_list = [os_prod_list, os_name_list, os_code_list, os_type_list]
            while len(values_list[0]):
                new_array = []
                for value in values_list:
                    new_array.append(value.pop(0))
                main_data.append(new_array)
    return main_data


def write_to_csv(csv_file):
    with open(csv_file, 'w') as f:
        data = get_data()
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)


if __name__ == "__main__":
    write_to_csv('new_file.csv')
