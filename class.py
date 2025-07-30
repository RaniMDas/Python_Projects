class Student (object):
    def __init__(self, n):
        self.name=n
    def display(self):
        print("Hi my name is:","",self.name)
n=int(input("Enter the number of students: "))
i=0
while (i<n):
    name=input("Enter your name: ")
    s1=Student(name)
    s1.display()
    i+=1
    print("------------------------")





      
  

