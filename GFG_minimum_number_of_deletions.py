def minimumNoOfDeletion(str1):
    ##DP used not completely solved
    start=0
    end=len(str1)-1
    count=0
    while(start<=end):
        if str1[start]!=str1[end]:
            count+=2
        start+=1
        end-=1
    return count
            
str1="abxbxaba"
print(minimumNoOfDeletion(str1))