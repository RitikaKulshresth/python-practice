def reverse_of_an_array(num,i,j):
    while(i<=j):
        tmp=num[i]
        num[i]=num[j]
        num[j]=tmp
        i+=1
        j-=1

def rotate_array(num,k):
    
    array_len=len(num)
    k=k%(array_len)

    if k<0:
        k=k+array_len
    
    #part1 reverse
    reverse_of_an_array(num,0,array_len-k-1)
    #part2 reverse
    reverse_of_an_array(num,array_len-k,array_len-1)
    #part3 reverse
    reverse_of_an_array(num,0,array_len-1)

    return num




num=[2,5,6,7,8,9,4]
k=2
print(rotate_array(num,k))


# n = int(input())
# nums=[]
# for i in range(0, n):
#     nums.append(int(input()))   
# k = int(input())



    






