#Input-->[64,25,12,22,11]
#Output-->[11, 12, 22, 25, 64]

class bubble_Problems:

    def __init__(self, stringval):
        self.stringval = stringval

    def swap(self,i,j):
        self.stringval[i],self.stringval[j]=self.stringval[j],self.stringval[i]
        return self.stringval[i],self.stringval[j]

    def bubble_sorting(self):
        for i in range(0,len(self.stringval)):
            for j in range(0,len(self.stringval)-i-1):
                if self.stringval[j]>self.stringval[j+1]:
                    self.swap(j,j+1)

        return self.stringval

input_array= [64,25,12,22,11]
# stringval=input(input_array)
s1 = bubble_Problems(input_array)

print(s1.bubble_sorting())