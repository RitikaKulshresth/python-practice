def isGood_Or_Bad(S):
    vowels=['a','e','i','o','u','?']
    for i in range(0,len(S)):
        
        if S[i] in vowels:
            count+=1
            if count > 5:
                return 0
        else:
            continue
    for i in range(0,len(S)):
        if S[i] not in 
        count+=1


            


S='bcdaeiou??'
print(isGood_Or_Bad(S))
