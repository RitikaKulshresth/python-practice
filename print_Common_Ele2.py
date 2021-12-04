#Input-->
#a1=1 1 2 2 2 3 5
#a2= f5f5
#Output
#res  = 1 1 2 2 5

class hashmap_Problems:

    def __init__(self,array1,array2):
        self.array1 = array1
        self.array2 = array2
        # print(self.array1,self.array2 )

        
    def comm_Ele2(self): 
        dict1={}
        for val in self.array1:
            if val not in dict1:
                dict1[val]=1
            else:
                dict1[val]=dict1[val]+1

        print(dict1)
        out=''
        for val in self.array2:
            if val in dict1 and dict1[val] > 0:
                out += val + ' '
                dict1[val]=dict1[val]-1
                
        return out


num1=int(input("Enter size of n1:"))  
input_array1=input("Input array1:")
array1=input_array1.split()
num2=int(input("Enter size of n2:"))
input_array2=input("Input array2:")
array2=input_array2.split()
s1 = hashmap_Problems(array1,array2)

print(s1.comm_Ele2())

