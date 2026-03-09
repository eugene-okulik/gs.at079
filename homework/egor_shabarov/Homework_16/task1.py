import os
import dotenv
import mysql.connector
import csv

dotenv.load_dotenv()

current_dir = os.path.dirname(__file__)
path_hw = (os.path.dirname(os.path.dirname(current_dir)))
file_path = os.path.join(path_hw, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(file_path, newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    csv_content = []
    for line in reader:
        csv_content.append(line)

db = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSW'),
    database=os.getenv('DB_NAME')
)
print("Успешное подключение к базе данных!")

cursor = db.cursor()

for line in csv_content:
    query = """SELECT s.name  FROM students s 
    JOIN `groups` g ON s.group_id = g.id 
    JOIN books b ON s.id = b.taken_by_student_id 
    JOIN marks m ON s.id = m.student_id 
    JOIN lessons l ON m.lesson_id = l.id 
    JOIN subjects sub ON l.subject_id = sub.id 
    WHERE s.name = %s AND s.second_name = %s AND g.title = %s AND b.title = %s AND sub.title = %s 
    AND l.title = %s AND m.value = %s
    """
    value = (line['name'], line['second_name'], line['group_title'], line['book_title'], line['subject_title'],
             line['lesson_title'], line['mark_value'])

    cursor.execute(query, value)
    result = cursor.fetchall()
    if len(result) == 0:
        print('Этих данных нет в базе данных')
        print(line)

db.close()
