import sys
sys.setrecursionlimit (10000)
def Allindex(arr, idx, x, n,csf):
    arr1=[]
    if idx>n-1:
        return arr1[0]*csf
    if arr[idx]==x:
        iarr=Allindex(arr, idx+1, x, n,csf+1)
        iarr[csf]=idx
        return iarr
    else:
        iarr=Allindex(arr, idx+1, x, n,csf)
        return iarr
        
def main():
    n = int(input())
    arr = []
    for i in range(n) :
        arr.append(int(input()))
    x = int(input())
    ans = Allindex(arr, 0, x, n,csf=0)
    print(ans)
main()