n=1
def fn ():
    global n
    n=5
    print("in",n)
fn()
print("out",n)

'''
n=1
def fn(n)
    global n 
    print("in",n)
fn(5)
This is wrong because you cannot make the parameter global and pass the variable as parameter. 
A parameter is specific to that function
It will throw a syntax error
'''