def highest_frequency_character_string(str1):
    dict1={}
    # max_fre=0
    # max_fre_ele=0
    list1=[]
    for i in range(0,len(str1)):
        if str1[i] not in dict1:
            dict1[(str1[i])]=1
        else:
            dict1[(str1[i])]=dict1[(str1[i])]+1

    max_fre= max(dict1.values())

    for i in dict1:
        if dict1[i]==max_fre:
            max_fre_ele=i
            list1.append(max_fre_ele)

    minV = ord('z')
    minC = 'z'

    for i in list1:
        # print(ord(i))
        if ord(i) < minV:
            minV = ord(i)
            minC = i
    return (minC)

str1=['testsample','output']
for x in str1:
    print(x,highest_frequency_character_string(x))