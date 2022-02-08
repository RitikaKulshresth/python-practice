def long_Consequence_Seq(arr):
    max=0
    arr1=set(arr)
    for i in range(0,len(arr1)-1):
        if (arr1[i]-1) in arr1:
            continue
        else:
            count=0
            length=0
            while(arr1[i]+length) in arr1:
                count+=1
                length+=1
            if count>max: 
                max+=count
    return max

arr=[24, 2, 34, 1, 3, 4]
print(long_Consequence_Seq(arr))

