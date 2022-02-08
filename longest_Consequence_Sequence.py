# Input-->
#11
#10 5 9 1 11 8 6 15 3 12 2
#Output-->8 9 10 11 12

class hashmap_Problems:

    def __init__(self,array1):
        self.array1 = array1
        
    def long_Consequence_Seq(self): 
        dict1={}
        out=''
        for ele in self.array1:
            dict1[ele]=True
        for val in dict1:
            value = str(int(val)-1)
            if value in dict1:
                dict1[val]=False
            else:
                dict1[val]=True
            
        for val in dict1:
            if dict1[val] == True:
                out +=val + ''
                value=str(int(val)+1)
                if value in dict1:
                    out +=val + ''

        # print(dict1)

     
num1=int(input("Size of n1:"))  
input_array1=input("Input array1:")
array1=input_array1.split()
s1 = hashmap_Problems(array1)

print(s1.long_Consequence_Seq())

#10 5 9 1 11 8 6 15 3 12 2