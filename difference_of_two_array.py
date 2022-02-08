def difference_of_two_array(a1,a2):
    a3=len(a2)*[0]
    i=len(a1)-1
    j=len(a2)-1
    k=len(a3)-1

    while(j>0):
        if a2[j]-a1[i]<0:
            a2[j-1]-=1
            diff=10+a2[j]-a1[i]
            a3[k]=diff

        else:
            diff=a2[j]-a1[i]
            a3[k]=diff

        i-=1
        j-=1
        k-=1
    
    a3[0]=a2[0]-a1[0]

    # out=''
    # for digit in a3:
    #     out += str(digit)
    # out=int(out)

    num_out=0
    for digit in a3:
        num_out = num_out*10 + digit

    return num_out

num1=[3,2,2]
num2=[3,2,4]
print(difference_of_two_array(num1,num2))