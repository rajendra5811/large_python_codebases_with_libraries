class Cat:
    def __init__(self, name, age, IsIndoor = True):
        self.name = name
        self.age = age
        self.IsIndoor = IsIndoor

    def speak(self):
        print(f'rrrr')
    def __repr__(self):
     return f'<{self.name},{self.age},{self.IsIndoor}>'   
