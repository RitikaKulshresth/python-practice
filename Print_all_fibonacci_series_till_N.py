def  fibonacci_Series(num):
    initialEle=0
    next_ele=1 
        
    for ele in range(num):
        print(initialEle)
        initialEle,next_ele = next_ele,initialEle+next_ele

    # return initialEle

num=int(input())
result= fibonacci_Series(num)
# print(result)

# 0,1,1,2,3
# a,b,a+b
#   a,b