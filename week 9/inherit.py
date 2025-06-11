class Student():

    def __init__(self,name,age,id):
         self.name = name
         self.age = age
         self.id = id
    def campus(self):
         print("London Campus")
class Mode(Student):
    def __init__(self,name,mode):
        self.name = name
        self.mode = mode
stu1=Mode("Tina", "Online")
stu2=Student("Mina", "21", "203")
print(stu1.name)
print(stu1.mode)
print(stu2.name, stu2.age, stu2.id)
print(stu2.age)
print(stu2.id)
stu2.campus()
stu1.campus()
