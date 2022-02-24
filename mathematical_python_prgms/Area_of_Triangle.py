#AREA OF TRIANGLE
def area_tri(a,b,c):
    s=(a+b+c)/2
    area_of_tri=(s*(s-a)*(s-b)*(s-c))*0.05
    print(area_of_tri)
area_tri(a=3,b=6,c=8)