from curses.ascii import isalpha


def count_Alphabets(S):
    count=0
    for i in range(0,len(S)):
        if S[i].isalpha():
            count+=1
    return count



S='adjfjh23'
print(count_Alphabets(S))
