def count_list(l1):
    l2=[{i:l1.count(i) for i in l1 }]
    print(l2)
l1=[1,2,3,4,5,6,7,8,1,2,3,4,5]
count_list(l1)
