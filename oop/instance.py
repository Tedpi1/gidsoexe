class human:
    species = "Homosapiens"
    def __init__(self,name):
        self.name = name
        def greet(self):
            print(f"{self.name} says hello")
my_human = human("dennis")
print(my_human.name)
print(my_human.species)