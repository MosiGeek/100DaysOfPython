
# class Cats:
#     def __init__(self):
#         self.Attribute = 0

#     def AnotherFunction(self):
#         Action(s)    
        
class Team:
    def __init__(self):
            self.TeamName = "NaN"
            self.TeamOrigin = "NaN"

    def setTeamName(self,name):
          self.TeamName = name    

    def setTeamOrigin(self,origin):
          self.TeamOrigin = origin          


Team1 = Team()

# Team1.TeamName = "Barcelona"
Team1.setTeamName("RealMadrid")
Team1.setTeamOrigin("Spain")

print(Team1.TeamName)
print(Team1.TeamOrigin)