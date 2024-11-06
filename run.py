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

# 示例数据
stu_1 = Student_t('Xiao Ming', '18', '1')
stu_2 = Student_t('Xiao Hong', '19', '2')
stu_3 = Student_t('Xiao Hua', '18', '1')

tea_1 = Teacher_t('Ding Lantian', '31', 'English')
tea_2 = Teacher_t('Xu Meng', '47', 'Math')

# 创建课程对象，初始化时加入老师和学生列表
cou_1 = Course_t('Math', tea_2, [stu_1])
cou_2 = Course_t('English', tea_1, [stu_2])

# 显示课程信息
cou_1.showCourseInfo()
cou_2.addStudent(stu_3)
cou_2.showCourseInfo()
