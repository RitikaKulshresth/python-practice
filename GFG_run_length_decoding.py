def run_length_decoding(arr):
    result=''
    num=0
    for i in range(0,len(arr)):
        if ord(arr[i])>=48 and ord(arr[i])<=57:
            num=int(arr[i])
        if ord(arr[i])>=97 and ord(arr[i])<=122:
            result+=arr[i]*num
        if ord(arr[i])>=65 and ord(arr[i])<=90:
            result+=arr[i]*num

    return result



str1=['4B3A2D1C2B']
for x in str1:
    print(x,run_length_decoding(x))