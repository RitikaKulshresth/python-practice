

class array_Problems:

    def __init__(self,n):
        self.n = n

    def staircase_problem(self):
        out_array=[1,2]
        for i in range(2,n+1):
            out= out_array[i-1]+out_array[i-2]
            out_array.append(out)
        return out_array
                
n= 5
# stringval=input(input_array)
s1 = array_Problems(n)

print(s1.staircase_problem())

#Time Complexity--->O(n)
#Space Complexity-->O(n)