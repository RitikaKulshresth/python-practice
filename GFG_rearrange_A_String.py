def rearrange_a_string(S):
    result=''
    sum = 0
    for i in range(0,len(S)):
        asciiValue = ord(S[i])
        if asciiValue >= 65 and asciiValue<=90:
            result+=S[i]
        elif asciiValue >= 48 and asciiValue<=57:
            sum+=int(S[i])

    result=''.join(sorted(result))
    if sum>0:
        return result + str(sum)
    else:
        return result

S='AC2BEW3'
print(rearrange_a_string(S))
#normal sorting-->O(nlogn)