class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grade_lecturer(self, lecturer, course, grade):
        for courses in self.courses_in_progress:
            if courses in lecturer.courses_attached and grade >= 1 and grade <= 10:
                lecturer.grades[course] += [grade]
            else:
                print('Что-то пошло не так...')

    def __str__(self):
        summ = 0
        counter = 0
        name = f'Имя: {self.name}'
        surname = f'Фамилия: {self.surname}'
        if len(self.grades.items()) != 0:
            for el in self.grades.values():
                for el1 in el:
                    summ += el1
                    counter += 1
            average_grade = f'Средняя оценка за домашние задания: {round(summ / counter, 2)}'
            courses_in_progress = f'Курсы в процессе изучения: {" ".join(self.courses_in_progress)}'
            if len(self.finished_courses) != 0:
                finished_courses = f'Завершенные курсы: {" ".join(self.finished_courses)}'
            else:
                finished_courses = f'Нет завершенных курсов'
            result = f'{name}\n{surname}\n{average_grade}\n{courses_in_progress}\n{finished_courses}'
            return result
        else:
            return print('Что-то пошло не так...')

    def comparison(self, anoter_student):
        summ = 0
        counter = 0
        for el in self.grades.values():
            for el1 in el:
                summ += el1
                counter += 1
        self_average_grade = round(summ / counter, 2)
        summ = 0
        counter = 0
        for el in anoter_student.grades.values():
            for el1 in el:
                summ += el1
                counter += 1
        anoter_student_average_grade = round(summ / counter, 2)
        if self_average_grade > anoter_student_average_grade:
            print(f'У студента {self.name} средний балл выше, чем у {anoter_student.name}')

        elif self_average_grade < anoter_student_average_grade:
            print(f'У студента {anoter_student.name} средний балл выше, чем у {self.name}')

        else:
            print('Оценки у обоих студентов равны')

    def average_grade(self, course):
        summ = 0
        counter = 0
        for student in students:
            if course in self.grades.keys():
                grades = self.grades[course]
                for grade in grades:
                    summ += grade
                    counter += 1
        result = summ / counter
        print(round(result, 1))


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        summ = 0
        counter = 0
        name = f'Имя: {self.name}'
        surname = f'Фамилия: {self.surname}'
        if len(self.grades.values()) != 0:
            if len(self.grades.values()) != 0:
                for el in self.grades.values():
                    for el1 in el:
                        summ += el1
                        counter += 1
                average = f'Средняя оценка за лекции: {round(summ / counter, 2)}'
        else:
            average = 'Лекций нет'
        result = f'{name}\n{surname}\n{average}'
        return result

    def comparison(self, another_lecturer):
        summ = 0
        counter = 0
        for el in self.grades.values():
            for el1 in el:
                summ += el1
                counter += 1
        self_average_grade = round(summ / counter, 2)
        summ = 0
        counter = 0
        for el in another_lecturer.grades.values():
            for el1 in el:
                summ += el1
                counter += 1
        anoter_student_average_grade = round(summ / counter, 1)
        if self_average_grade > anoter_student_average_grade:
            print(f'У лектора {self.name} средний балл выше, чем у {another_lecturer.name}')

        elif self_average_grade < anoter_student_average_grade:
            print(f'У лектора {another_lecturer.name} средний балл выше, чем у {self.name}')

        else:
            print('Оценки у обоих лекторов равны')

    def average_grade(self, course):
        summ = 0
        counter = 0
        for lecturer in lecturers:
            if course in self.grades.keys():
                grades = self.grades[course]
                for grade in grades:
                    summ += grade
                    counter += 1
        result = summ / counter
        print(round(result, 1))


class Rewiewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades.keys():
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        name = f'Имя: {self.name}'
        surname = f'Фамилия: {self.surname}'
        result = f'{name}\n{surname}'
        return result


# Создание экземпляров класса Student
jack = Student('Jack', 'Wilson', 'Male')
jack.finished_courses = ['HTML', 'C++']
jack.courses_in_progress = ['Java', 'Python']
jack.grades = {'Python': [9, 7], 'HTML': [9, 9], 'C++': [10, 8], 'Java': [8, 10]}

billy = Student('Billy', 'Bons', 'Male')
billy.finished_courses = ['Java', 'C#']
billy.courses_in_progress = ['Python']
billy.grades = {'Java': [9, 9], 'C#': [8, 10], 'Python': [10, 10]}

# Создание экземпляров класса Mentor
joseph = Mentor('Joseph', 'Evans')
joseph.courses_attached = ['Python', 'C#']

rick = Mentor('Rick', 'Wilson')
rick.courses_attached = ['Java', 'JavaScript']

# Создание экземпляров класса Lecturer
george = Lecturer('George', 'Adamson')
george.courses_attached = ['Java', 'Python', 'C#']
george.grades = {'Java': [9, 10], 'Python': [9, 8], 'C#': [8, 10]}

olivia = Lecturer('Olivia', 'Harris')
olivia.courses_attached = ['HTML', 'JavaScript', 'Python']
olivia.grades = {'HTML': [8, 9], 'JavaScript': [8, 10], 'Python': [10, 8]}

# Создание экземпляров класса Reviewer
jessica = Rewiewer('Jessica', 'Walker')
jessica.courses_attached = ['Python', 'JavaScript']

connor = Rewiewer('Connor', 'Ellington')
connor.courses_attached = ['Python', 'C#', 'Java']

# Оценивание лектора студентом
jack.grade_lecturer(george, 'Python', 10)

#    Вывод метода __str__
# Student
print(jack)

# Lecturer
print(george)

# Reviewer
print(jessica)

#    Сравнение
# Студентов
billy.comparison(jack)

# Лекторов
george.comparison(olivia)

# Оценивание Reviewer
jessica.rate_hw(jack, 'Python', 8)

# Расчет средний оценки за д/з по всем студентам в рамках конкретного курса
students = [jack, billy]
jack.average_grade('Python')

# Расчет средней оценки за лекции всех лекторов в рамках курса
lecturers = [george, olivia]
george.average_grade('Python')