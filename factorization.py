import math
class factorization:

    def __init__(self, val):
        self.val = val
        # len_String=len(self.stringval)
        

    def prime_Factorization(self):
        for div in range(2,int(math.sqrt(self.val))+1):
            while(self.val%div == 0):
                self.val=self.val//div
                # print(div)
                print(div)

        if self.val !=1:
            return self.val
    
   
val=int(input("Input value:"))
s1 = factorization(val)

print(s1.prime_Factorization())


