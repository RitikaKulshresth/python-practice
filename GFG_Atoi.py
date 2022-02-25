def Atoi(str1):
    isNeg=False
    start=0
    len_of_lo=len(str1)-1
    num=0

    if len(str1)==0:
        return -1

    if str1[0]=='-':
        isNeg=True
        start = 1
        len_of_lo=len(str1)-2

    for i in range(start,len(str1)):
        if ord(str1[i])-ord('0')>=0 and (ord(str1[i])-ord('0'))<=9:
            num=num+(ord(str1[i])-ord('0'))*(10**len_of_lo)
            len_of_lo-=1
        else:
            return -1
    
    if isNeg==True:
        return num*-1

    else:
        return num


        
arr=['','-123','12 3','12$3','12ab','123','0','012']
for x in arr:
    print(x,Atoi(x))