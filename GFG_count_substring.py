def count_substring(S):
    count=0
    for i in range(0,len(S)):
        if S[i]=='1':
            count+=1
    m=(count*(count-1)//2)
    return m


S='10101'
print(count_substring(S))

#1---0
#2---1
#3---3
#4---6
#5---10
