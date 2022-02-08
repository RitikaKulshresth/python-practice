#i to k [u]
#k+1 to e -->[2]
#j to i-1 [1]
#0 to j-1 [0]
def swap(arrList,i,j):
    arrList[i], arrList[j]=arrList[j], arrList[i]

def segZeroAndOne(arrList):
    i=0
    j=0
    k=len(arrList)-1
    while(i<k):
        if arrList[i]==1:
            i+=1
        elif arrList[i]==0:
            swap(arrList, i, j)
            i+=1
            j+=1
        elif arrList[i]==2:
            swap(arrList, i, k)
            k-=1

        
    return arrList
    
arrList=[0,1,2,0,2,0,2,0,1,1,1,1,1,0,1]
result=segZeroAndOne(arrList)
print(result)