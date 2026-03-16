import os
import argparse
import datetime


def arg_parser():
    """
    Разбирает аргументы командной строки
    :return:
    path - путь к папке
    search - текст, который хотим найти
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Путь к папке/файлу')
    parser.add_argument('--text', required=True, help='Значение поискового запроса для поиска по тексту')
    args = parser.parse_args()

    search = args.text
    path = args.path
    return path, search


def get_file_list(path):
    """
    Получает список файлов в папке
    :param path: путь к файлу/папке
    :return: список файлов
    """
    if os.path.isfile(path):
        file_list = [path]
        return file_list
    elif os.path.isdir(path):
        file_list = []
        files = os.scandir(path)
        for file in files:
            if file.is_file():
                file_list.append(file.path)
        files.close()
        return file_list
    else:
        print('Путь не содержит файлов')
        return None


def datetime_from_line(line):
    """
    Получаем объект datetime из линии файла с логами
    :param line: строка из файла с логами
    :return: datetime объект или None
    """
    try:
        datetime_block = datetime.datetime.strptime(' '.join(line.split()[:2]), '%Y-%m-%d %H:%M:%S.%f')
        return datetime_block
    except (ValueError, IndexError):
        return None


def log_reader(file_list):
    """
    Читает файлы с логами и создает словарь с ключом по дате
    :param file_list: список файлов
    :return: словарь, где ключ - дата записи в логах (блока), список строк блока
    """

    all_logs_dict = {}

    for file_path in file_list:
        file_name = os.path.basename(file_path)
        datetime_block = None
        current_block_lines = []

        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.rstrip('\n')

                datetime_key = datetime_from_line(line)
                if datetime_key:

                    if datetime_block and current_block_lines:
                        if datetime_block not in all_logs_dict:
                            all_logs_dict[datetime_block] = []
                        for block_line in current_block_lines:
                            all_logs_dict[datetime_block].append(block_line)

                    datetime_block = datetime_key
                    current_block_lines = [(line, file_name, line_num)]

                else:
                    if datetime_block:
                        current_block_lines.append((line, file_name, line_num))

            if datetime_block and current_block_lines:
                if datetime_block not in all_logs_dict:
                    all_logs_dict[datetime_block] = []
                for block_line in current_block_lines:
                    all_logs_dict[datetime_block].append(block_line)

    return all_logs_dict


def search_text(all_logs_dict, search):
    """
    Находит текст в логах и печатает итоговые результаты
    :param all_logs_dict: словарь с логами
    :param search: текст, по которому осуществляет поиск
    :return: количество результатов
    """
    result_count = 0

    for date, log_data in all_logs_dict.items():
        for line, filename, line_num in log_data:
            if search in line:
                result_count += 1

                word_list = line.split()
                word_list_without_dor = [word.strip('.,:;!?') for word in word_list]

                index_word = word_list_without_dor.index(search)
                index_start = index_word - 5
                index_stop = index_word + 6
                len_line = len(word_list)

                if index_start < 0 and index_stop > len_line:
                    part_text = ' '.join(word_list[:])
                elif index_start < 0:
                    part_text = ' '.join(word_list[:index_stop])
                elif index_stop > len_line:
                    part_text = ' '.join(word_list[index_start:])
                else:
                    part_text = ' '.join(word_list[index_start:index_stop])

                print(f"\nРезультат {result_count}")
                print(f"Имя файла: {filename}")
                print(f"Дата: {date}")
                print(f"Фрагмент логов: ... {part_text} ...")

    if result_count == 0:
        print(f"Текст '{search}' не найден.")

    return result_count


path, search = arg_parser()

file_list = get_file_list(path)

logs_dict = log_reader(file_list)

search_text(logs_dict, search)
