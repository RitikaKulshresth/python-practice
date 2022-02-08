def Count_Strictly_Increasing_Subarrays(arr):
    count=1
    max=1

    for i in  range(0,len(arr)-1):
        prev_char=arr[i]
        curr_char=arr[i+1]
        
        if curr_char > prev_char:
            count+=1
        else:
            if count > max:
                max=count   
            count=1
    if count > max:
        max=count   
    return max
                            
arr=[1,4,5,3,4,1,2,3,4,5,7]
res=Count_Strictly_Increasing_Subarrays(arr)
print(res)