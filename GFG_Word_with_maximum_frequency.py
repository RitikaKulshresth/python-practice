def word_with_max_frequency(str1):
    dict1={}
    wordList=str1.split()
    for i in range(0,len(wordList)):
        if wordList[i] not in dict1:
            dict1[wordList[i]]=[1,i]
        else:
            dict1[wordList[i]][0]=dict1[wordList[i]][0]+1

    print(dict1)  
    fre=0
    min_lowest_index=10000  
    fre_ele=0
    out_list=[]
    result=''

    for i in dict1:
        if dict1[i][0]>fre or (dict1[i][0]==fre and dict1[i][1]<min_lowest_index) :
            fre=dict1[i][0]
            fre_ele=i
            min_lowest_index=dict1[i][1]

    out_list.append(str(fre_ele))
    out_list.append(str(fre))
    result=' '.join(out_list)
    return result
        
str1=['rjs kot w lmy nh fn zo cfg bl m q ms pnt tko iym uo nmx jl vn i sin','this is not right','the devil in the sky']
for x in str1:
    print('ans=>',x,'=>',word_with_max_frequency(x))