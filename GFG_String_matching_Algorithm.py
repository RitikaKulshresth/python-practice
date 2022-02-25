def String_Matchin_Algoritm(str1,str2):

    if len(str1)!=len(str2):
            return 0
    if len(str1)>2:

        if str1[2:]+str1[:2]==str2 or str1[-2:]+str1[:-2]==str2:
            return 1
        else :
            return 0




str1='fsbcnuvqhffbsaqxwp'
str2='wpfsbcnuvqhffbsaqx'
print(String_Matchin_Algoritm(str1,str2))