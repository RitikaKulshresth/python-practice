def validAnagram(anagran_string,list_string):
    dict1={}
    for ele in anagran_string:
        if ele not in dict1:
            dict1[ele] = 1
        else:
            dict1[ele] = dict1[ele] +1

    list_string=list_string.split(',')
    anagrams = []
    
    for word in list_string:
        dict2 = dict1.copy()
        if len(word)!=len(anagran_string):
            continue
        else:
            for val in word:
                if val in dict2:
                    if dict2[val]==1:
                        del dict2[val]
                    else:
                        dict2[val]=dict2[val]-1
            if(len(dict2.keys()) == 0):
                anagrams.append(word)

                ana=','.join(anagrams)
                
    return ana           


        
anagran_string = 'CAT'
list_str='ACT,TAC,DOG,TCA,BOB,JUM'
result= validAnagram(anagran_string,list_str)
print(result)

