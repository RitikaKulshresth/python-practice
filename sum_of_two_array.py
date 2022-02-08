
def sum_of_two_arrays(arr1,arr2):
    # n1=len(arr1)-1
    # n2=len(arr2)-1

    extra_len = 0
    if (arr1[0]+arr2[0]) > 9:
        extra_len = 1
    new_arr_len = max(len(arr1),len(arr2))+extra_len
    arr3 = [0]*new_arr_len

    i=len(arr1)-1
    j=len(arr2)-1
    k=len(arr3)-1
    carry = 0
    while(k>=0):
        if i>=0:
            num1=arr1[i]
        else:
            num1=0

        if j>=0:
            num2=arr2[j]
        else:
            num2=0
        
        sum = num1 + num2 + carry
        divisor=sum%10
        carry=sum//10
        arr3[k]=divisor
        i-=1
        j-=1
        k-=1
    return arr3

    
# write your code here


# n1 = int(input())
# arr1 = []
# for i in range(n1) :
#     val = int(input())
#     arr1.append(val)

# n2 = int(input())
# arr2 = []
# for i in range(n2) :
#     val = int(input())
#     arr2.append(val)

arr1=[9,2,8]
arr2=[3,4,5]  
print(sum_of_two_arrays(arr1,arr2))