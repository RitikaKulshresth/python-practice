import re


def ispar(x):
        # code here
        dict1={'(':')','{':'}','[':']'}
        stack=[]
        for char in x:
            if char=='{' or char == '[' or char =='(' :
                stack.append(char)
            elif char=='}' or char==']' or char ==')':
                if len(stack)==0:
                    return "not balanced "
                else:
                    top_ele_open=stack[-1]
                    if char == dict1[top_ele_open]:
                        stack.pop()
                    else:
                        return "not balanced"
    
    
        if len(stack) == 0:
            return "balanced"
        else:
            return 'not balanced'


str1=['{}{(}))}','(','{([])}','()','([]']
for x in str1:
    print(x,ispar(x))