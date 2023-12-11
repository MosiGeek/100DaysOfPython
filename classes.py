
# class Cats:
#     def __init__(self):
#         self.Attribute = 0

#     def AnotherFunction(self):
#         Action(s)    
        
class Team:
    def __init__(self,Name,Origin):
            self.TeamName = Name
            self.TeamOrigin = Origin

    def setTeamName(self,name):
          self.TeamName = name    

    def setTeamOrigin(self,origin):
          self.TeamOrigin = origin          


Team1 = Team("","")
Team2 = Team("Orlando Pirates","South Africa")

# Team1.TeamName = "Barcelona"
Team1.setTeamName("RealMadrid")
Team1.setTeamOrigin("Spain")

print(f"Team Name: {Team1.TeamName}")
print(f"Team Origin: {Team1.TeamOrigin}")

print(Team2.TeamName)
print(Team2.TeamOrigin)