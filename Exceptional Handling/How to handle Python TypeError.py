#handling typeerror
def type_error(x,y):
    try:
        print(x+y)
    except TypeError as t:
        print("we cannot add an int and str")
type_error(5,"sam")