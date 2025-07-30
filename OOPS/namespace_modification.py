class Student(object):
    n=10            #This is a class variable
s1=Student()        #Instance1
s2=Student()
print("The value of n in s1","",s1.n)   #The value of n in s1  10
print("The value of n in s2","",s2.n)   #The value of n in s2  10

s1.n+=1
print("The value of n in s1","",s1.n)   #The value of n in s1  11
print("The value of n in s2","",s2.n)   #The value of n in s1  10