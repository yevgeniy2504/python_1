# Создайте класс студента.
# ○
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○
# Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○
# Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.


import csv


class Text:
    def __init__(self, validation_func):
        self.validation_func = validation_func

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value):
        if self.validation_func(value):
            setattr(instance, self.param_name, value)
        else:
            raise ValueError(f'Bad value: {value}')

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)


class Student:
    subjects = []

    def __init__(self, first_name, last_name, filename):
        self.first_name = first_name
        self.last_name = last_name
        self.file_name = filename

    def __call__(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            self.subjects = next(reader)

    def __repr__(self):
        return f'Student(first_name={self.first_name}, last_name={self.last_name})'


class Grade:
    def __init__(self):
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject not in Student.subjects:
            raise ValueError(f'Invalid subject: {subject}')
        if grade < 2 or grade > 5:
            raise ValueError(f'Invalid grade: {grade}')
        self.grades[subject] = grade

    def get_average_grade(self, subject):
        if subject not in self.grades:
            raise ValueError(f'No grades available for subject: {subject}')
        return self.grades[subject]

    def get_overall_average(self):
        if not self.grades:
            raise ValueError('No grades available')
        return sum(self.grades.values()) / len(self.grades)


# Пример использования
if __name__ == '__main__':
    student = Student('Гвидо', 'ВАН РОССУМ', 'subjects.csv')
    grades = Grade()
    grades.add_grade('Геометрия', 4)
    grades.add_grade('Химия', 5)
    grades.add_grade('Биология', 3)

    print(student)
    print(grades.get_average_grade('Геометрия'))
    print(grades.get_overall_average())
