# Input-->["A1B","C2","34B","5F6,"7"]
# ["A1B","C2","34B","5F6"]
#Output-->['1','2','34','56','7']


# import json
class contigousNumbers_Problems:

    def __init__(self,array1):
        self.array1 = array1
          
    def contigousNumbers_to_array(self):
        out=[]
        arr=self.array1
        list1=arr.replace('[','').replace(']','').split(',')
        print(list1)
        out=[]
        for ele in list1:
            newword = ''
            
            for char in ele:
                if char.isnumeric():
                    newword+=char
            out.append(newword)

        print(out)
                
# input_array1=input("Enter the input:")
input_array1='["A1B","C2","34B","5F6,"7"]'
s1 = contigousNumbers_Problems(input_array1)

print(s1.contigousNumbers_to_array())