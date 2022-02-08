import numpy as np
def pascal_triangle(n):
    m=n+1
    li=[0]*m
    li[0]=1
    for i in range(0,m-1):
        factor = (n-i)/(i+1)
        li[i+1]= round(li[i]*(factor))
    return li
n= 5
print(pascal_triangle(n-1))                                                                                                                                 