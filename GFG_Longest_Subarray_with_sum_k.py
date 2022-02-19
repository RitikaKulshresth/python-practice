def longest_subarray_with_sum_k(arr,k):
    sum=0
    dict1={}
    max_length=0
    for i in range(0,len(arr)):
        sum+=arr[i]
        if sum == k :
            max_length=i+1
        rsum=sum-k
        if sum not in dict1:
            dict1[sum]=i
        else:
            # if i-dict1[sum-k]>max_length:
            #     max_length=i-dict1[sum-k]
            max_length=max(i-dict1[rsum],max_length)
    return max_length

        
arr=[-1, 2, 3]
k=15
print(longest_subarray_with_sum_k(arr,k))