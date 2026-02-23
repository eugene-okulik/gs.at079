my_dict = {'tuple': (1, None, 'text', True, 3.55),
           'list': [6, 7, 'list', 8, 9],
           'dict': {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5},
           'set': {99, 'text', 37, False, 165}}

res_tuple = my_dict['tuple'][-1]
print(res_tuple)

my_dict['list'].append('new_value')
my_dict['list'].pop(1)

my_dict['dict']['i am a tuple'] = (1, 2, 3)
my_dict['dict'].pop('two')

my_dict['set'].add('new_elem')
my_dict['set'].pop()

print(my_dict)
