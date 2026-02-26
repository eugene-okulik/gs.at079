import random


def final_salary(salary):
    user_bonus = random.choice([True, False])
    if user_bonus is True:
        fin_sal = salary + random.randrange(1, 5000)
    else:
        fin_sal = salary
    return fin_sal


user_salary = int(input('Введите вашу текущую зарплату: '))

print(f'Итоговая зарплата составит: {final_salary(user_salary)}')
