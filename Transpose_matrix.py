def solve(matrix):
    r=len(matrix)

    if r==0:
        return []

    c=len(matrix[0])

    for i in range(0,r):
        for j in range(0,i):
            tmp = matrix[i][j]  
            matrix[i][j]=matrix[j][i]
            matrix[j][i] = tmp
    return matrix       
        

matrix=[[1, 2, 3],[4, 5, 6],[7, 8, 9]]

print(solve(matrix))