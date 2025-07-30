class Student(object):
#This is a mutator method and initialized the instance variable in class
           
    def setname(self,name):
        self.name = name
#This is accessor mthod
    def getname(self):
        return self.name

#This is a mutator method 
    def setmarks(self, marks):
        self.marks=marks
#Accessor Method:
    def getmarks(self):
        return self.marks
#Create instances
n=int(input("Enter the number of students: "))
i=0
while(i<n):
    s1=Student()
    name=input("Enter your name: ")
    s1.setname(name)
    marks=int(input("Enter your marks: "))
    s1.setmarks(marks)

#Retreive data from student class instance
    print("Hi, Your name is ",s1.getname())
    print("Hi your marks is :",s1.getmarks())
    i+=1
    print("----------------------------------------------")