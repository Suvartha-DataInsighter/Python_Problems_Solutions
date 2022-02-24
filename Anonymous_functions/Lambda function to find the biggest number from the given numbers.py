max=lambda x,y:x if x>y else y
a,b=[int(n) for n in input("enter two values:").split(",")]
print("the greatest number is=",max(a,b))
