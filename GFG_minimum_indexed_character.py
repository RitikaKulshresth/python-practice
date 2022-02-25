def minimum_indexed_character(S,patt):
    dict1={}
    for i in range(0,len(S)):
        if S[i] not in dict1:
            dict1[S[i]]=[1,i]
        else:
            dict1[S[i]][0]+=1
    min_Idx=len(S)

    for ele in dict1:
        if ele in patt:
            if dict1[ele][1]<min_Idx:
                min_Idx=dict1[ele][1]

    if  min_Idx != len(S):
        return S[min_Idx]
    else:
        return '$'
S='zsyle'
patt='bjz'
print(minimum_indexed_character(S,patt))