def isomorphic_String(arr1,arr2):
    dict1={}
    dict2={}

    if len(arr1) != len(arr2):
        return False

    for i in range(0,len(arr1)):
        if arr1[i] not in dict1:
            dict1[arr1[i]]=arr2[i]
            print(dict1)
        else:
            key=arr1[i]
            value=dict1[key]
            if value==arr2[i]:
                continue
            else:
                return 'not Isomorphic String'
    return 'Isomorphic String'


arr1=['a','b','a','c','b','a']
arr2=['x','y','x','z','y','x']
print(isomorphic_String(arr1,arr2))
