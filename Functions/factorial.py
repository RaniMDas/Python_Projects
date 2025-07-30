def fact (num):
    i=1
    while(num>0):
        i=i*(num)
        print(i)
        num-=1
    return i
    
a=fact(5)
print("The factorial of the number 5 is: ",a)