
# Input-->["A1B","C2","34B","5F6,"7"]
# ["A1B","C2","34B","5F6"]
#Output-->['1','2','34','56','7']


# import json
class array_Problems:

    def __init__(self,array1):
        self.array1 = array1
          
    def rem_duplicates_from_array(self):
        new_dict1={}
        for ele in self.array1:
            if ele not in new_dict1:
                new_dict1[ele] = 1
            else :
                new_dict1[ele] = new_dict1[ele] + 1

        list1=[]
        for val in new_dict1:
            if val not in list1:
                list1.append(val)
            new_dict1[val] = new_dict1[val] - 1

        return list1
        
# input_array1=input("Enter the input:")
input_array1=['4','1','2','3','4','2','9']
s1 = array_Problems(input_array1)

print(s1.rem_duplicates_from_array())