def common_prefix(s1,s2):
    min_word_len=min(len(s1),len(s2))
    out=''
    for i in range(0,min_word_len):
        if s1[i]==s2[i]:
            out+=s1[i]
        
        else:
            break
    return out

def longestCommonPrefix(arr):
    out=arr[0]
    for i in range(0,len(arr)):
        str1 = arr[i]
        out=common_prefix(str1,out)  
    if out=='':
        return -1
    else:
        return out

arr=['geeksforgeeks','geeks','geekser','geekszer']
# print(common_prefix('geeks', 'geez'))
print(longestCommonPrefix(arr))