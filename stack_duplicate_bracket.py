

#Input-->((a+b)+(c+d))-->True
#(a+b)+((c+d))-->False

class stack_Problems:

    def __init__(self, stringval):
        self.stringval = stringval
        
    def duplicate_brackets(self):
        stack=[]
        for i in self.stringval:
            if i == ')':
                if stack[-1] == '(':
                    print("Duplicacy is there ")
                else:
                    while (stack[-1] != '('):
                        stack.pop()

                    stack.pop()
            else:
                stack.append(i)
                
        return "True"

            

stringval=input("Input string:")
s1 = stack_Problems(stringval)

print(s1.duplicate_brackets())

