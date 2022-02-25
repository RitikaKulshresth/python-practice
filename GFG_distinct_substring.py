def fun(s):
    dict1={}
    for i in range(0,len(s)):
        if s[i:i+2] not in dict1:
            dict1[s[i:i+2]]=1
    print(dict1)
    count=0
    result_str=''
    for i in dict1:
        if len(i)==2:
            result_str+=i+' '
            count+=1

    return count
s = "XYZ"
print(fun(s))