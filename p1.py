def pattern1(n):
    str1=''
    for i in range(1,n+1):
        for j in range(i,i-1,-1): 
            str1+=str('*\t')
            
        print(str1)
           
pattern1(2)