# Создайте студента (student)
INSERT INTO students (name, second_name, group_id) VALUES ('Игорь', 'Ветров', 1)

# Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
INSERT INTO book (title, taken_by_student_id) VALUES ('Алые паруса', 22394)
INSERT INTO book (title, taken_by_student_id) VALUES ('SQL для чайников', 22394)

# Создайте группу (group) и определите своего студента туда
INSERT INTO groups (title, start_date, end_date) VALUES ('GS_group', 'февраль2026', 'апрель2026');
UPDATE students s SET group_id = 22084 WHERE id = 22394

# Создайте несколько учебных предметов (subjects)
INSERT INTO subjects (title) VALUES ('gs_subj_1')
INSERT INTO subjects (title) VALUES ('gs_subj_2')

# Создайте по два занятия для каждого предмета (lessons)
INSERT INTO lessons (title, subject_id) VALUES ('gs_lesson1', 14065)
INSERT INTO lessons (title, subject_id) VALUES ('gs_lesson2', 14065)
INSERT INTO lessons (title, subject_id) VALUES ('gs_lesson3', 14066)
INSERT INTO lessons (title, subject_id) VALUES ('gs_lesson4', 14066)

# Поставьте своему студенту оценки (marks) для всех созданных вами занятий
INSERT INTO marks (value, lesson_id, student_id) VALUES ('отлично', 75255, 22394)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('хорошо', 75256, 22394)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('хорошо', 75257, 22394)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('отлично', 75258, 22394)

# Все оценки студента
SELECT s.name, s.second_name, l.title AS 'Занятие', m.value
FROM lessons l
JOIN marks m ON m.lesson_id = l.id
JOIN students s ON m.student_id = s.id
WHERE m.student_id = 22394

# Все книги, которые находятся у студента
SELECT s.name, s.second_name, b.title
FROM books b
JOIN students s ON b.taken_by_student_id = s.id
WHERE s.id = 22394

# Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
SELECT
s.name, s.second_name,
g.title AS "group",
b.title AS book,
m.value AS mark,
l.title AS lesson,
sub.title AS subject
FROM students s
JOIN "groups" g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjects sub ON l.subject_id = sub.id
WHERE s.id = 22394;

# Второй вариант запроса (с LEFT JOIN), если у пользователя вообще не будет оценок или книг
SELECT
s.name, s.second_name,
g.title AS group_name,
b.title AS book_title,
m.value AS mark,
l.title AS lesson_title,
sub.title AS subject_title
FROM students s
LEFT JOIN "groups" g ON s.group_id = g.id
LEFT JOIN books b ON b.taken_by_student_id = s.id
LEFT JOIN marks m ON m.student_id = s.id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjects sub ON l.subject_id = sub.id
WHERE s.id = 22394;