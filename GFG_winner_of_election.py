def winner(arr):
    dict1={}
    for i in range(0,len(arr)):
        if arr[i] not in dict1:
            dict1[arr[i]]=1
        else:
            dict1[arr[i]]=dict1[arr[i]]+1
    maxVotes=0
    maxVotesEle=[]
    result=[]
    for i in dict1:
        if dict1[i]>=maxVotes:
            maxVotes=dict1[i]
            maxVotesEle.append(i)
    maxVotesEle.sort()
    result.append(maxVotesEle[0])
    result.append(str(maxVotes))
    return result


votes=['john','johnny','jackie','johnny','john','jackie','jamie','jamie','john','johnny','jamie','johnny','john']
print(winner(votes))