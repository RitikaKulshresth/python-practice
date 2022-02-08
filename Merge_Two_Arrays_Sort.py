#Input1-->[1,2,5,7,9]
#Input2-->[0,3,4,8,9,10,11]
#Output-->[11, 12, 22, 25, 64]

class sorting_Problems:

    def __init__(self, input_array1,input_array2):
        self.input_array1 = input_array1
        self.input_array2 = input_array2

    def merge_sorting(self):
        input_array3=[]
        i=0
        j=0
        k=0
        
        while i <= len(self.input_array1)-1 and j <= len(self.input_array2)-1:
            if self.input_array1[i]<=self.input_array2[j]:
                input_array3.append(self.input_array1[i])
                i+=1
                k+=1
            else:
                input_array3.append(self.input_array2[j])
                j+=1
                k+=1


        while(i<len(self.input_array1)):
            input_array3.append(self.input_array1[i])
            i+=1
            k+=1

        while(j<len(self.input_array2)):
            input_array3.append(self.input_array2[j])
            j+=1
            k+=1

        return input_array3
                          
input_array1= [1,2,5,7,9]
input_array2= [0,3,4,8,9,10,11]
# stringval=input(input_array)
s1 = sorting_Problems(input_array1,input_array2)

print(s1.merge_sorting())