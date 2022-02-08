
# def factorial(n):
#     if (n==1 or n==0):
#         return 1 
#     else :
#         return (n * factorial(n - 1))
##Handshake problem-->nC2

def combination(n):
    val = (n* (n-1))//2
    return val
    # nC2 => n-2! * n-1 * n/(2! * n-2!)

def get_identical_twins(arr):
    count=0
    dict1={}
    for i in range(0,len(arr)):
        if arr[i] not in dict1:
            dict1[arr[i]]=1
        else:
            dict1[arr[i]]=dict1[arr[i]]+1

    for i in dict1:
        val = dict1[i]
        if val > 1:
            count += combination(val)

    return count
    
 
arr=[1, 2, 2, 3, 2, 1]
print(get_identical_twins(arr))