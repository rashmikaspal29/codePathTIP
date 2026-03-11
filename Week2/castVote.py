votes= {'Alice': 6, 'Bob': 3}

def cast_vote(votes,candidate):
    if candidate not in votes:
        votes[candidate] = 1
    else:
        votes[candidate] += 1 

cast_vote(votes,'Dien')
print(votes)
cast_vote(votes,'Dien')
print(votes)
