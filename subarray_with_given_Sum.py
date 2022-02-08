def subarray_with_givrn_sum(arr,s):
    curr_sum=0
    new_dict={}
    start=0
    end=-1
    for i in range(0,len(arr)):
        curr_sum+=arr[i]
        if curr_sum==s:
            start=0
            end=i
            break
        if (curr_sum-s) not in new_dict:
            new_dict[curr_sum-s]=i
        else:
            start=new_dict[curr_sum-s]+1
            end=i
            break
    if end==-1:
        return ("Not found")
    else:
        return (str(start)+" "+str(end))

arr=[10,15,-5,15,-10,5]
s=5
print(subarray_with_givrn_sum(arr,s))
