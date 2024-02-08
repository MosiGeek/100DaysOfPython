class Pet():
    def __init__(self,name="NaN",age=0,hunger_level="NaN",playful=False):
        self.name = name
        self.age = age
        self.hunger_level = hunger_level
        self.playful = playful

# setters
    def set_pet_name(self,name):
        self.name = name    

    def set_pet_age(self,age):
        self.age = age 

    def set_pet_level(self,level):
        self.hunger_level = level   

    def set_playful(self,play):
        self.playful = play         


# getters
    def get_pet_name(self):
        return print(self.name)   
    
    def get_pet_age(self):
        return print(self.age)  
     
    def get_pet_name(self):
        return print(self.name)   
    
    def get_pet_hunger(self):
        return print(self.hunger_level)   
    
    def get_pet_play(self):
        return print(self.playful)   
        
    
    




Pet_One = Pet("TikiTaka",3,"5",True)    


# Pet_One.get_pet_name()

print(Pet_One.name)

Pet_One.name = "Snowball"

print(Pet_One.name)