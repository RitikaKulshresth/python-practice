
def checkStringEqual(s,p):
    print(s,p)
    if len(s)!=len(p):
        return False

    mp1={}
    for i in range(0,len(p)):
        character = p[i]
        if character in mp1:
            if s[i] != mp1[character]:
                return False
        else:
            mp1[character] = s[i]
    return True

def match_Specific_pattern(arr,pattern):
    list1=[]
    for i in range(0,len(arr)):
        if checkStringEqual(arr[i],pattern)==True:
            list1.append(arr[i])
    return list1


arr=['abb','abc','xyz','xyy']
pattern='foo'
print(match_Specific_pattern(arr,pattern))