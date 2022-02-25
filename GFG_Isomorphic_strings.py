def areIsomorpicString(str1,str2):
    # a= [str1.index(x) for x in str1]
    # b= [str2.index(y) for y in str2]
    # return a==b   
    dict1={}
    # dict2={}
    if len(str1)!=len(str2):
        return False
    for i in range(0,len(str1)):
        chr1=str1[i]
        chr2=str2[i]
        if chr1 not in dict1 and chr2 not in dict1:
            dict1[chr1] = chr2
            dict1[chr2] = chr1
        else:
            if (chr1 in dict1 and dict1[chr1] != chr2) or (chr2 in dict1 and dict1[chr2] != chr1):
                return False
        
    return True           
        
str1='pepcoding'
str2='sosherlok'
print(areIsomorpicString(str1,str2))