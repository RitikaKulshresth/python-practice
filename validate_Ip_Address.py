import re


def isValid(s):

    num_s=s.split('.')
    count_s=len(num_s)
    if count_s != 4:
        return 0

    for i in range(0,len(num_s)):
        if num_s[i]=='':
            return 0

        if num_s[i][0] == '0' and len(num_s[i])>1:
            return 0
        
        if ord(num_s[i][0]) in range(ord('a'), ord('z')):
            return 0
        
        if ord(num_s[i][0])  in range(ord('A'), ord('Z')):
            return 0

        if int(num_s[i])>=0 and int(num_s[i])<=255 :
            continue
        else:
            return 0
    return 1

str1=['a.b.c.e','1...1','222.111.111.111','5555..555','240.0.0.111','0000.0000.0000.0000','255.168.0.1',]
for s in str1:
    print(s,isValid(s))
