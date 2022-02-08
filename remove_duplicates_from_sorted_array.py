def remove_duplicates_from_sorted_array(A):
    count=0
    for i in range(len(A)):
        if i<len(A)-1 and A[i]==A[i+1]:
            continue
        else:
            A[count]=A[i]
            count+=1

    while len(A)!=count:
        A.pop()
    return A


     
A=[1,2,2,3,3,4,4,5,5,6,6,6,7,7]
print(remove_duplicates_from_sorted_array(A))