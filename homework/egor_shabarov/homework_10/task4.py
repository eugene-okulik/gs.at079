PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

pairs_list = PRICE_LIST.split('\n')

# Вариант 1. List comprehension
name_list = [i.split()[0] for i in pairs_list]
cost_list = [int(i.split()[1].rstrip('р')) for i in pairs_list]
new_dict1 = dict(zip(name_list, cost_list))

# Вариант 2. Dict comprehension
new_dict2 = {i.split()[0]: int(i.split()[1].rstrip('р')) for i in pairs_list}

print(new_dict1)
print(new_dict2)
