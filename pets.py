class Pet():
    def __init__(self,name="NaN",age=0,hunger_level="NaN",playful=False):
        self.name = name
        self.age = age
        self.hunger_level = hunger_level
        self.playful = playful

    def set_pet_name(self,n):
        self.name = n    

    def get_pet_name(self):
        return print(self.name)   


Cat = Pet()    

Cat.get_pet_name()
Cat.set_pet_name("Nija")
Cat.get_pet_name()

