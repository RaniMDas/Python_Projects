# input n
n = 5
First_num=1
for i in range(1, n+1):
    for j in range(1, (n-i)+1):
        print(' ', end=' ')

    for k in range (0,i):
        if k ==0 or i==0:
            First_num=1
        else:
            First_num=First_num*(i-k)//k
        print(First_num, end=" ")
    print()