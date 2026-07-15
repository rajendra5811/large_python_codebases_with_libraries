"""Cat is an animal"""
class Cat():
       """ A Cat is an Animal."""
def __init__(self, name:str, age:int):
""" Create a new cat.
        Arguments: name {str} --the name of the cat     
           age{int}--the age of the cat in years"""
        self.name = name
        self.age = age
def speak(self) -> None:
        """ Make a cute cat sound. >>> kitty.speak() Spot says purrrr"""
        print(f'{self.name} says, purrrrrr.')
if"__name__"=="__main__":
 import doctest
doctest.testmod(extraglobs={"kitty": Cat('Spot', 3)})
    
