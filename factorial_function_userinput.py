def fact(num):
    n=1
    while(num>=1):
        n=num*n
        num-=1
    return n
    print("The factorial of the number is:" ,n)
num=int(input("Enter the value of your choice: "))
fact(num)
