class Shapes:
    def __init__(self,base=0,height=0):
        self.base = base
        self.height = height

    def triangle_area(self):
        return print(1/2*self.base*self.height,"sqr_cm")
    
    def rect_area(self):
        return print(self.base * self.height,"sqr_cm")
    
    # printing a custom message 
    def __str__(self):  
        return "The base and height are "+str(self.base)+" & "+str(self.height)
        
    
Trian1 = Shapes(6,2)    
Rect1 = Shapes(5,8)

Trian1.triangle_area()
Rect1.rect_area()


print(Trian1)
