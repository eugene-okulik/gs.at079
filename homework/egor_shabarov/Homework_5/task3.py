students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print('Students ' + ', '.join(students) + ' study these subjects: ' + ', '.join(subjects))  # Вариант №1
print(f'Students {", ".join(students)} study these subjects: {", ".join(subjects)}')  # Вариант №2
