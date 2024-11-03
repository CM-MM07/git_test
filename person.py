class Person_t():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        print("姓名：{} 年龄：{}".format(self.name,self.age))

