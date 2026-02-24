my_number = 79


def game_number(secret_number):
    while True:
        user_num = int(input('Введите число: '))
        if user_num == my_number:
            print('Поздравляю! Вы угадали!')
            break
        else:
            print('Попробуйте снова')


game_number(my_number)