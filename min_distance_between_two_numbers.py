import sys
def min_dist_between_two_numbers(arr,x,y):
    m=0
    n=0
    min_dist=100
    for i in range(0,len(arr)):
        if arr[i]==x:
            m==i
        elif arr[i]==y:
            n==i
        res=m-n
        if res<min_dist:
            min_dist==res
    return min_dist


arr=[1,2,3,2]
x=1
y=2
print(min_dist_between_two_numbers(arr,x,y))