votes = {"Alice" : 5, "Bob": 3}
def castVote(votes, candidate):
      

        if candidate not in votes:
            votes[candidate] = 1

        else:
            votes[candidate] += 1
    

castVote(votes, 'Gina')
print(votes)
    
