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
       
    def get_pet_hunger(self):
        return print(self.hunger_level)   
    
    def get_pet_play(self):
        return print(self.playful)   
        
class Dog(Pet):
    def __init__(self,name,age,hunger_level,playful,breed,fav_toy): # thing about additional properties we want the dog to have
        Pet.__init__(self,name,age,hunger_level,playful) #calling the initializer of the pet class
        self.breed = breed
        self.fave_toy = fav_toy

    def wants_to_play(self):
        return "Dog wants to play with " + self.fave_toy if self.playful else "Dog does not want to play with " + self.fave_toy



Dogido = Dog("Doink",5,"8",False,"Germany Sherpad", "stick")


print(Dogido.wants_to_play())
Dogido.playful = True

print(Dogido.wants_to_play())


Dogido.get_pet_name()




