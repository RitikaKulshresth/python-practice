def reverse_A_Number(num):
    r=''
    while(num!=0): #123
        rem=num%10 #3
        r = r+str(rem)  #3 2 1
        num=num//10 #12
    return r 

num=int(input())
result=reverse_A_Number(num)
print(result)