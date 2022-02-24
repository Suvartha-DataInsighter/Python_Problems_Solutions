#.Raising an Exception to handle another exception
def fun(x):
    try:
        int('N/A')
    except ValueError as e:
        raise RunTimeError("An error occured")from e
fun(2)

