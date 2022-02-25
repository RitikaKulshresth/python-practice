def swap(S1,S2):
    count=0
    if len(S1)!=len(S2):
        return False
    dict1={}
    for i in range(0,len(S1)):
        if S1[i] not in dict1:
            dict1[S1[i]]=[1,i]
    print(dict1)        

# def Meta_Strings(S1,S2):
#     for i in range(0,len(S1)):
#         count=0



        