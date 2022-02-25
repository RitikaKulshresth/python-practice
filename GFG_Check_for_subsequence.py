def check_for_subsequence(A,B):
    #Time_Complexity(O(N*N))
    i=0
    j=0
    while(i<len(A)):#1
        found=False
        while(j<len(B)):#0
            if A[i] == B[j]:
                j+=1
                found = True
                break
            j+=1
        if found==False:
            return 0
        i+=1
    return 1
        

A='gksrek'
B='geeksforgeeks'
print(check_for_subsequence(A,B))

