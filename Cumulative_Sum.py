def cumulative_Sum(arr): #
    sum=0
    arr1=[]
    for i in range(0,len(arr)):
        sum+=arr[i]
        arr1.append(sum)
    return arr1


arr=[1, 2, 3, 4]
print(cumulative_Sum(arr))
