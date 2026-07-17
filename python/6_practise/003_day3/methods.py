def add_doctor(self, doctor):
    d_id = int(input("enter Doctor ID:"))
    name = input("Enter Doctor Name:")
    specialization = input("Enter Specialization")

    doctor = doctor(d_id, name, specialization)
    self.doctors.append(doctor)
    print("Doctor Added Successfully")
    books = []
    def remove_book(self, book):
        if book in books:
          self.books.remove(book)
          print(f"{self.title} is removed")
    def available_rooms(self):
       rooms = Hotel.avilable
       for rooms in available_rooms
       print(f"{self.rooms}")

    def available_rooms(self):

     available = []

    for room in self.rooms:

        if room.available:

            available.append(room)

    return available
def display_accounts(self):
   print("\n{self.Acctount_number}\t{self.Balance}\t{self.name}\t{self.age}")

def available_doctors(self):

    available = []

    for doctor in self.doctors:

        if doctor.available and len(doctor.patients) < 10:

            available.append(doctor)

    return available

class Bank:

    def __init__(self):
        self.customers = []

    def find_customer_by_pan(self, pan):

        for customer in self.customers:

            if customer.pan == pan:

                return customer

        return None
    