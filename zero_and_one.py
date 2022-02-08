### [0,1,0,0,1,1,1,1,0]--->[0,0,0,0,1,1,1,1,1]
# You are given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array 
# [Basically you have to sort the array]. Traverse array only once.
# 
# #i to end [u]
#j to i-1 [1]
#0 to j-1 [0] 

def swap(arrList,i,j):
    arrList[i], arrList[j]=arrList[j], arrList[i]


def segZeroAndOne(arrList):
    i=0
    j=0
    while(i<len(arrList)):
        if arrList[i]==1:
            i+=1
        else:
            swap(arrList, i, j)
            i+=1
            j+=1
    return arrList
    
arrList=[0,1,0,0,1,1,1,1,0,1]
result=segZeroAndOne(arrList)
print(result)