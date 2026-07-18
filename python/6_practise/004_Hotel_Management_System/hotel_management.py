class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def display_info(self):
        print(f"Customer Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")


class Room:
    def __init__(self):
        self.room_number = None
        self.room_type = None
        self.room_charge = 0

    def book_room(self):
        print("\n---Room Menu---")
        print("1. Standard (1000/day)")
        print("2. Deluxe (2000/day)")
        print("3. Suite (3000/day)")

        choice = int(input("Enter your room type (1-3): "))
        days = int(input("Enter number of days to stay: "))

        if choice == 1:
            self.room_type = "Standard"
            self.room_charge = 1000 * days
        elif choice == 2:
            self.room_type = "Deluxe"
            self.room_charge = 2000 * days
        elif choice == 3:
            self.room_type = "Suite"
            self.room_charge = 3000 * days
        else:
            print("Invalid choice. Please select a valid room type.")
            return

        print(f"Room booked successfully! Room Type: {self.room_type}, Total Charge: Rs {self.room_charge}")


class Restaurant:
    def __init__(self):
        self.food_bill = 0

    def order_food(self):
        while True:
            print("\n---Food Menu---")
            print("1. Tea Rs(20)")
            print("2. Lunch Rs(150)")
            print("3. Dinner Rs(200)")
            print("0. Back to Main Menu")

            choice = int(input("Enter your food choice (0-3): "))

            if choice == 1:
                self.food_bill += 20
                print("Tea ordered. Current Food Bill: Rs", self.food_bill)
            elif choice == 2:
                self.food_bill += 150
                print("Lunch ordered. Current Food Bill: Rs", self.food_bill)
            elif choice == 3:
                self.food_bill += 200
                print("Dinner ordered. Current Food Bill: Rs", self.food_bill)
            elif choice == 0:
                print("Returning to Main Menu.")
                break
            else:
                print("Invalid choice. Please select a valid food option.")

        print(f"Total Food Bill: Rs {self.food_bill}")


class Hotel(Customer, Room, Restaurant):
    def __init__(self, name, email, phone):
        # Initialize all parent classes
        Customer.__init__(self, name, email, phone)
        Room.__init__(self)
        Restaurant.__init__(self)

    def get_details(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")
        self.name = name
        self.email = email
        self.phone = phone

    def show_bill(self):
        total_bill = self.room_charge + self.food_bill
        print("\n--- Bill Summary ---")
        self.display_info()
        print(f"Room Type: {self.room_type}")
        print(f"Room Charge: Rs {self.room_charge}")
        print(f"Food Bill: Rs {self.food_bill}")
        print(f"Total Bill: Rs {total_bill}")


# Main program
if __name__ == "__main__":
    hotel = Hotel("", "", "")  # temporary; will be filled by get_details()
    hotel.get_details()
    hotel.book_room()
    hotel.order_food()
    hotel.show_bill()