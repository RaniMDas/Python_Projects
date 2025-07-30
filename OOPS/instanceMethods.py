class Student(object):

#Constructor to initialize instance variables
    def __init__(self,name="", marks=0):
        self.name=name
        self.marks=marks

#Instance method to dsiplay the student details
    def display(self):
        print("Hi, My name is","",self.name)
        print("Hi, My marks is","",self.marks)

#Instance method to display the grade
    def calculate(self):
        if(self.marks>=600):
            print("Congrats, you got First Grade")
        elif(self.marks>=500):
            print("Congrats, you got Second Grade")
        elif(self.marks>=400):
            print("Congrats, you got Third Grade")
        else:
            print("You are Failed. Take Re-test")
            
#Instances to get some data from keyboard
n=int(input("Enter the number of students"))
i=0
while(i<n):
    name=input("Enter your name:  ")
    marks=int(input("Enter your make: "))
    s1=Student(name,marks)
    s1.display()
    s1.calculate()
    i+=1
    print("---------------------------------------------")