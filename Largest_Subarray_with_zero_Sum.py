def largest_subarray_with_zero_Sum(arr):
    sum=0
    new_dict={}
    max_length=0

    for i in range(0,len(arr)):
        sum+=arr[i]
        if sum is 0:
            max_length= i + 1
        if sum not in  new_dict:
            new_dict[sum]=i
        else:
            if i-new_dict[sum]>max_length:
                max_length=i-new_dict[sum]
    return max_length


# arr=[15,-2,2,-8,1,7,10,23]
arr=[-1,1,-1,1]
print(largest_subarray_with_zero_Sum(arr))