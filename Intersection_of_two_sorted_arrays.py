def intersection_of_two_sorted_arrays(a,b):
    dict1={}
    li=[]
    count=0
    for i in range(0,len(a)):
        if a[i] not in dict1:
            dict1[a[i]]=1
        else:
            dict1[a[i]]+=1
    
    for j in range(0,len(b)):
        if b[j] in dict1:
            count+=1
            del dict1[b[j]]

    return count
        

a=[1, 2, 3, 4, 5, 6]
b=[3, 4, 5, 6, 7]
print(intersection_of_two_sorted_arrays(a,b))