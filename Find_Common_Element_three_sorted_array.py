def Find_Common_Element_three_sorted_array(A,B,C):
    prev1=prev2=prev3=0
    
    i=j=k=0
    str1=''

    while (i<len(A) and j<len(B) and k<len(C)):
        while(i<len(A)-1 and A[i]==prev1):
            i+=1
        while(j<len(B)-1 and B[j]==prev2):
            j+=1
        while(k<len(C)-1 and C[k]==prev3) :
            k+=1
        
        if (A[i]==B[j] and B[j]==C[k]):
            str1+=' '+str(A[i])
            prev1=A[i]
            prev2=B[j]
            prev3=C[k]
            i+=1
            j+=1
            k+=1
        elif (B[j]<A[i] and B[j]<=C[k]):
            j+=1
        elif (A[i]<B[j] and A[i]<=C[k]):
            i+=1
        else:
            k+=1
    return str1

    # return (A[i],B[j],C[k])

A=[1, 5, 10, 20, 40, 80]
B=[6, 7, 20, 80, 100]
C=[3, 4, 15, 20, 30, 70, 80, 120]
# A = [3,3,3,2,2,1]
# B = [3,3,2]
# C = [3,3,3,3,2,2,1]


print(Find_Common_Element_three_sorted_array(A,B,C))