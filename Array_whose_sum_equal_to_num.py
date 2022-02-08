#Input1-->[1,5,3,6,2,4,4,7]
#Output-->
# 1,7
# 4,4
# 5,3
# 6,2

def pairs_of_sum_equal_to_num(input_array1,sum):
    # count=0
    dict1={}
    for i in input_array1:
        if i not in dict1: # {7:1,3:5,2:6,4:4)
            dict1[sum-i] = i
        else:
            print(i,sum-i)

               
input_array1= [1,5,3,6,2,4,4] 
sum=8
print(pairs_of_sum_equal_to_num(input_array1,sum))

#Time complexity-->O(n)