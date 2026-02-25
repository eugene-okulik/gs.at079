my_text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
           'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

word_list = my_text.split()
list_new = []

for word in word_list:
    if word.endswith('.'):
        list_new.append(word.rstrip('.') + 'ing.')
    elif word.endswith(','):
        list_new.append(word.rstrip(',') + 'ing,')
    else:
        list_new.append(word + 'ing')

new_text = ' '.join(list_new)

print(f'Первоначальный текст: {my_text}')
print(f'Измененный текст: {new_text}')
