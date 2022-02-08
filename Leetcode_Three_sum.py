def three_sum(arr,target):
    arr.sort()
    print(arr)
    res=[]
    for i,a in enumerate(arr):
        if i >0 and a==arr[i-1]:
            continue
        l=i+1
        r=len(arr)-1
        while(l<r):
            threesum=a+arr[l]+arr[r]
            
            if threesum>0:
                r-=1
            elif threesum<0:
                l+=1
            else:
                res.append([a,arr[l],arr[r]])
                l+=1
                while arr[l]==arr[l-1] and l<=r:
                    l+=1

    return res



        
arr=[-1,0,1,2,-1,-4] #[1, 4, 6, 8, 10, 45]
target=0
print(three_sum(arr,target))



#Time Complexity-->O(nlogn)+O(n^2)===O(N^2)
#Space Complexity-->O(1)