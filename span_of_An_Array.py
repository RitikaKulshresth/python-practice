def Span_of_an_Array(nums):
    max=nums[0]
    min=nums[0]
    for i in range(0,len(nums)):
        if nums[i]>max:
            max=nums[i]

        if nums[i]<min:
            min=nums[i]
    
    return (max-min)

nums=[5,10,15,70,80,35,90,100,65]
print(Span_of_an_Array(nums))