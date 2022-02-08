def Transition_Point(arr):
    for i in range(0,len(arr)-1):
        if arr[i+1]!=arr[i]:
            return i+1    
    return -1


arr=[0,0,0,0,0]
print(Transition_Point(arr))