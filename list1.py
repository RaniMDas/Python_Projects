from array import *
lst= [int(i) for i in input("Enter marks")]
print(lst)
Marks=array('i', lst)
sum=0
for x in Marks:
    print(x)
    sum+=x
print(sum)     
