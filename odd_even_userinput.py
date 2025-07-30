def even_odd(x):
    rem=x%2
    if(rem==0):
        print("The number is even")
    else:
        print("The number is odd")
    return x
x=int(input("Enter your choice of value: "))
even_odd(x)