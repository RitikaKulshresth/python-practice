
class string_Problems:

    def __init__(self, stringval):
        self.stringval = stringval
        # len_String=len(self.stringval)

    
    def isPalindrome(self,str1):
        left = 0
        right = len(self.stringval)
        while(left<=right):
            ch1= self.stringval[left]
            ch2= self.stringval[right]

            if (ch1 !=ch2):
                return 'false'
            else:
                left=left+1
                right = right-1
                return 'True'

    def palandromic_Substring(self,stringval):
        string_len=len(self.stringval)
        for i in range(0,string_len):
            for j in range(i+1,string_len+1):
                str1=self.stringval[i:j]
                if self.isPalindrome(self,str1) == True:
                    print(str1)

   
stringval=input("Input string:")
s1 = string_Problems(stringval)

print(s1.palandromic_Substring())

#abracadabra