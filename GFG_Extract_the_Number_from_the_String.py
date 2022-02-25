def Extract_the_number_from_the_string(S):
        word_list=S.split()
        valid_list=[]
        max=0
        for word in word_list:
            if word.isnumeric() and '9' not in word:
                valid_list.append(int(word))
        if valid_list==[]:
            return -1
        for i in valid_list:
            if i > max:
                max=i
        if max !='':
            return max



sentence="sdda 999"
print(Extract_the_number_from_the_string(sentence))