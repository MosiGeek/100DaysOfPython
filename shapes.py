class Shapes:
    def __init__(self,len,heit):  #more of a constructor
            self.Length = len
            self.Height = heit

    def  triange_area(self,b,h):
       area = 1/2*b*h
       return area
    

Triangle = Shapes(4,2)

print(Triangle.triange_area(Triangle.Length,Triangle.Height),"sqr cm")