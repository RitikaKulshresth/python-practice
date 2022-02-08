def max_distence_between_same_elements(arr):
    new_dict={}
    max_dist=0
    for i in range(0,len(arr)):
        if arr[i] not in new_dict:
            new_dict[arr[i]]=i
        else:
            dist=i-new_dict[arr[i]]
            if dist > max_dist:
                max_dist=dist

    return max_dist





arr=[3,2,1,2,1,4,5,8,6,7,4,2]
print(max_distence_between_same_elements(arr))