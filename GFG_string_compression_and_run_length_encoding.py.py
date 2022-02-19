def string_compression1(str1):
    result=''
    for i in range(1,len(str1)):
        prev_char=str1[i-1]
        curr_char=str1[i]
        if curr_char!=prev_char:
            result+=prev_char
    result+=str1[-1]
    return result
            
def string_compression2(arr):
    result=''
    count=1
    for i in range(1,len(arr)):
        prev_char=arr[i-1]
        curr_char=arr[i]
        if prev_char == curr_char:
            count+=1
        else:
    #         result+=prev_char+str(count)
    #         count=1
    # result+=arr[-1]+str(count)
    # return result

            if count>1:
                result+=prev_char+str(count)
                count=1
            else:
                result+=prev_char

    if count>1:
        result+=arr[-1]+str(count)
    return result
          
str1=['abbbcdddd','aaaabbbccc']
for x in str1:
    print(x,string_compression1(x))
    print(x,string_compression2(x))