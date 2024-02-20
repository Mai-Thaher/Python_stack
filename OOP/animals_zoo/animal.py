class Animal:
    def __init__(self, name, age,animal_species, health_level=0, happiness_level=0):
        self.name=name
        self.age=age
        self.health_level=health_level
        self.happiness_level=happiness_level
        self.animal_species=animal_species
    def display_info(self):
        print(f"animal name: {self.name}, age: {self.age}, health level: {self.health_level}, happiness level: {self.happiness_level},animal_species: {self.animal_species}")
        return self
        
    def feed(self):
        self.health_level+=10
        self.happiness_level+=10
        return self

class Lion(Animal):
    def __init__(self, name, age, gender,animal_species="lion", health_level=2, happiness_level=4):
        super().__init__( name, age,animal_species, health_level, happiness_level)
        self.gender=gender
    def display_info(self):
        super().display_info()
        return self  
    def feed(self):
        super().feed()  
        return self
    
class Tiger(Animal):
    def __init__(self, name, age, weight,animal_species="tiger" ,health_level=1, happiness_level=2):
        super().__init__( name, age,animal_species, health_level, happiness_level)
        self.weight=weight
    def display_info(self):
        super().display_info()
        return self  
    def feed(self):
        super().feed()  
        return self
    
class Bear(Animal):
    def __init__(self, name, age, color,animal_species="bear",health_level=5, happiness_level=3):
        super().__init__( name, age,animal_species, health_level, happiness_level)
        self.color=color  
    def display_info(self):
        super().display_info()
        return self  
    def feed(self):
        super().feed()  
        return self


    
Jimy=Animal("Jimy", 4, "Monkey")
Jimy.feed().display_info()

    
Jim=Tiger("Jim", 5,200,"Tiger")
Jim.feed().display_info()

lion1=Lion("Lion1", 4,"male","Lion")
lion1.feed().display_info().gender

white_bear=Bear("Anna", 3,"white","Bear")
white_bear.feed().display_info()



