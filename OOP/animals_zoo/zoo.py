from animal import *
class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, animal):
        self.animals.append(animal)
        return self
        
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
            return self

zoo1 = Zoo("John's Zoo")
zoo2=Zoo("Mai zoo")
zoo2.add_animal(Tiger("jj",5,500, "tiger"))
zoo2.print_all_info()



zoo1.add_animal(Lion("Fatima",4,"female","lion"))
zoo1.print_all_info()
