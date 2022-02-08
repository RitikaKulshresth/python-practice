def rearrange_array_of_positive_and_negative_elements(arr):
    i=0
    j=len(arr)-1
    k=0
    while(i<j):
        while(i<len(arr)-1 and arr[i]>0):
            i+=1
        while(j>=0 and arr[j]<0):
            j-=1
        if (i<j):
            arr[i],arr[j]=arr[j],arr[i]

    print(arr)
    # if i==0 or i==len(arr):
    #     return arr
    ########
    # Negative and positive numbers
    # while(k<len(arr) and i<len(arr)):
    #     if arr[k]>=0 and arr[i]<0:
    #         arr[k],arr[i]=arr[i],arr[k]
    #         k+=2
    #     i+=1

    #[9, 4, 2, 5, 0, -1, -5, -3, -2]

    while(k<len(arr) and i<len(arr)):
        if arr[k]
        
    return arr
           
arr=[9,4,-2,-1,5,0,-5,-3,2]
# arr=[-5,]
print(rearrange_array_of_positive_and_negative_elements(arr))

