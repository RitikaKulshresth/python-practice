def firstLetter_Of_Every_Word(S):
    out=S.split()
    result=''
    for i in range(0,len(out)):
        result+=out[i][0]

    return result


S="geeks for geeks"
print(firstLetter_Of_Every_Word(S))