# N.B when inside a class always include a self 
# if we want to access the properties of a class always use a self

# a class is just a general way of grouping things that are related together

class Pet:
    def __init__(self, name="NaN", age=0, hunger=False, playful=False):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.playful = playful

    # setters
    def set_pet_name(self, name):
        self.name = name

    def set_pet_age(self, age):
        self.age = age

    def set_pet_hunger(self, level):
        self.hunger = level

    def set_playful(self, play):
        self.playful = play

    # getters
    def get_pet_name(self):
        return self.name

    def get_pet_age(self):
        return self.age

    def get_pet_hunger(self):
        return self.hunger

    def get_pet_play(self):
        return self.playful
    
    def __str__(self):
        return self.name + " is " + str(self.age) + " years old"



class Dog(Pet):
    def __init__(
        self, name, age, hunger, playful, breed, fav_toy
    ):  # think about additional properties we want the dog to have
       
        Pet.__init__(
            self, name, age, hunger, playful
        )  # calling the initializer of the pet class
        self.breed = breed
        self.fave_toy = fav_toy

    def wants_to_play(self):
        return (
            "Dog wants to play with " + self.fave_toy
            if self.playful
            else "Dog does not want to play with " + self.fave_toy
        )

class Cat(Pet):
    def __init__(self,name,age,hunger,playful,place="NaN"):
        Pet.__init__(self,name,age,hunger,playful)
        self.fav_place_to_sit = place


    # # making the cat printable
    # def __str__(self):
    #     return (self.name + " Likes to sit in " + self.fav_place_to_sit)  


class Human():
    def __init__(self,name,pets):
        # what properties do we want the human to have?
        self.name = name
        self.pets = pets

    def hasPets(self):
        if len(self.pets) != 0:
            return "yes"
        else:
            return "no"



Dogido = Dog("Doink", 5, False, False, "Germany Sherpad", "stick")


print(Dogido.wants_to_play())
Dogido.playful = True

print(Dogido.wants_to_play())


Dogido.hunger = True
Dogido.get_pet_hunger()

Dogido.get_pet_name()

print("#######################################################")

# create a typical cat 
Pussy = Cat("Skidy",2,True,True,"Sofa")


print(Pussy.fav_place_to_sit)

# Pussy.fav_place_to_sit = "Door Mat"

Pussy.get_pet_name()


print(Pussy)
print(Dog)


print("###########################################################")

yourAverageHuman = Human("Henrika Nova",[Pussy,Dogido])



print(yourAverageHuman.hasPets())

# print(yourAverageHuman.pets[1])

for i in yourAverageHuman.pets:
    i.set_playful(True)

for j in yourAverageHuman.pets:
    print(j.name)

print(yourAverageHuman.pets[1].breed)    