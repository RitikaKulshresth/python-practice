import sys
sys.setrecursionlimit (10000)
def Lastindex(arr, idx, x, n):
# Write your code here
    if idx>n-1:
        return -1
    
    
    lidx= Lastindex(arr, idx+1, x, n)
    if lidx!=-1:
        return lidx
    elif arr[idx]==x:
        return idx
    else:
        return -1
    

def main():
    n = int(input())
    arr = []
    for i in range(n) :
        arr.append(int(input()))
    x = int(input())
    ans = Lastindex(arr, 0, x, n)
    print(ans)
main()