def two_sum(arr,target):
    arr1=[]
    dict1={}
    for i in range(0,len(arr)):
        if arr[i] not in dict1:
            dict1[target-arr[i]]=i
        else:
            # arr1.append(dict1[arr[i]],i)
            arr1.append(dict1[arr[i]])
            arr1.append(i)
            return arr1



arr=[1, 3, 3, 4]
target=5
print(two_sum(arr,target))
