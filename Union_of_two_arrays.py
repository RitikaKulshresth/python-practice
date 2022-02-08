def Union_of_two_array(a,b):
    i=j=0
    li=[]
    while(i<len(a)and j<len(b)):
        if (a[i]==b[j]):
            if len(li)==0:
                li.append(a[i])
            elif len(li)>0 and (a[i]!=li[-1]):
                li.append(a[i])
            i+=1
            j+=1
        elif(a[i]<b[j]):
            if len(li)==0:
                li.append(a[i])
            elif len(li)>0 and (a[i]!=li[-1]):
                li.append(a[i])
            i+=1
        elif(b[j]<a[i] and len(li)>0 and a[i]!=li[-1]):
            if len(li)==0:
                li.append(b[j])
            elif len(li)>0 and (b[j]!=li[-1]):
                li.append(b[j])
            j+=1
    while(i<len(a)):
        if (len(li)>0 and a[i]!=li[-1]):
            li.append(a[i])
        i+=1
    while(j<len(b)):
        if (len(li)>0 and b[j]!=li[-1]):
            li.append(b[j])
        j+=1
    return li
        
a=[1, 2, 3, 4, 5,6]
b=[1, 2, 3,7]
print(Union_of_two_array(a,b))