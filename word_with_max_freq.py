#User function Template for python3

def maximumFrequency (S) : 
    #Complete the function
    fa=S.split()
    dict1={}
    max_num=0
    fre=0
    li=[]
    for i in range(0,len(fa)):
        if fa[i] not in dict1:
            dict1[fa[i]]=[1, i]
        else:
            dict1[fa[i]][0]=dict1[fa[i]][0]+1
    print(dict1)
    max_num_lowest_index = 10000

    for ele in dict1: 
        print(dict1[ele][0])
        if dict1[ele][0]>fre or (dict1[ele][0]==fre and dict1[ele][1] < max_num_lowest_index):
            fre=dict1[ele][0]
            max_num=ele
            max_num_lowest_index=dict1[ele][1]

            
    li.append(str(fre))
    li.append(str(max_num))
    result=' '.join(li)

    return result


# s=['the devil in the sky','this is not right']
s='rjs kot w lmy nh fn zo cfg bl m q ms pnt tko iym uo nmx jl vn i sin'
print(maximumFrequency(s))