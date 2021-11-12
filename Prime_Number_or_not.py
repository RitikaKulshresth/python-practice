import math
def primeAndNotPrime(n):
    count=0
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i==0):
            count+=1

    if count==0:
        return('Prime')
    else:
        return('Not Prime')



t=int(input())
for i in range(t):
    n= int(input())
    result=primeAndNotPrime(n)
    print(result)