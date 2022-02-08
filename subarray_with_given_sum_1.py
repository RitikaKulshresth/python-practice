def subarray_with_givrn_sum(arr,s):
    curr_sum=arr[0]
    start=0
    end=0
    li=[-1, -1]
    i=0
    while(i <=len(arr)):
        if curr_sum==s:
            li[0] = (start+1)
            li[1] = (end+1)
            return li
        if curr_sum < s:
            end+=1
            if end < len(arr):
                curr_sum+=arr[end]
        else:
            curr_sum-=arr[start]
            start+=1
        i+=1
    
    return li
        
arr=[36,95,104,12,123,134]
s=468
print(subarray_with_givrn_sum(arr,s))