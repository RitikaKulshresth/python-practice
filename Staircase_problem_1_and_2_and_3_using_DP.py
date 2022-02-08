#Input-->[64,25,12,22,11]
#Output-->[11, 12, 22, 25, 64]

class array_Problems:

    def __init__(self,n):
        self.n = n

    def staircase_problem(self):
        res=[1,2,4]
        for i in range(3,n+1):
            out= res[i-1]+res[i-2] +res[i-3]
            res.append(out)
        return res
                
n= 5
s1 = array_Problems(n)
print(s1.staircase_problem())

#Time Complexity--->O(n)
#Space Complexity-->O(n)