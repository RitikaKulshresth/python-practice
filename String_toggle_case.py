def togglecase(st):
    list1=[]
#write your code here
    for ele in st:
        if ord(ele)>65 and ord(ele)<90:
            chlow=ord(ele)+32
            list1.append(chr(chlow))
        elif ord(ele)>97 and ord(ele)<122:
            chigh=ord(ele)-32
            list1.append(chr(chigh))
    res=''.join(list1)
    return res
if __name__ == '__main__':
    st = input()
    print(togglecase(st))
