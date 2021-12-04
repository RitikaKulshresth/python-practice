#Input-->
#a1=1 1 2 2 2 3 5
#a2= 1 1 1 2 2 4 5
#Output
#res  = 1  2 5

class hashmap_Problems:

    def __init__(self,array1,array2):
        self.array1 = array1
        self.array2 = array2
        # print(self.array1,self.array2 )

        
    def comm_Unique_Ele(self): 
        dict1={}
        for ele in self.array1:
            if ele not in dict1:
                dict1[ele]=1
            else:
                dict1[ele]=dict1[ele]+1

        # print(dict1)
        out=''
        for val in self.array2:
            # print(type(val))
            if val in dict1:
                out += val + ' '
                del dict1[val]
        return out
 

num1=int(input("Numbers to Enter n1:"))  
input_array1=input("Input array1:")
array1=input_array1.split()
num2=int(input("Numbers to Enter n1:"))
input_array2=input("Input array2:")
array2=input_array1.split()
s1 = hashmap_Problems(array1,array2)

print(s1.comm_Unique_Ele())
