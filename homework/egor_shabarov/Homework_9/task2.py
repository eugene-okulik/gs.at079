temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
    22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]

high_temp = list(filter(lambda x: x > 28, temperatures))

print(high_temp)
print(f'Самая высокая температура: {max(high_temp)}')
print(f'Самая низкая температура из жарких дней: {min(high_temp)}')
print(f'Средняя температура в жаркие дни: {round(sum(high_temp) / len(high_temp), 1)}')
