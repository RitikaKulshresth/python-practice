def min_ele_in_rotated_sorted_Array(arr):
    l=0
    r=len(arr)-1
    if (arr[l]<=arr[r]):
        return arr[0]
    while(l<=r):
        mid=(l+r)//2
        if arr[mid+1]<arr[mid]:
            return arr[mid+1]
        elif arr[mid-1]>arr[mid]:
            return arr[mid]
        elif (arr[l]<=arr[mid]):
            l=mid+1
        elif (arr[mid]<=arr[r]):
            r=mid-1

    return -1
        






arr=[2,3,4,5,6,7,8,9,10,1]
print(min_ele_in_rotated_sorted_Array(arr))