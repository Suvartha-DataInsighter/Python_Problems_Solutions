def final(x,y):
    try:
        z=x/y
        print(z)
    except ZeroDivisionError:
        print("we cannot divide by 0")
    finally:
        print("we should always provide a positive integer > 0")
final(10,2)
final(10,0)