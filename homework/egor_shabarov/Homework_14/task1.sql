INSERT INTO students (name, second_name, group_id) VALUES ('Игорь', 'Ветров', 1)

INSERT INTO book (title, taken_by_student_id) VALUES ('Алые паруса', 22394)
INSERT INTO book (title, taken_by_student_id) VALUES ('SQL для чайников', 22394)

INSERT INTO groups (title, start_date, end_date) VALUES ('GS_group', 'февраль2026', 'апрель2026');

UPDATE students s SET group_id = 22084 WHERE id = 22394

INSERT INTO subjects (title) VALUES ('gs_subj_1')
INSERT INTO subjects (title) VALUES ('gs_subj_2')

INSERT INTO lessons (title, subject_id) VALUES ('gs_lesson1', 14065)
INSERT INTO lessons (title, subject_id) VALUES ('gs_lesson2', 14065)
INSERT INTO lessons (title, subject_id) VALUES ('gs_lesson3', 14066)
INSERT INTO lessons (title, subject_id) VALUES ('gs_lesson4', 14066)

INSERT INTO marks (value, lesson_id, student_id) VALUES ('отлично', 75255, 22394)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('хорошо', 75256, 22394)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('хорошо', 75257, 22394)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('отлично', 75258, 22394)

SELECT s.name, s.second_name, l.title AS 'Занятие', m.value
FROM lessons l
JOIN marks m ON m.lesson_id = l.id
JOIN students s ON m.student_id = s.id
WHERE m.student_id = 22394

SELECT s.name, s.second_name, b.title
FROM books b
JOIN students s ON b.taken_by_student_id = s.id
WHERE s.id = 22394

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