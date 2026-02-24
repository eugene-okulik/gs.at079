result_1 = 'результат операции: 42'
result_2 = 'результат операции: 54'
result_3 = 'результат работы программы: 209'
result_4 = 'результат: 2'


def my_func(result_program):
    print(int(result_program.split(': ')[1]) + 10)


my_func(result_1)
