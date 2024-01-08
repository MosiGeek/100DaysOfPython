
# class Cats:
#     def __init__(self):
#         self.Attribute = 0

#     def AnotherFunction(self):
#         Action(s)    
        
class Team:
    def __init__(self, Name = "Name", Origin = "Origin"):
            self.TeamName = Name
            self.TeamOrigin = Origin

    def setTeamName(self,name):
          self.TeamName = name    

    def setTeamOrigin(self,origin):
          self.TeamOrigin = origin          


Team1 = Team("","")
Team2 = Team("Orlando Pirates","South Africa")
Team3 = Team()
Team4 = Team("Dynamos","Zimbabwe")

# Team1.TeamName = "Barcelona"
Team1.setTeamName("RealMadrid")
Team1.setTeamOrigin("Spain")

print(f"Team Name: {Team1.TeamName}")
print(f"Team Origin: {Team1.TeamOrigin}")

print(Team2.TeamName)
print(Team2.TeamOrigin)
print(Team3.TeamName)
print(Team3.TeamOrigin)

print(Team4.TeamName,Team4.TeamOrigin)


    
class Player(Team):
      def  __init__(self,playerName="Nan",playerNumber="Nan"):
            Team.__init__(self)
            self.PlayerName = playerName
            self.PlayerNumber = playerNumber
            self.PlayerPoints = 0

Player1 = Player("Christiano","7")
Player2 = Player("Mbappe","11")


Player1.setTeamName("Barcelona")

print(Player1.TeamName,Player1.PlayerName,Player1.PlayerNumber)


Player2.setTeamName("Borusia Dotmut")
Player2.setTeamOrigin("Germany")

print(Player2.TeamName,Player2.TeamOrigin,Player2.PlayerName,Player2.PlayerNumber)
      