def  reverse_a_string(s):
    list1=s.split('.')
    final_list=list1[::-1]
    final_string='.'.join(final_list)
    return final_string


str1=['i.like.this.program.very.much','pqr.mno']
for s in str1:
    print(s,reverse_a_string(s))