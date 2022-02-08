def inverse_a_num(num1):
    inv=0
    op=1
    #ip,id,od
    while(num1!=0):
        
        od=num1%10
        ip=od
        id=op
        inv= inv + id* (10**(ip-1))

        num1=num1//10
        op+=1
    return inv


num1=28346751
res=inverse_a_num(num1)
print(res)
