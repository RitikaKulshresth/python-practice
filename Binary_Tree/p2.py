
def pattern2(n):
    for i in range(0, n):
        for j in range(n, i, -1):
            print('*\t', end='')
        print()    
        
        
n = int(input())
pattern2(n)