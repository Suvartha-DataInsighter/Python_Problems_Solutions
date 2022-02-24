s=[]
n=int(input("enter how many strings that we need to sort:"))
for i in range(n):
    print("enter string:",end=" ")
    s.append(input())
s1=sorted(s)
print("sorted list is:")
for i in s1:
    print(i)