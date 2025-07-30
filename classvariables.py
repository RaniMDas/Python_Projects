class sample(object):
    x=10
    @classmethod
    def modify (cls):
        cls.x+=1
s1=sample() #instance 1
s2=sample() #instance 2
print(s1.x,s2.x)
s1.modify() #invoked class method
#s2.modify() #invoked class method
print(s1.x,s2.x)

class sample:
    x=10
    def modify(cls):
       cls.x+=1
#Create two instances
s1=sample()
s2=sample()
s1.modify()
print(s1.x,s2.x)
