def valid_Anagrams(a,b):
    dict1={}
    if len(a)!=len(b):
        return False
    for i in range(0,len(a)):
        if a[i] not in dict1:
            dict1[a[i]]=1
        else:
            dict1[a[i]]=dict1[a[i]]+1
    

    for chr in b:
        if chr in dict1:
            dict1[chr]-=1
            if dict1[chr]==0:
                del dict1[chr]
        
    if len(dict1)==0:
        return True
    else:
        return False


str1='b'
str2='d'
print(valid_Anagrams(str1,str2))