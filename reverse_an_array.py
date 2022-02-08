def reverse_an_array(num):

    i=0
    j=len(num)-1

    while(i<=j):
        tmp=num[i]
        num[i]=num[j]
        num[j]=tmp

        i+=1
        j-=1
    return num
    

num=[1,2,3,4,5,6]
print(reverse_an_array(num))
