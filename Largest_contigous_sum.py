def largest_Contigous_sum(arr):
    maximum_Sum_upto_now=0
    max_sum=0
    for i in range(0,len(arr)):
        if maximum_Sum_upto_now+arr[i]>0:
            maximum_Sum_upto_now+=arr[i]
            if maximum_Sum_upto_now > max_sum:
                max_sum=maximum_Sum_upto_now

        else:
            maximum_Sum_upto_now=0
    return max_sum

arr=[1,2,3,4,5]
print(largest_Contigous_sum(arr))