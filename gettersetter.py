class student:
    def setName(self,name):
        self.name=name
    def setMarks(self, marks):
        self.marks=marks
    def getName(self):
        return self.name
    def getMarks(self):
        return self.marks
    
n = int(input("Enter the number of student  :  "))
i=0
while (i<n):
    s= student()
    name = input("Enter the name of the student: ")
    s.setName
    marks=input("Enter your marks")
    s.setMarks
    print("Hi", "", s.getName)
    print("Your marks is","", s.getMarks)
    i+=1