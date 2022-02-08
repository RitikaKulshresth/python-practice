def find_ele_in_array(arr,data):
    for i in range(0,len(arr)):
        if arr[i]==data:
            return i
        else:
            i+=1
    return -1

# n = int(input())
# arr=[]
# for i in range(0, n):
#     arr.append(int(input()))   
# data = int(input())
# print(find_ele_in_array(arr,data))

arr=[3,2,1]
data=1
print(find_ele_in_array(arr,data))

