def binary_serach(num,data):
    left=0
    right=len(num)-1
    # print('ll->',left)

    while(left<=right):
        mid=(left+right)//2

        if data>num[mid]:
            left=mid+1

        elif data<num[mid]:
            right=mid-1

        else:
            return mid
            
    return False
            

num=[10,20,35,40,45,55,60,65,75,89,90,100,110]
data=80
print(binary_serach(num,data))