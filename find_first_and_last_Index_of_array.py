def first_and_last_index_in_An_array(num,data):
    left=0
    right=len(num)-1
    
    while(left<=right):
        mid=(left+right)//2

        if data>num[mid]:
            left=mid+1

        elif data<num[mid]:
            right=mid-1

        else:
            li=mid
            ri=mid
            while(data == num[li-1] and li>=0):
                li-=1
            while(data == num[ri+1] and ri<len(num)):
                ri+=1
            return [li,ri]
                 
    
            
num=[10,10,10,20,20,20,20,20,20,50,60,70,80]
data=20
print(first_and_last_index_in_An_array(num,data))