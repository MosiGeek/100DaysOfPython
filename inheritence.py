class Shapes:
    def __init__(self,base=0,height=0):
        self.base = base
        self.height = height

    def triangle_area(self):
        return print(1/2*self.base*self.height,"sqr_cm")
        
    
Trian1 = Shapes(6,2)    

Trian1.triangle_area()
