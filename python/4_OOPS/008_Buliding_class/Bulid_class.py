class Customer:
    def __init__(self, first_name, last_name, tier=("free", 0)):
       self.first_name = first_name
       self.last_name = last_name
       self._tier = tier[0]
       self._cost = tier[1]
       
    def bill_for(self, months):
          return self._cost * months
          
    
    def can_access(self, content):
        return content['tier'] == 'free' or content['tier'] == self._tier

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def premium(cls, first_name, last_name):
        return cls(first_name, last_name, tier=('premium', 10))
        


if __name__ == '__main__':
    # This won't run until you implement the `Customer` class!
    
    marco = Customer('Marco', 'Polo')  # Defaults to the free tier
    print(marco.name)  # Marco Polo
    print(marco.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
    print(marco.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # False

    victoria = Customer.premium("Alexandrina", "Victoria")  # Build a customer around the ('premium', 10$/mo) streaming plan.
    print(victoria.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
    print(victoria.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # True
    print(victoria.bill_for(5))  # => 50 (5 months at 10$/mo)
    print(victoria.name)  # Alexandrina Victoria