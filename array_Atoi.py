def array_Atoi(string):
    # if string[0]<0:
    #     string= string.replace("-", "")
    
    len_of_lo=len(string)-1
    num=0

    isNeg = False
    start = 0
    if len(string)==0:
        return -1

    if string[0]=='-':
        isNeg = True
        start = 1
        len_of_lo=len(string)-2

    for char in range(start,len(string)):

        if ord(string[char])-ord('0')>=0 and ord(string[char])-ord('0')<=9:
            num=num+(ord(string[char])-ord('0'))*(10**len_of_lo)
            len_of_lo-=1
        else:
            return -1
    
    if isNeg:
        return num*-1

    return num

str=['12d456','1234', '-123', 'abc', '12d4', '12 3', '012', '0','']
for s in str:
    print(s,array_Atoi(s))

