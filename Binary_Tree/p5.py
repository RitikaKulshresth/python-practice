def pattern5(n):
    mid = n//2 + 1 
    for i in range(0, mid):
        
        for j in range(mid, i+1, -1):
            print('\t',end='')
            
        for k in range(0, i*2+1):
            print('*\t',end='')
            
        print()

    for i in range(0, mid-1):#2

            for j in range(0,):#2,0->2,1 #2,1->2
                print('\t',end='')
                
            for k in range(i, mid):#0-2-->0,1
                print('*\t',end='')
                
            print()

        
n = int(input())
pattern5(n)