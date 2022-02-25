def check_palindromic_string(S):
    start=0
    end=len(S)-1
    while(start<=end):
        if S[start]!=S[end]:
            return 0
        start+=1
        end-=1
    return 1

S='abba'
print(check_palindromic_string(S))

