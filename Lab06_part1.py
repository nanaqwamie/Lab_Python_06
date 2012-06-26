"""
Lab_Python_06
Part 1
"""

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/21/2012	| 1
"""

## create the player_stats data structure

import datetime

a=datetime.date(2012,6,23)
b=datetime.date(2012,6,25)
c=datetime.date(2012,6,19)
d=datetime.date(2012,6,20)
e=datetime.date(2012,6,21)

print str(a)

player_stats={'rooney':[(str(a),2),(str(b),2)],'ronaldo':[(str(c),0),(str(d),3)],'torres':[(str(e),0),(str(e),1)]}
print player_stats


## implement highest_score

def highest_score(player_stats):
    maxi=0
    player=0
    date=0
    for high in player_stats:
        for i in player_stats[high]:
            if i[1]>maxi:
                maxi=i[1]
                player=high
                date=i[0]
    return (maxi,player,date)

print highest_score(player_stats)



## implement highest_score_for_player

def highest_score_for_player(player_stats,player):
    max_score=0
    for high in player_stats[player]:
        if high[1]>max_score:
            max_score=high[1]
    return(max_score,player)
player=raw_input("Please enter the player's name :")
print highest_score_for_player(player_stats,player)




## implement highest_scorer

def highest_scorer(player_stats):

    player_scores = {}
    
    for player in player_stats:
        temp=0
        for i in player_stats[player]:
            print i
            temp+=i[1]
        player_scores[player]=temp
    print player_scores 

    temp_again=0
    player_name=0
    for highest in player_scores:
        print player_scores[highest]>temp_again
        temp_again+=player_scores[highest]
        player_name=highest
    return(temp_again,player_name)

