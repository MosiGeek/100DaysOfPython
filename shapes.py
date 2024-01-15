class Shapes:
        
    def __init__(self,len,heit,rad):  #more of a constructor
            self.Length = len
            self.Height = heit
            self.Radias = rad
            self.PI = 3.14

    def  triange_area(self,b,h):
       area = 1/2*b*h
       return area
    
    def circle_area(self,r):
         area = self.PI*r*r
         return area

Triangle = Shapes(4,2)

print(Triangle.triange_area(Triangle.Length,Triangle.Height),"sqr cm")