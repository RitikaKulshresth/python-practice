def amendSentence(s):
    res_list=''
    res_list+=s[0].lower()
    for i in range(1,len(s)):
        if s[i].islower():
            res_list+=s[i]
        elif s[i].isupper():
            res_list+=' '+s[i].lower()
    return res_list            
s='BruceWayneIsBatman'
print(amendSentence(s))
