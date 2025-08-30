
class Color:

    def __init__(self, name):
        self.name = name

    def describe(self):
        print( f"Color: {self.name}")


class TransparentColor(Color):
    def __init__(self, name, opacity: float):
        super().__init__(name)
        self.opacity = opacity  

    def describe(self):
        print( f"Color: {self.name}, Opacity: {self.opacity * 100:.0f}%")


class Animal:
    def __init__(self, species, color):
        self.species = species
        self.color = color

    def show_info(self) :
        print( f"{self.species} has ") 
        self.color.describe()


if __name__ == "__main__":

    duck = Animal("Duck", Color("Yellow"))

    jellyfish = Animal("Jellyfish", TransparentColor("Blue", 0.3))

    duck.show_info()   
    jellyfish.show_info()
