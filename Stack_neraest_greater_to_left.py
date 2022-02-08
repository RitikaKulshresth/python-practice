def Stack_nearest_greater_to_left(arr):
    max=0
    stack=[]
    for i in range(0,len(arr)):
        if arr[i]>=max:
            max=arr[i]
            stack.insert(0,max)

    print(stack)
    str1=[]

    for ele in range(len(arr)-1,-1,-1):
        # print(arr[ele])
        if arr[ele]<stack[0]:
            str1.append(stack[0])
        elif arr[ele]==stack[0]:
            stack.pop(0)
            str1.append(-1)

    return str1[::-1]
        
arr=[5,3,8,-2,7]
print(Stack_nearest_greater_to_left(arr))
#[-1,5,-1,8,8]
