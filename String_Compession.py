#Input-->aaabbcccddaeeff
#Output-->a3b2c3d2ae2f

class string_Problems:

    def __init__(self, stringval):
        self.stringval = stringval
        
    def string_Compression1(self):
        string_con=''
        for ele in range(0,int(len(self.stringval))):
            curr_char = self.stringval[ele] 
            prev_char = self.stringval[ele - 1]
            if  curr_char != prev_char :
                string_con += self.stringval[ele]
        
        return string_con

    def string_Compression2(self):
        string_con1 = ''
        count = 1
        for ele in range(0,int(len(self.stringval))):

            curr_char = self.stringval[ele] 
            prev_char = self.stringval[ele - 1]

            if (curr_char == prev_char):
                count +=1
            else:
                if count > 1:
                    string_con1 += str(count)
                    count=1
                
                string_con1 += self.stringval[ele] 
        if count > 1:
                    string_con1 += str(count)
                    count=1

        return string_con1

            

stringval=input("Input string:")
s1 = string_Problems(stringval)

print(s1.string_Compression1())
print(s1.string_Compression2())

#abracadabra
