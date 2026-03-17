import os
import datetime

current_dir = os.path.dirname(__file__)
path_homework = os.path.dirname(os.path.dirname(current_dir))
file_path = path_homework + '/eugene_okulik/hw_13/data.txt'
# file_path = path_homework + '/egor_shabarov/Homework_13/data.txt'


def file_open(path_file):
    """
    Открывает файл и читает все строки
    :param path: путь до файла
    :return: list: список из всех строк файла
    """
    with open(path_file, 'r') as file:
        file_data = file.readlines()
    return file_data


def str_date(my_str):
    """
    Излекает строку с датой из строки с текстом
    :param my_str: строку с датой и другим текстом
    :return: str: дата
    """
    return my_str.split()[1] + ' ' + my_str.split()[2]


def parser_date(my_date_str):
    """
    Преобразует строку с датой в объект с типом дата
    :param my_date_str: строка с датой
    :return: объект с типом дата
    """
    return datetime.datetime.strptime(my_date_str, '%Y-%m-%d %H:%M:%S.%f')


for line in file_open(file_path):
    line = line.strip()
    if line.startswith('1.'):
        date_str = str_date(line)
        print(f'Дата через неделю от указанной {parser_date(date_str) + datetime.timedelta(weeks=1)}')
    if line.startswith('2.'):
        date_str = str_date(line)
        date_obj = parser_date(date_str)
        print(f'День недели: {date_obj.strftime("%A")}')
    if line.startswith('3.'):
        date_str = str_date(line)
        date_obj = parser_date(date_str)
        result = datetime.datetime.now() - date_obj
        print(f'Прошло дней {result.days}')
