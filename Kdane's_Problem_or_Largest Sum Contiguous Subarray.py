def Kdanes_Problem(arr):
    max_sum=0
    sum_upto_now=0
    len_arr=len(arr)
    for i in range(0,len_arr):
        if sum_upto_now+arr[i] > 0:

            sum_upto_now+=arr[i]
            if sum_upto_now>max_sum:
                max_sum=sum_upto_now
        else:
            sum_upto_now=0

    return max_sum


arr=[5,-3436,-46,-3456,-4637,-100]
print(Kdanes_Problem(arr))

# 5,-3436,-46,-3456,-4637,-100