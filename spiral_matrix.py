def spiral_matrix(matrix):

    # matrix = [ [ 0 for i in range(col) ] for j in range(row)]

    # print(len(matrix))
    min_row=0
    min_col=0
    max_row = len(matrix)-1
    max_col=len(matrix[0])-1
    tne= len(matrix)*len(matrix[0])
    count=0
    while(True):

    #left wall
        for i in range(min_row,max_row+1):
            if count<tne:
                j=min_col
                print(matrix[i][j])
                count+=1
            else:
                break
        min_col+=1
        

    #bottom wall
        for j in range(min_col,max_col+1):
            if count<tne:
                i=max_row
                print(matrix[i][j])
                count+=1
            else:
                break
        max_row-=1
        
    #right wall
        for  i in range(max_row,min_row-1, -1):
            if count<tne:
                j=max_col
                print(matrix[i][j])
                count+=1
            else:
                break    
        max_col-=1
      
    #top wall
        for  j in range(max_col,min_col-1, -1):
            if count<tne:
                i=min_row
                print(matrix[i][j])
                count+=1
            else:
                break
        min_row+=1

    #lw=min_col
    #bw=max_row
    #rw=max_col
    #tw=min_row


row=3
col=6
# for i in range(0, row):
#     for j in range(0, col):
#         a[i][j]=int(input())
matrix = [[1,2,3], [4,5,6], [7,8,9]]
res=spiral_matrix(matrix)
print(res,end='')
