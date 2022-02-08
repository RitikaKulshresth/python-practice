def Stack_nearest_smallest_to_right(arr):
    min=arr[len(arr)-1]
    stack=[]
    for i in range(len(arr)-1,-1,-1):
        if arr[i]<=min:
            min=arr[i]
            stack.insert(0,min)
    print(stack)
    str1=[]
    for ele in range(0,len(arr)):
        if arr[ele]>stack[0]:
            str1.append(stack[0])
        elif arr[ele]==stack[0]:
            stack.pop(0)
            str1.append(-1)

    return str1
            
         
arr=[4,5,2,10,8]
print(Stack_nearest_smallest_to_right(arr))
#[2,2,-1,8,-1]