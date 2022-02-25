def winner_of_an_election(votes):
    dict1={}
    for i in votes:
        if i not in dict1:
            dict1[votes[i]]=1
        else:
            dict1[votes[i]]+=1






votes=['john','johnny','jackie','johnny','john','jackie','jamie','jamie','john','johnny','jamie',
'johnny','john']
print(winner_of_an_election(votes))