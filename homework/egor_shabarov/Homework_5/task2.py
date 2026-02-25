res_1 = 'результат операции: 42'
res_2 = 'результат операции: 514'
res_3 = 'результат работы программы: 9'

ind_space = res_1.index(': ')
num_1 = int(res_1[ind_space + 1:])

ind_space = res_2.index(': ')
num_2 = int(res_2[ind_space + 1:])

ind_space = res_3.index(': ')
num_3 = int(res_3[ind_space + 1:])

print(num_1 + 10)
print(num_2 + 10)
print(num_3 + 10)
