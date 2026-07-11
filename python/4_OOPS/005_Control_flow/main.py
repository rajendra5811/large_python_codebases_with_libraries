class car:
  def read_int():
     while True:
        try:
            return int(input("Enter a number"))
        except ValueError:
          print("please enter number again")
  read_int()
  def update_the_database():
      pass
  def commit():
      pass
  def rollback():
      pass
# abc
try: 
    distance = int(input("how far?"))
    car.travel(distance)
    car.rev()
except ValueError as e:
    print(e)
except ZeroDivisionError:
    print("Bad Division")
except (NameError, AttributeError):
    print("Bad name or attribute.")
  
"""
try:
    update_the_database()
except TransactionError:
    rollback()
else:
    commit()"""