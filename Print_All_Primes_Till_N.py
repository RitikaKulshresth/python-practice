

'''1. You've to print all prime numbers between a range. 
2. Take as input "low", the lower limit of range.
3. Take as input "high", the higher limit of range.
4. For the range print all the primes numbers between low and high (both included).
Input Format
low 
high
Output Format
n1
n2
.. all primes between low and high (both included)
'''
import math
def printAllPrimes(low,high):
    for num in range(low,high+1):#5
        count=0
#         print(num)
        for i in range(2,int(math.sqrt(num))+1):
            if (num%i==0):
                count+=1
                break

        if count==0:
            print(num)

        else:
            continue
            
                
low=int(input())
high=int(input())
result=printAllPrimes(low,high)
# print(result)