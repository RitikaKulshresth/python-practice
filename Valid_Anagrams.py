#Python Program to Check if Two Strings are Anagram whose frequency map is same,length of two string should be same

# Input : s1 = "listen"
#         s2 = "silent"
# Output : The strings are anagrams.


# Input : s1 = "dad"
#         s2 = "bad"
# Output : The strings aren't anagrams



class anagram_Problems:

    def __init__(self, stringval1,stringval2):
        self.stringval1 = stringval1
        self.stringval2= stringval2
        
    def valid_Anagrams(self):
        anagram_dict={}
        if len(self.stringval1) !=len(self.stringval2):
            return 'false'
        for ele in stringval1:
            if ele not in anagram_dict:
                anagram_dict[ele] = 1
            else:
                anagram_dict[ele] = anagram_dict[ele] + 1

        for val in stringval2:
            if val not in anagram_dict.keys():
                return "False"
            else: 
                if anagram_dict[val]==1:
                    del anagram_dict[val]
                else:
                    anagram_dict[val] = anagram_dict[val] - 1

        if len(anagram_dict.keys())==0 :
            return "Valid Anagram"

stringval1=input("Input string1:")
stringval2=input("Input string2:")
s1 = anagram_Problems(stringval1,stringval2)


print(s1.valid_Anagrams())


