class Book:
    material_page = 'бумага'
    presence_text = True

    def __init__(self, title, author, count_page, isbn, reserved=False):
        self.title = title
        self.author = author
        self.count_page = count_page
        self.ISBN = isbn
        self.reserved = reserved

    def print_info_book(self):
        if self.reserved:
            print((f'Название: {self.title}, Автор: {self.author}, страниц: {self.count_page}, '
                   f'материал: {self.material_page}, книга зарезервирована.'))
        else:
            print((f'Название: {self.title}, Автор: {self.author}, страниц: {self.count_page}, '
                   f'материал: {self.material_page}.'))

class SchoolBook(Book):

    def __init__(self, title, author, count_page, isbn, subject, grade, task, reserved=False):
        super().__init__(title, author, count_page, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.task = task

    def print_info_book(self):
        if self.reserved:
            print((f'Название: {self.title}, Автор: {self.author}, страниц: {self.count_page}, '
                   f'Предмет: {self.subject}, класс: {self.grade}, книга зарезервирована.'))
        else:
            print((f'Название: {self.title}, Автор: {self.author}, страниц: {self.count_page}, '
                   f'Предмет: {self.subject}, класс: {self.grade}.'))


book_id1 = Book('Идиот', 'Достоевский', 500, '978-6-699-1204-7')
book_id2 = Book('Война и мир', 'Толстой', 1000, '978-5-699-1204-8')
book_id3 = Book('Мастер и Маргарита', 'Булгаков', 350, '978-5-17-987654-3', reserved=True)
book_id4 = Book('Над пропастью во ржи', 'Сэлинджер', 352, '978-5-04-123456-1')
book_id5 = Book('Мы', 'Замятин', 224, '978-5-17-110724-6')

book_id5.reserved = True

book_id1.print_info_book()
book_id2.print_info_book()
book_id3.print_info_book()
book_id4.print_info_book()
book_id5.print_info_book()

book_id6 = SchoolBook('Алгебра', 'Иванов', 200, '78-5-17-987654-9', 'Математика', 9, task=True)
book_id7 = SchoolBook('Физика', 'Сидоров', 250, '978-5-09-123456-7', 'Физика', 8, task=False, reserved=True)
book_id8 = SchoolBook('Русский язык', 'Петров', 300, '978-5-09-765432-1', 'Русский язык', 5, task=True)
book_id9 = SchoolBook('История', 'Смирнов', 280, '978-5-09-888999-0', 'История', 7, task=True)

book_id9.reserved = True

print()
book_id6.print_info_book()
book_id7.print_info_book()
book_id8.print_info_book()
book_id9.print_info_book()
