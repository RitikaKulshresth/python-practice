def pythagorean_triplet(a,b,c):
    max=a

    if max < b:
        max=b
    if max <c:
        max=c
    
    if max==a:
        if a**2==b**2+c**2:
            return True
        else:
            return False
    elif max==b:
        if b**2==a**2+c**2:
            return True
        else:
            return False
    else:
        if c**2==a**2+b**2:
            return True
        else:
            return False


a=int(input())
b=int(input())
c=int(input())
res=pythagorean_triplet(a,b,c)
print(res)

