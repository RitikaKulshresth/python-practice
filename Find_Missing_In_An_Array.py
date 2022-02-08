def Missing_In_AN_Array(arr,n):
    sum=0
    for i in arr:
        sum+=i
    sum_of_n=n*(n+1)//2
    # print(sum_of_n)
    num=sum_of_n-sum
    return num
n=5
arr=[1,2,3,5]
print(Missing_In_AN_Array(arr,n))