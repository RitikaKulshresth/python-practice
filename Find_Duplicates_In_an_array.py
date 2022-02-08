def duplicates_in_an_Array(list1):
    new_dict={}
    for i in list1:
        if i not in new_dict:
            new_dict[i]=1
        else:
            new_dict[i]=new_dict[i]+1
            
                    
    ll=[]
    for i in new_dict:
        if new_dict[i]>1:
            ll.append(i)
    return ll
            



list1=[2,3,1,2,3,3,5,5]
print(duplicates_in_an_Array(list1))