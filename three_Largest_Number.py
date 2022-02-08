# Input-->2 10 15 17 7 18 6 4
#Output-->10,14,17

# Input-->
#11
#10 5 9 1 11 8 6 15 3 12 2
#Output-->8 9 10 11 12

class hashmap_Problems:

    def __init__(self,array1):
        self.array1 = array1
        
    def long_Consequence_Seq(self): 
        dict1={}
        for ele in self.array1:
            dict1[ele]=True
        for val in dict1:
            if val-1 in dict1:
                dict1[ele]=False
            else:
                dict1[ele]=True
        print(dict1)



        
# num1=int(input("Size of n1:"))  
input_array1=input("Input array1:")
array1=input_array1.split()
s1 = hashmap_Problems(array1)

print(s1.long_Consequence_Seq())