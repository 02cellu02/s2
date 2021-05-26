#2d list
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0])#print first list inside
print(matrix[0][1])#print 2
#to edit elt
matrix[0][0]=10
for row in matrix:
    for item in row:
        print(item)
        