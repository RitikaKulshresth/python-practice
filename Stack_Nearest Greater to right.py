def Stack_nearest_greater_to_right(arr):
    max=0
    stack=[]
    for i in range(len(arr)-1,-1,-1):
        if arr[i]>max:
            max=arr[i]
            stack.insert(0,max)
    str1=[]
    for ele in range(0,len(arr)):
        if arr[ele]<stack[0]:
            str1.append(stack[0])
        elif arr[ele]==stack[0]:
            stack.pop(0)
            str1.append(-1)

    return str1
            
         
arr=[5,3,8,-2,7]
print(Stack_nearest_greater_to_right(arr))
#[8,8,-1,7,-1]