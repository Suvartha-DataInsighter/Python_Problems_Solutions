def zip_index(names,ages):
    for i,(names, ages) in enumerate(zip(names, ages)):
        print(i,names, ages)
names = ['Rakesh', 'Prince', 'Charles']
ages = [24, 50, 18]
zip_index(names,ages)
 