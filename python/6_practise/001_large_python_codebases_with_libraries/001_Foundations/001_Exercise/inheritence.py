class Animal:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
class Cat(Animal):
    isIndoor = True

    def __init__(self, name, age, isIndoor=True):
        super().__init__(name, age)
        """Create a new cat"""
        self.name = name
        self.age = age
        self.isIndoor = isIndoor

    def speak(self):
        """Make the cat pur""
        print("purrr")
        
class Animal:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
class Cat(Animal):
    isIndoor = True

    def __init__(self, name, age, isIndoor=True):
        super().__init__(name, age)
        """Create a new cat"""
        self.name = name
        self.age = age"
        print(f'{self.name} says, "purrrrrr"')
class Frog(Animal):
    def __init__(self,name:str, age:int, color = 'Green'):
    super().__init__(name, age)
        self.color = color
    
        
class Dog(Animal):

    def __init__(self, name:str, age:int, breed:str, weight:int):
        super().__init__(name,age)
        """Create a new dog"""
        self.name = name
        self.age = age
        self.breed = breed
        self.weight = weight

    def speak(self) -> None:
        """Make the dog bark"""
        print(f'{self.name} says, "woof"')

if __name__ == "__main__":
    wiskers = Cat('Wiskers', 3)
    paws = Dog('Mr. Paws', 4, 'dachshund', 18)
    wiskers.speak()
    paws.speak()
    hops = Frog('Hops', 1, 'Blue')
    print(f'The frog is named {hops.name}, is {hops.age} years old, and is the color {hops.color}.')