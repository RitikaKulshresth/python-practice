# Input-->["A1B","C2","34B","5F6,"7"]
# ["A1B","C2","34B","5F6"]
#Output-->['1','2','34','56','7']


# import json
class string_Problems:

    def __init__(self,array1):
        self.array1 = array1
          
    def duplicate_char_string(self):
        new_dict1={}
        for ele in self.array1:
            if ele not in new_dict1:
                new_dict1[ele] = 1
            else :
                new_dict1[ele] = new_dict1[ele] + 1
        
        str1=''
        for val in new_dict1:
            
            if new_dict1[val]>1:
                str1+=val 
        return str1
            

        
# input_array1=input("Enter the input:")
input_array1='cccaabbd'
s1 = string_Problems(input_array1)
print(s1.duplicate_char_string())


input_array2='adbxyzcccaabbdx'
s2 = string_Problems(input_array2)
print(s2.duplicate_char_string())