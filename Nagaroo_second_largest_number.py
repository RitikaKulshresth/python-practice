def seconlargest_num(arr):
    largest=arr[0]
    second_largest=arr[0]

    

    for i in range(0,len(arr)):
        if arr[i]>largest :
            second_largest=largest
            largest=arr[i]
        elif arr[i]>second_largest and arr[i]!=largest:
            second_largest=arr[i]
    
    if largest==second_largest:
        return -1

    return second_largest

# arr=[1,2,3,5,4] 
# arr=[5,5, 6,7,1]
arr=[2,2,2]
print(seconlargest_num(arr))