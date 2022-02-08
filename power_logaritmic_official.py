import sys
sys.setrecursionlimit(1500)

def powerLog(x, n):
# write your code here
    if n==0:
        return 1
    if n%2==0:
        return powerLog(x, n-1//2)*powerLog(x, n-1//2)
    else:
        return powerLog(x, n-1//2)*powerLog(x, n-1//2)*x



num = int(input())
power = int(input())
print(powerLog(num, power))