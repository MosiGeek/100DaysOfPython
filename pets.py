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
        
class Dog(Pet):
    def __init__(self,name,age,hunger_level,playful,breed,fav_toy):
        Pet.__init__(self,name,age,hunger_level,playful)
        self.breed = breed
        self.fave_toy = fav_toy

    def wants_to_play(self):
        if self.playful == True:
            return ("Dog want to play with " + self.fav_toy)
        else:
            return ("Dog does not want to play with " + self.fave_toy)


Dogido = Dog("Doink",5,"8",False,"Germany Sherpad", "stick")


print(Dogido.wants_to_play())




