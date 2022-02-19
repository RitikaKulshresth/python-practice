#subarray_sum_equals_k
def Subarray_with_given_sum(arr,target):
    hash_map = {}
    curr_sum = 0
    count = 0

    for i in range(0,len(arr)):
        curr_sum += arr[i]
        #if 13 is occuring n number times
        if curr_sum - target in hash_map:
            count += hash_map[curr_sum-target]
        if curr_sum == target:
            count += 1

        if curr_sum in hash_map:
            hash_map[curr_sum] += 1
        else:
            hash_map[curr_sum] = 1
    print(hash_map)

    return count


arr=[1,4,20,3,10,5]
sum=33
print(Subarray_with_given_sum(arr,sum))
