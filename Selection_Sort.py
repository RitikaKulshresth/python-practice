#Input-->[64,25,12,22,11]
#Output-->[11, 12, 22, 25, 64]

class sorting_Problems:

    def __init__(self, stringval):
        self.stringval = stringval

    def swap(self,i,j):
        self.stringval[i],self.stringval[j]=self.stringval[j],self.stringval[i]
        return self.stringval[i],self.stringval[j]

    def selection_sorting(self):
        for i in range(0,len(self.stringval)):
            for j in range(i+1,len(self.stringval)):
                if self.stringval[i]>self.stringval[j]:
                    self.swap(i,j)
                    
        print(self.stringval)
                    
input_array= [64,25,12,22,11]
# stringval=input(input_array)
s1 = sorting_Problems(input_array)

print(s1.selection_sorting())
