# Input-->["A1B","C2","34B","5F6,"7"]
# ["A1B","C2","34B","5F6"]
#Output-->['1','2','34','56','7']
def contigous_number(arr):
    
    list1=arr.replace('[','').replace(']','').split(',')
    # print(list1)
    # list2=arr.replace('[','').replace(']','')
    # print(list2[1])
    out=[]
    for ele in list1:
        new_word=''
        for chr in ele:
            if ord(chr)>=65 and ord(chr)<90:
                continue
            elif ord(chr)>=48 and ord(chr)<=57:
                new_word+=chr
        out.append(new_word)
    return out
        
arr='["A1B","C2","34B","5F6,"7"]'
print(contigous_number(arr))



