def areIsomorpicString_bidirectional(str1,str2):
    dict1={}
    if len(str1)!=len(str2):
        return False
    for i in range(0,len(str1)):
        chr1=str1[i]
        chr2=str2[i]
        if chr1 not in dict1 and chr2 not in dict1:
            dict1[chr1]=chr2
            dict1[chr2]=chr1
        elif (chr1 in dict1 and chr2 not in dict1) or (chr2 in dict1 and chr1 not in dict1) :
                return False
        elif (chr1 in dict1 and chr2 in dict1):
            return False

    return True        
        
str1='aba'
str2='xyy'
print(areIsomorpicString_bidirectional(str1,str2))