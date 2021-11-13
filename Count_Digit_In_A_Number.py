def count_Digits_In_A_Number(num):
    count=0
    while(num!=0):
        num= num//10
        count+=1
    return count




num=int(input())
result=count_Digits_In_A_Number(num)
print(result)