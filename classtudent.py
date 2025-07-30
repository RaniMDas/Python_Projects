class sample ():
    def __init__(self):
        self.x=10
    def modify (self): #instance method
        self.x+=1
s1=sample()
s2=sample()
print(s1.x) #10
print(s2.x) #10
s1.modify() #call
print(s1.x)
print(s2.x)

