#Raise an Exception
# the raise statement allows us the programmer to raise a specific exception to occur forcefully
def fun(x):
    try:
        raise NameError("Hii,where are you")
    except NameError:
        print("An exception raised")
        raise
fun(10)