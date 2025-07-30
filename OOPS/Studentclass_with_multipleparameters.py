class Student(object):

#This is constructor
    def __init__(self, name="", marks=0):
        self.name=name
        self.marks=marks

#Creating an instance method
    def display(self):
        print("Hi I am", "",self.name)
        print("My marks are","",self.marks)

#Constructor is called with parameters in the instance
print("-------------------------")
s1=Student("Rani",400)
s1.display()
print("-------------------------")

#Constructor is called without values in the instance
s1=Student()
s1.display()
print("-------------------------")