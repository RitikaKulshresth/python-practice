def ispalindrome(i,j,subarr):
    i=0
    j=len(subarr)-1
    while(i<=j):
        if subarr[i]!=subarr[j]:
            return False
        i+=1
        j-=1
    return True
            
def printallpalindrome(st):
    len_of_sub=len(st)
    for i in range(0,len_of_sub):
        for j in range(i,len_of_sub):
            # print(arr[i:j+1])
            str1 = ' '.join(str(e) for e in st[i:j+1])
            if ispalindrome(i,j,str1)==True:
                print(str1)
            
    
st = str(input())
printallpalindrome(st)