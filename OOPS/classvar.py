class Sample(object):

#Declaring and initializing a class variable
    x=10

#This is a class method
    @classmethod
    def modify(cls):
        cls.x+=1

#Creating two instances
s1=Sample()
s2=Sample()
print("-------------------------------")
print("The value of x in s1","",s1.x)           #10
print("The value of x in s2","",s2.x)           #10
print("-------------------------------")
print("The class variable is","",Sample.x) 
#Modifying class variable in one instance
s1.modify()
print("-------------------------------")
print("The value of x in s1","",s1.x)           #11
print("The value of x in s2","",s2.x)           #11
print("-------------------------------")
print("The class variable is","",Sample.x)      #The class variable is  11
print(type(s1))                                 #<class '__main__.Sample'>
print(type(s1.x))                               #<class 'int'>
print(type(s1.modify()))                        #<class 'NoneType'>
print(type(Sample))                             #<class 'type'>
