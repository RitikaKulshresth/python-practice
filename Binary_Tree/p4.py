def pattern2(n):
    for i in range(0, n):
        for j in range(0,i):
            print(' \t',end='')

        for k in range(0, n-i):   
            print('* \t',end='')
        print()

        
n = int(input())
pattern2(n)