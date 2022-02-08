#Python Program to Check if Two Strings are Anagram whose frequency map is same,length of two string should be same

# Input : s1 = "listen"
#         s2 = "silent"
# Output : The strings are anagrams.


# Input : s1 = "dad"
#         s2 = "bad"
# Output : The strings aren't anagrams

#Input-->
# string1-->ababaddccc
# string2-->bcbecabacd


class string_Problems:

    def __init__(self, stringval1,stringval2):
        self.stringval1 = stringval1
        self.stringval2= stringval2
        
    def two_Strings_K_Anagrams(self):
        anagram_dict={}
        if len(self.stringval1) !=len(self.stringval2):
            return 'false'
        for ele in stringval1:
            if ele not in anagram_dict:
                anagram_dict[ele] = 1
            else:
                anagram_dict[ele] = anagram_dict[ele] + 1

        for val in stringval2:
            if val in anagram_dict:
                anagram_dict[ele] = anagram_dict[ele] - 1
                if anagram_dict[ele] <= 0:
                    del anagram_dict[ele]
            else:
                return False    


        print(anagram_dict)


stringval1=input("Input string1:")
stringval2=input("Input string2:")
s1 = string_Problems(stringval1,stringval2)


print(s1.two_Strings_K_Anagrams())


