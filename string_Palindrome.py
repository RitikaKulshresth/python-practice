#Input-->NITIN
#Output-->Palindrome

class string_Problems:

    def __init__(self, stringval):
        self.stringval = stringval
        
    def string_Palindrome(self):
        string_con=''
        left= 0
        right= len(self.stringval)-1

        str=''
        while(left<=right):
            if self.stringval[left]== self.stringval[right]:
                left+=1
                right-=1
            else:
                return "Not Palindrome"
        return "Palindrome"
        
stringval=input("Input string:")
s1 = string_Problems(stringval)

print(s1.string_Palindrome())

