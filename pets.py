# N.B when inside a class always include a self 
# if we want to access the properties of a class always use a self

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
        return print(self.name)

    def get_pet_age(self):
        return print(self.age)

    def get_pet_hunger(self):
        return print(self.hunger)

    def get_pet_play(self):
        return print(self.playful)


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




Dogido = Dog("Doink", 5, False, False, "Germany Sherpad", "stick")


print(Dogido.wants_to_play())
Dogido.playful = True

print(Dogido.wants_to_play())


Dogido.hunger = True
Dogido.get_pet_hunger()

Dogido.get_pet_name()

print("#######################################################")

Pussy = Cat("Skidy",2,True,True,"Sofa")


print(Pussy.fav_place_to_sit)

Pussy.fav_place_to_sit = "Door Mat"

print(Pussy.fav_place_to_sit)
Pussy.get_pet_name()