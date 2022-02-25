def Non_Repeating_Character(S):
    dict1={}
    for i in range(0,len(S)):
        if S[i] not in dict1:
            dict1[S[i]]=[1,i]
        else:
            dict1[S[i]][0]+=1
    print(dict1)
    minF=len(S)
    minIdx=len(S)-1
    for ele in dict1:
        if dict1[ele][0]<minF :
            minF=dict1[ele][0]
            minIdx=dict1[ele][1]
        elif dict1[ele][0]==minF:
            if dict1[ele][1]<minIdx:
                minIdx=dict1[ele][1]
    return S[minIdx]

S='zxvczbtxyzvy'
print(Non_Repeating_Character(S))

#  minF = S.length
#  if dict[ele][0] < minF
#    minF = dict[ele][0] minIdx = dict[ele][1]
#  elif dict[ele][0] == minF
#    if  dict[ele][1] < minIdx:
#        minIdx = 