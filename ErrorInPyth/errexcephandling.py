try:
    a=8
    b=0
    print(a/b)
except ZeroDivisionError:
    print("There is an error")
finally:
    print("Continue with the following code")

""""We use try except and finally
If you want to try something and do not know whethere it gives an error
Bring it under the try part
If you know the error and do not want a traceback and want your statement, it is written under except
Finally whether your code gives error or not, the piece of code gets printed"""