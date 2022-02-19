def count_occurence_of_Anagrams(txt,pat):
    end=len(pat)
    dict1={}
    
    final_count=0

    for i in range(0,len(pat)):
        if pat[i] not in dict1:
            dict1[pat[i]]=1
        else:
            dict1[pat[i]]=dict1[pat[i]]+1
    for i in range(0,len(txt)-len(pat)+1):
        dict2={}
        for j in range(i,end+i):#03,14,25
            if txt[j] not in dict2:
                dict2[txt[j]]=1
            else:
                dict2[txt[j]]=dict2[txt[j]]+1
        final_count=final_count+if_Anagram(dict1,dict2)
    return final_count

def if_Anagram(dict1,dict2):
    count=0
    rel_count=0
    for ele in dict2:
        if ele in dict1:
            if dict1[ele]==dict2[ele]:
                count=count+dict1[ele]
            else:
                break
                
    if count==len(pat):
        rel_count=rel_count+1
    else:
        rel_count=0

    return rel_count

        
txt='forxxorfxdofr'
pat='for'
# txt = 'aabaabaa'
# pat = 'aaba'
print(count_occurence_of_Anagrams(txt,pat))
##Time Complexity-->O(n2)



