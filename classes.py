
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

# Team1.TeamName = "Barcelona"
Team1.setTeamName("RealMadrid")
Team1.setTeamOrigin("Spain")

print(f"Team Name: {Team1.TeamName}")
print(f"Team Origin: {Team1.TeamOrigin}")

print(Team2.TeamName)
print(Team2.TeamOrigin)
print(Team3.TeamName)
print(Team3.TeamOrigin)

class Shapes:
    def __init__(self,len,heit):  #more of a constructor
            self.Length = len
            self.Height = heit

    def  triange_area(self,b,h):
       area = 1/2*b*h
       return area
    

Triangle = Shapes(4,2)

print(Triangle.triange_area(Triangle.Length,Triangle.Height))
    
