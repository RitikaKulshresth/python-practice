def pattern_searching(text,patt):
    
    if patt in text:
        return 1
    else:
        return 0


text="geeksforgeeks"
pat="gfg"
print(pattern_searching(text,pat))