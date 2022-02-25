def binary_String(S):
    count=0
    print(S)
    for i in range(0,len(S)):
        # print(S[i],type(S[i]))
        if S[i]=='1':
            count+=1
    m=count
    result=(m*(m-1))//2
    return result
S='1111'
print(binary_String(S))