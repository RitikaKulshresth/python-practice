def three_sum(arr,target):
    arr.sort()
    print(arr)
    arr1=[]
    for i in range(0,len(arr)):
        low=i+1
        high=len(arr)-1
        diff=target-arr[i]
        while(low<high):
            if arr[low]+arr[high]==diff:
                return 1
                
            elif arr[low]+arr[high] > diff:
                high-=1
            else:
                low+=1  
    return  0

             
arr=[1, 1, 0, -1, -2] #[1, 4, 6, 8, 10, 45]
target=0
print(three_sum(arr,target))