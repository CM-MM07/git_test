class Person_t():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("姓名：{} 年龄：{}".format(self.name, self.age))

class Teacher_t(Person_t):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        print("姓名：{} 年龄：{} 教授科目：{}".format(self.name, self.age, self.subject))

class Student_t(Person_t):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def introduce(self):
        print("姓名：{} 年龄：{} 年级：{}".format(self.name, self.age, self.grade))

class Course_t:
    def __init__(self, course_name, teacher, students=None):
        self.course_name = course_name
        self.teacher = teacher  # `Teacher_t` 对象
        self.students = students if students is not None else []  # 存储 `Student_t` 对象的列表

    def addStudent(self, Student):
        if Student not in self.students:
            self.students.append(Student)

    def removeStudent(self, Student):
        if Student in self.students:
            self.students.remove(Student)

    def showCourseInfo(self):
        print(f'-->课程：{self.course_name} 老师：{self.teacher.name}')
        print("学生：", end=" ")
        for student in self.students:
            print(f"{student.name}", end=" ")
        print("\n")
