def stringPatternMatching(S,pat):
    len_of_pat=len(pat)
    pat_hash = hash(pat)
    result=[]
    for i in range(0,len(S)):
        str1 = S[i:i+len_of_pat]
        if hash(str1) == pat_hash and str1 == pat: 
            result.append(str(i+1))
    out = ' '.join(result)
    if out!='':
        return out
    else:
        return -1

    
         
S="batmanandrobinarebat"
pat="bat"
print(stringPatternMatching(S,pat))