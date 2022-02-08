def rotate_a_number(num,k):
    tmp=num
    nod=0
    while(tmp!=0):
        tmp=tmp//10
        nod+=1
    print(nod)#5
    div=1
    mul=1
    for i in range(1,nod+1):
        if i<=k:
            div=div*10
        else:
            mul=mul*10

    rem=num%div
    q=num//div
    out=rem*mul+q
    return out
      
num=35618
k=2
print(rotate_a_number(num,k))