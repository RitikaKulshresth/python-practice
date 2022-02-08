def equilibirium_point(A):
    sum_so_far=0
    lsum=rsum=0
    t_sum=0
    flag=-1

    if len(A)==1:
        return 1
    if len(A)==2 or len(A)==0:
        return -1
    for i in range(0,len(A)):
        t_sum+=A[i]
    
    for i in range(0,len(A)):
        sum_so_far+=A[i]
        lsum=sum_so_far-A[i]
        rsum=t_sum-sum_so_far
        if lsum==rsum:
            flag=i
            return flag+1
        else:
            continue
    return -1


A=[1,3,1,5,2,2,1]
print(equilibirium_point(A))