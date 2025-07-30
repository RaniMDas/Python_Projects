class student(object):
    def __init__(self,name,age,marks): #dunder method to initialize the variable using a parameterised constructor
        self.name=name 
        self.age=age
        self.marks=marks
        print(id(self))

