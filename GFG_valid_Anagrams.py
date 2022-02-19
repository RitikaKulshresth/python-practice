def valid_Anagrams(str1,str2):
    dict1={}
    if len(str1)!=len(str2):
        return 'NO'
    for i in range(0,len(str1)):
        if str1[i] not in dict1:
            dict1[str1[i]]=1
        else:
            dict1[str1[i]]=dict1[str1[i]]+1
    print(dict1)


    for chr in str2:
        if chr in dict1:
            dict1[chr]-=1
            if dict1[chr]==0:
                del dict1[chr]
        
    if len(dict1)==0:
        return 'YES'
    else:
        return 'NO'

    

str1='b'
str2='d'
print(valid_Anagrams(str1,str2))