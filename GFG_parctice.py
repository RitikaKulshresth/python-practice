def is_valid_ip(x):
    num_s=x.split('.')

    count_str=len(num_s)

    if count_str!=4:
        return 0
    for i in range(0,len(num_s)):
        if num_s[i] =='':
            return 0
        if num_s[i][0]=='0' :
            return 0
        if ord(num_s[i][0]) in range(ord('a'), ord('z')+1):
            return 0       
        if ord(num_s[i][0])  in range(ord('A'), ord('Z')+1):
            return 0
        if int(num_s[i])>=0 and int(num_s[i])<=255 :
            continue
        else:
            return 0
    return 1

str1=['z.b.c.z','5555...555','222.111.111.222','0.0.0.0','300.1.1.222','255.168.0.1','255.2.3.3.255']
for x in str1:
    print(x,is_valid_ip(x))
