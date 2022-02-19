def maxSubArraySum(arr):
    sum_upto_now=0
    max_sum=0
    len_arr=len(arr)
    for i in range(0,len_arr):
        if sum_upto_now+arr[i] > 0:

            sum_upto_now+=arr[i]
            if sum_upto_now>max_sum:
                max_sum=sum_upto_now
        else:
            sum_upto_now=0

    if max_sum==0:
        return max(arr)
    return max_sum

    # maxsum = arr[0]
    # cursum = 0
        
    # for i in range(0,len(arr)):
    #     cursum += arr[i]
    #     maxsum = max(cursum, maxsum)
    #     if(cursum < 0):
    #         cursum = 0
    # return maxsum


arr=[-3,-2,-1,-4]
print(maxSubArraySum(arr))