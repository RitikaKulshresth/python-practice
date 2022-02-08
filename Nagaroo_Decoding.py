def Decoding(num):
    count=1
    start=0
    end=2
    string1=str(num)

    for i in range(0,len(string1)-1):
        if int(string1[start:end])>1 and int(string1[start:end])<26:
            count+=1
        start+=1
        end+=1
    return count
        

num=121
print(Decoding(num))
