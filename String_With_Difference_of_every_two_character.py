def printstring(st):
#write your code here
    out=''
    for i in range(0,len(st)-1):
        
        res=ord(st[i+1])-ord(st[i])
        out+=st[i]+''+str(res)+''
    out=out+str(st[len(st)-1])
    
    return out
       
st = 'pepCODinG'
print(printstring(st))
