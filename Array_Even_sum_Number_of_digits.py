def getEvenDigitNumbers(arr):
    list1=[]
    for i in range(0,len(arr)):
        num=arr[i]
        sum=0
        while (num!=0):
            rem=num%10
            sum+=rem
            num=num//10
        
        if sum % 2==0:
            list1.append(arr[i])
    return list1



arr=[42, 564, 5775, 34, 123, 454, 1, 5, 45, 3556, 23442]
print(getEvenDigitNumbers(arr))