 from person import Person_t

class Teacher_t(Person_t):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject

    def introduce(self):
        print("姓名：{} 年龄：{} 教授科目：{}".format(self.name,self.age,self.subject))


# per=Teacher_t("Yang",19,"math")
# per.introduce()