t=(10,20,30,255,30)
#print(type(t))
#b=bytes(t)
#print(b)
#a=10
#c=bytes(t)
#print(c)
for i in range(0,4,1):
    print(t[i])
print("Out of for loop")

i=0
while(i<4):
    print(t[i])
    i=i+1
print("Out of while loop")