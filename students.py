class Student:

    all_students = []

    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        Student.all_students.append(self)

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        if new_grade < 0 or new_grade > 100:
            raise ValueError("not a valid grade")
        self._grade = new_grade

    @staticmethod
    def calculate_average_grade(students):
        if len(students) < 1:
            return -1
        else:
            total_grades = 0
            for i in students:
                total_grades += i.grade

        return total_grades / len(students)

    @classmethod
    def get_average_grade(cls):
        return cls.calculate_average_grade(cls.all_students)


    @classmethod
    def get_best_student(cls):
        best_student = None
        for j in cls.all_students:
            if best_student == None:
                best_student = j
            if j.grade > best_student.grade:
                best_student = j
        return best_student.name


