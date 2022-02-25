def replace_a_word(S,oldW,newW):
    return S.replace(oldW,newW)
    # newS=S.split()
    # out=''
    # for i in range(0,len(newS)):
    #     # print(type(newS[i]))
    #     newS[i].replace(oldW,newW)
    # return newS
S="xxforxx xx for xx"
oldW='xx'
newW='Geeks'
print(replace_a_word(S,oldW,newW))