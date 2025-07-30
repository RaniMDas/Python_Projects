m,n=int(input("Enter the maximum and minimum number "))
x=m
while x>=m and x<=n:
    if x%2==0:
        print(x)
    else:
        x+=1
print("You are out of the loop")
