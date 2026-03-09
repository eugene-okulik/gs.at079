import mysql.connector

db = mysql.connector.connect(
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='st-onl',
    password='AVNS_tegPDkI5BlB2lW5eASC',
    database='st-onl'
)
print("Успешное подключение к базе данных!")

cursor = db.cursor(dictionary=True)

insert_query_1 = 'INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)'
values_1 = ('Игорь', 'Ветров', 1)
cursor.execute(insert_query_1, values_1)
student_id = cursor.lastrowid

insert_query_2 = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
values_2 = [('Алые паруса', student_id), ('SQL для чайников', student_id)]
cursor.executemany(insert_query_2, values_2)


insert_query_3 = 'INSERT INTO "groups" (title, start_date, end_date) VALUES (%s, %s, %s)'
values_3 = ('GS_group', '2026-02-01', '2026-04-30')
cursor.execute(insert_query_3, values_3)
group_id = cursor.lastrowid

insert_query_4 = "UPDATE students s SET group_id = %s WHERE id = %s"
values_4 = (group_id, student_id)
cursor.execute(insert_query_4, values_4)

insert_query_5 = "INSERT INTO subjects (title) VALUES (%s)"
values_5 = [('gs_subj_1', ), ('gs_subj_2', )]
subject_id = []
for subject in values_5:
    cursor.execute(insert_query_5, subject)
    subject_id.append(cursor.lastrowid)


insert_query_6 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values_6 = [('gs_lesson1', subject_id[0]), ('gs_lesson2', subject_id[0]),
            ('gs_lesson3', subject_id[1]), ('gs_lesson4', subject_id[1])]
lesson_id = []
for lesson in values_6:
    cursor.execute(insert_query_6, lesson)
    lesson_id.append(cursor.lastrowid)

insert_query_7 = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
values_7 = [('отлично', lesson_id[0], student_id), ('хорошо', lesson_id[1], student_id),
            ('хорошо', lesson_id[2], student_id), ('отлично', lesson_id[3], student_id)]
cursor.executemany(insert_query_7, values_7)

cursor.execute('''
SELECT s.name, s.second_name, l.title AS 'Занятие', m.value
FROM lessons l
JOIN marks m ON m.lesson_id = l.id
JOIN students s ON m.student_id = s.id
WHERE m.student_id = %s
''', (student_id,))
mark_student = cursor.fetchall()
print(f'Оценки студента: {mark_student}')

cursor.execute('''
SELECT s.name, s.second_name, b.title
FROM books b
JOIN students s ON b.taken_by_student_id = s.id
WHERE s.id = %s
''', (student_id,))
book_student = cursor.fetchall()
print(f'Книги студента: {book_student}')

cursor.execute('''
    SELECT
    s.name, s.second_name,
    g.title AS `group`,
    b.title AS book,
    m.value AS mark,
    l.title AS lesson,
    sub.title AS subject
    FROM students s
    JOIN `groups` g ON s.group_id = g.id
    JOIN books b ON s.id = b.taken_by_student_id
    JOIN marks m ON s.id = m.student_id
    JOIN lessons l ON m.lesson_id = l.id
    JOIN subjects sub ON l.subject_id = sub.id
    WHERE s.id = %s
''', (student_id,))
data_student = cursor.fetchall()

print("Вся информация о студенте:")
for _ in data_student:
    print(_)

db.commit()
db.close()
