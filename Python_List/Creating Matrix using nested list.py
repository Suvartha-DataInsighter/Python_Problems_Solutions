def matrix_list(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print("%d"%m[i][j],end=" ")
        print()
m=[[1,2,3],[4,5,6],[7,8,9]]
matrix_list(m)