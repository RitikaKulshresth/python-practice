def stockSpan(price):
    stack=[price[0]]
    index=[0]
    out=[1]

    for i in range(1,len(price)):
        while (len(stack)>0 and price[i]>stack[0]):
            stack.pop(0)
            index.pop(0)
        
        if len(stack)==0:
            out.append(i+1)
        else:
            out.append(i-index[0])
        # if (len(stack)!=0  and  price[i]<stack[0]):
        #     if len(stack)!=0:
        #         out.append(i-index.pop(0))

        stack.insert(0, price[i])
        index.insert(0, i)
    return out
       
price=[2,5,9,3,1,12,6,8,7]
print(stockSpan(price))
# stack=[9,3]
# index=[2,3]
# out=[1,2,3,1]
#------------------------
#Stack = [12,8,7]
#index = [5,7,8]
# Out--> [1,2,3,1,1,6,1,2,1]
#top chota h toh pop
# len(index)==0 => (i+1)#when stack is empty
# len(index)!=0 => (i-j)#when stack is not empty
#  3-2=1

# out=[1,2,3,1,1,6 ,1,2,1]



