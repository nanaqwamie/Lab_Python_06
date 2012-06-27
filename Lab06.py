#archibold_acheampong

import datetime

class Player:
    def __init__(self,firstname,lastname,team=None):
        self.first_name = firstname
        self.last_name = lastname
        self.score = []
        self.team = team
        
    def add_score(self,date,score):
        self.date=date
        #self.score=score
        self.score.append(score)

    def total_score(self):
        total=0
        for i in range [len(score)]:
            total+=score[i]
        return total

    def average_score(self):
        total=0
        for i in range(len(self.score)):
            total+=self.score[i]
        average=total/len(self.score)
        return average

torres=Player('Fernando','Torres','Spain')
torres.add_score((datetime.date(2012,01,01)),0)
torres.add_score((datetime.date(2012,01,02)),0)
torres.add_score((datetime.date(2012,01,03)),1)
torres.add_score((datetime.date(2012,01,04)),0)
torres.add_score((datetime.date(2012,01,05)),1)
print torres.score
print torres.average_score()



class Team:
    def __init__(self,name,league,manager_name,points):
        self.name = name
        self.league = league
        self.manager_name = manager_name
        self.points = points
        self.players = []

    def add_player(self,player):
        self.player = player
        self.players.append(player)

   

    def __str__(self):
        description = self.name+', playing the '+self.league+' and is managed by '+self.manager_name+' has '+ str(self.points)+' points'
        return description

portugal = Team('Portugal','euro2012','jose',4)
spain = Team('Spain','euro2012','alex',3)
espana = spain
torres=Player('Fernando','Torres',spain)
print portugal
print spain
print torres.team
print spain is torres.team

print spain.add_player(torres)
print spain.players
print portugal.players
print spain.players[0].first_name,spain.players[0].last_name

ronaldo=Player('Christiano','Ronaldo',portugal)
print portugal
print ronaldo.team
print portugal is torres.team
print portugal.add_player(ronaldo)
print portugal.players
print portugal.players[0].first_name,portugal.players[0].last_name
