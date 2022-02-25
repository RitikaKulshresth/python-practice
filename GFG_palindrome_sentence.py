def palindrome_sentence(s):
    out=''
    s=s.split()
    for i in range(0,len(s)):
        out+=s[i]
    start=0
    end=len(s)-1
    while(start<=end):
        if s[start]!=s[end]:
            return False
        start+=1
        end-=1
    return True   

s='race car'
print(palindrome_sentence(s))