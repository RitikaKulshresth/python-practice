def remove_duplicates_from_given_string(str1):
    for i in range(0,len(str1)):
        dict1={}
        result=''
        for x in range(0,len(str1)):
            if str1[x] not in dict1:
                dict1[str1[x]]=1
                result+=str1[x]
            else:
                continue
        return result

str1=['geeksforgeeks','HappyNewYear']
for x in str1:
    print(x,remove_duplicates_from_given_string(x))