
def solve(n):
    a =0
    b= 1
    li=[]
    for i in range(0,n+1):
        if i ==0 :
            li.append(i)
        elif i ==1:
            li.append(i)
        else:
            a,b=a+b,a #2
            li.append(a) 
    return li[n] 
n=3
print(solve(n))
