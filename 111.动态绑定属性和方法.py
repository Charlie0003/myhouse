# 文件名: 111.动态绑定属性和方法.py
# 开发时间: 2022/7/10 21:12
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')

stu1=Student('张三',20)
stu2=Student('李四',30)
print(id(stu1))
print(id(stu2))
stu1.gender='女'
print(stu1.name,stu1.age,stu1.gender)
print(stu2.name,stu2.age)

stu1.eat()
stu2.eat()

def show():
    print('函数')

stu1.show=show
stu1.show()