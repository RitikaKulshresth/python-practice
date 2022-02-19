def Anagram_of_String(str1,str2):
    dict1={}
    count=0
    count1=0
    for i in range(0,len(str1)):
        if str1[i] not in dict1:
            dict1[str1[i]]=1
        else:
            dict1[str1[i]]= dict1[str1[i]]+1

    for ele in str2:
        if ele in dict1:
            dict1[ele]-=1
            if dict1[ele]==0:
                del dict1[ele]           
        else:
            count+=1
    for val in dict1:
        count1=count1+dict1[val]
    final_count=count+count1
            
    return final_count
  
str1='basgadhbfgvhads'
str2='sjdhgvbjdsbhvbvd'
print(Anagram_of_String(str1,str2))