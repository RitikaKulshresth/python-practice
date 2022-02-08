#Sample Input
# 4
# 3 12 13 15
import math
def prime(val):
    count=0
    for i in range(2,val):
        if val%i==0:
            count+=1
            break
    if count==0:
        return True
    else:
        return False

def solution(al):
    print(al)
#write your code here
    res=[]
    i=len(al)-1
    while(i>=0):
        val=al[i]
        print(prime(val))
        if prime(val)==True:
            al.remove(val)
        i-=1
    return al        


n = int(input())
al = []
al = list(map(int, input().split()))
print(solution(al))