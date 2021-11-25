def GCD_and_LCM(num1,num2):
    
    opn1=num1
    opn2=num2

    while (num2 % num1 != 0):
        rem = num2 % num1
        num1=num2
        num2=rem
        

    gcd= num2

    lcm = (opn1 * opn2)//gcd

    print(gcd)
    print(lcm)


num1=int(input())
num2 = int(input())
result= GCD_and_LCM(num1,num2)
