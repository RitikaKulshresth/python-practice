class hashmap_Problems:

    def __init__(self, stringval):
        self.stringval = stringval
        # len_String=len(self.stringval)
        

    def high_Freq_Char(self):
        result={}

        for val in self.stringval:
            if val not in result:
                result[val]=1
            else:
                result[val]=result[val]+1
        print(result)

        max_value=list(result.values())[0]
        max_char=list(result.keys())[0]
        # print(max_char)

        for i in result:
             if result[i]>max_value:
                 max_value=result[i]
                 max_char=i
        # print(max_value,max_char)
        return (max_value,max_char)

            # print(val)
    
stringval=input("Input string:")
# print(stringval, "hello")
s1 = hashmap_Problems(stringval)

print(s1.high_Freq_Char())

#abracadabra

