res_1 = 'результат операции: 42'
res_2 = 'результат операции: 514'
res_3 = 'результат работы программы: 9'

text_1, num_1 = res_1.split(': ')
text_2, num_2 = res_2.split(': ')
text_3, num_3 = res_3.split(': ')

print(int(num_1)+10)
print(int(num_2)+10)
print(int(num_3)+10)