def subarray_problem(arr):
    len_of_sub=len(arr)
    for i in range(0,len_of_sub):
        for j in range(i,len_of_sub):
            # print(arr[i:j+1])
            str1 = ' '.join(str(e) for e in arr[i:j+1])
            print(str1)

      
# n = int(input())
# arr = []
# for i in range(n) :
#     val = int(input())
#     arr.append(val)
arr=[1,2,3]
print(subarray_problem(arr))