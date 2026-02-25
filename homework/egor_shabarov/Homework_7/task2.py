words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def dict_func(my_dict):
    for key in my_dict:
        print(key * my_dict[key])


dict_func(words)
