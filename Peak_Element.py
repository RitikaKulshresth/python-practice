def peak_Element(arr):
    l=0
    r=len(arr)
    if len(arr)==1:
        return 0
    while(l<=r):
        mid=(l+r)//2
        if mid ==0:
            if arr[mid]>arr[mid+1]:
                return mid
            else:
                l=mid+1
        elif mid==len(arr)-1:
            if arr[mid]>arr[mid-1]:
                return mid
            else:
                r=mid-1
        if arr[mid]> arr[mid-1] and arr[mid]>arr[mid+1]:
            return mid
        elif arr[mid]<arr[mid+1]:
            l=mid+1
        elif arr[mid]<arr[mid-1]:
            r=mid-1



    return -1

arr=[1,2,3]
print(peak_Element(arr))