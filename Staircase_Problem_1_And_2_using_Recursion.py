

def staircase_problem(n):
    if (n==0):
        return 1
    elif(n < 0):
        return 0
    else:
        return staircase_problem(n-1)+staircase_problem(n-2)  
                
n= 5
# stringval=input(input_array)

print(staircase_problem(n))

#Time Complexity--->O(2^n)
#Space Complexity-->O(n)--Stack