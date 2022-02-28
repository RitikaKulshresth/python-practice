def palindrome_sentence(s):
    out=s.replace(' ', '').replace('.', '').replace(';','')
    # out=''
    # s=s.split()
    # for i in range(0,len(s)):
    #     out+=s[i]
    start=0
    end=len(out)-1
    while(start<=end):
        if out[start]!=out[end]:
            return 0
        start+=1
        end-=1
    return 1   

s='race car'
print(palindrome_sentence(s))