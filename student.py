 from person import Person_t

class Student_t(Person_t):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade

    def introduce(self):
        print("姓名：{} 年龄：{} 年级：{}".format(self.name,self.age,self.grade))

# per=Student_t("Yang",19,2023)
# per.introduce()