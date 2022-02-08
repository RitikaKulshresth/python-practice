def count_odd_and_even(arr):
    even_count=0
    odd_count=0
    for i in range(0,len(arr)):
        if arr[i]%2==0:
            even_count+=1
        else:
            odd_count+=1
    return(odd_count,even_count)
    
arr=[1,2,3,4,5]
print(count_odd_and_even(arr))