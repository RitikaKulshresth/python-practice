def getEvenDigitNumbers(arr):
    list1=[]
    for i in range(0,len(arr)):
        num=arr[i]
        count=0
        while (num!=0):
            count+=1
            num=num//10
        
        if count % 2==0:
            list1.append(arr[i])
    return list1



arr=[3,11,4,200]
print(getEvenDigitNumbers(arr))