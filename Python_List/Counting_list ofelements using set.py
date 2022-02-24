def listcount_set(lst):
    print ([[l, lst.count(l)] for l in set(lst)])
    print (dict( (l, lst.count(l) ) for l in set(lst)))
lst=[1,1,1,3,2,3,3,4,4,4,5,5,6]
listcount_set(lst)