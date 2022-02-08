
def solve(nums):
    dict1={}
    if len(nums)<3:
        return False
    if len(nums)>=3:

        for i in nums:
            if i not in dict1:
                dict1[i**2]=i
        
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                sum= nums[i]**2+nums[j]**2
                # print(sum)
                if sum in dict1:
                    return True
        return False

nums = [1,2,1]
print(solve(nums))

