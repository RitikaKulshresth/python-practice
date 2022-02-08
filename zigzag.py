def printZigZag(n):
# write your code here
    if(n==1):
        return '1 1 1'
    
    
    outPrev = printZigZag(n-1)
    strn = str(n)
    curr = '{strn} {outPrev} {strn} {outPrev} {strn}'.format(strn=strn, outPrev=outPrev)
    # curr = strn+' '+outPrev + strn + outPrev + strn
    return curr


num = int(input())
print(printZigZag(num))