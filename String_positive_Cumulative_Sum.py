def Positive_Cumulative_sum(arr):
    sum=0

    list1=[]
    for i in range(0,len(arr)):
        sum+=arr[i]
        if sum < 1:
            continue
        else:
            list1.append(sum)
    return list1


arr=[1, -1, -1, -1, 1]
print(Positive_Cumulative_sum(arr))