def rotateNumber(n,k):
    count=0
    div = 1
    mul =1
    org = n
    # k=k-1
    while(n>0):#38
        count+=1 #1
        n=n//10
    
    k=k%count

    print(k, 'k')
    if (k<0):
        k=k + count
    for i in range(0,count):
        if i<k:
            div = div *10
        else:
            mul=mul * 10  

    q = org//div
    r = org%div
    print(q, r)

    rot_num = mul*r+q

    return rot_num

n=int(input())
k=int(input()) 
# n=12345
# k=3
result= rotateNumber(n,k)
print(result)
