def second_Most_Repeated_String_Sequence(arr):
    dict1={}
    largest_fre=[0, 0]
    second_most_Fre=[0, 0]
    for i in range(0,len(arr)):
        if arr[i] not in dict1:
            dict1[arr[i]]=[1,i]
        else:
            dict1[arr[i]][0]+=1
    
    
    
    for ele in dict1:
        if dict1[ele][0]>largest_fre[0] :#3
            second_most_Fre=largest_fre#0
            largest_fre=dict1[ele]#3
        elif dict1[ele][0]>second_most_Fre[0] and dict1[ele][0]!=largest_fre[0]:
            second_most_Fre=dict1[ele]#2

    if second_most_Fre[0]==0:
        return ''
    else:
        return arr[second_most_Fre[1]]
        

arr=['aaa','aaa']
print(second_Most_Repeated_String_Sequence(arr))