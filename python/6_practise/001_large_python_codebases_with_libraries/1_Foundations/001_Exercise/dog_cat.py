# method speak with class cat , dog 
class Cat():
    def __init__(self, name, age, isIndoor = True):    
     self.name = name
     self.age = age
     self.isIndoor = isIndoor
    def speak(self):
      print(f'{self.name} says,"purrrrr"')
class Age_Error(Exception):
    pass
class Dog():
    def __init__(self, name, age, breed):
      self.name = name
      self.age = age
      self.breed = breed
    def speak(self):
      print(f"{self.name} says,'woof!'")
#herbert = Cat('Herbert', 2)
herbert = Cat(5, -2)
herbert.speak()
print(herbert.isIndoor)
rex = Dog("Rex", 2, 'Terrior')
rex.speak()
print(f'This dog is a {rex.breed}!')

try:
    if herbert.age < 0:
        raise Age_Error("negative age")
except Age_Error:
        print("age is less than 1")
try:
    if ((type(herbert.name)) is not str):
        raise Exception("Name must be a string.")
except:
    print('Bad Cat.')