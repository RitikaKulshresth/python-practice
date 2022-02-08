#Input-->aaabbcccddaeeff
#Output-->a3b2c3d2ae2f

class string_Problems:

    def __init__(self, stringval):
        self.stringval = stringval
        
    def rem_Prime_numbers_ArrayList(self):
        string_con=''
        for ele in range(0,int(len(self.stringval))):
            curr_char = self.stringval[ele] 
            prev_char = self.stringval[ele - 1]
            if  curr_char != prev_char :
                string_con += self.stringval[ele]
        
        return string_con



            

stringval=input("Input string:")
s1 = string_Problems(stringval)

print(s1.rem_Prime_numbers_ArrayList())

