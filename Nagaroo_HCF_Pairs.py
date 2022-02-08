def isHcf1(n1,n2):
    factors = 1
    for k in range(2,n1):
        if n1%k==0 and n2%k==0:
            factors+= 1
    if factors == 1:
        return True
    else:
        return False
    
def Count_of_HCF_Pairs(num):
    count=3
    list=[]
    for i in range(1,num):
        for j in range(1,num):
            if isHcf1(i,j):
                list.append((i,j))
                count+=1
            else:
                continue
            
    return count,list

num=5
print(Count_of_HCF_Pairs(num))