#Input1-->[1,2,5,7,9]
#Input2-->[0,3,4,8,9,10,11]
#Output-->[11, 12, 22, 25, 64]


def merge_sorting(arr, lo, hi):
    if lo == hi:
        ba=[arr[lo]]
        return ba
    mid = (lo + hi)//2
    fsh = merge_sorting(arr,lo,mid)
    ssh = merge_sorting(arr,mid+1,hi)
    return merge_2_sorted(fsh, ssh)


def merge_2_sorted(input_array1, input_array2):
    input_array3=[]
    i=0
    j=0
    k=0
    
    while i <= len(input_array1)-1 and j <= len(input_array2)-1:
        if input_array1[i]<=input_array2[j]:
            input_array3.append(input_array1[i])
            i+=1
            k+=1
        else:
            input_array3.append(input_array2[j])
            j+=1
            k+=1

    while(i<len(input_array1)):
        input_array3.append(input_array1[i])
        i+=1
        k+=1

    while(j<len(input_array2)):
        input_array3.append(input_array2[j])
        j+=1
        k+=1

    return input_array3
     
                          
input_array2= [0,3,4,8,9,10,11]
# stringval=input(input_array)

print(merge_sorting(input_array2, 0, len(input_array2)-1))