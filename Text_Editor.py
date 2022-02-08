def solve( s,res=''):


    new_s = s.replace("<-", ".") 
    print(new_s)
    res = []
    for char in new_s:
        if char == ".":
            if res:
                res.pop()
        else:
            res.append(char)
    return "".join(res)

s = ""
print(solve(s,res=''))
