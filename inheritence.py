class Shapes:
    def __init__(self,base=0,height=0):
        self.base = base
        self.height = height

    def triangle_area(self,b,h):
        self.area = 1/2*b*h
        return print(self.area,"Sqr_CM")
    
Trian1 = Shapes(6,2)    

Trian1.triangle_area(Trian1.base,Trian1.height)
