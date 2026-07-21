class Vehicle:
    def __init__(self, vehicle_type, vehicle_number, owner_name, license_plate, balance):
        self.vehicle_type = vehicle_type
        self.vehicle_number = vehicle_number
        self.owner_name = owner_name
        self.license_plate = license_plate
        self.balance = balance

    def get_vehicle_type(self):
        return self.vehicle_type

    def get_vehicle_number(self):
        return self.vehicle_number

    def get_owner_name(self):
        return self.owner_name

    def get_license_plate(self):
        return self.license_plate

    def get_balance(self):
        return self.balance

    def display_vehicle(self):
        print(f"Vehicle Type: {self.vehicle_type}")
        print(f"Vehicle Number: {self.vehicle_number}")
        print(f"Owner Name: {self.owner_name}")
        print(f"License Plate: {self.license_plate}")
        print(f"Balance: {self.balance}")

    def deduct_balance(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Deducted {amount} from balance. New balance: {self.balance}")
        else:
            print("Insufficient balance ")
    
    def add_balance(self, amount):
        self.balance += amount
        print(f"Added {amount} to balance. New balance: {self.balance}")
        return self.balance
    
    class TollTicket:
       def __init__(self, ticket_id, vehicle, toll_amount):
            self.ticket_id = ticket_id
            self.vehicle = vehicle
            self.toll_amount = toll_amount

       def display_ticket(self):
            print(f"Ticket ID: {self.ticket_id}")
            print(f"Vehicle Type: {self.vehicle.get_vehicle_type()}")
            print(f"Vehicle Number: {self.vehicle.get_vehicle_number()}")
            print(f"Toll Amount: {self.toll_amount}")

class TollPlaza:                           
    def __init__(self, vehicles ,toll_tickets):
        self.vehicles = []
        self.toll_tickets = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Vehicle {vehicle.get_vehicle_number()} added to the toll plaza.")

    def find_vehicle(self, vehicle_number):
        for vehicle in self.vehicles:
            if vehicle.get_vehicle_number() == vehicle_number:
                return vehicle
        return None
    
    def remove_vehicle(self, vehicle_number):
        vehicle = self.find_vehicle(vehicle_number)
        if vehicle:
            self.vehicles.remove(vehicle)
            print(f"Vehicle {vehicle_number} removed from the toll plaza.")
        else:
            print(f"Vehicle {vehicle_number} not found in the toll plaza.")

    def show_low_balance_vehicles(self):
        low_balance_vehicles = []
        for vehicle in self.vehicles:
            if vehicle.get_balance() < 50:  # Assuming 50 is the threshold for low balance
                low_balance_vehicles.append(vehicle)
        return low_balance_vehicles

    def collect_toll(self, vehicle_number, toll_amount):
        vehicle = self.find_vehicle(vehicle_number)
        if vehicle:
            if vehicle.get_balance() >= toll_amount:
                vehicle.deduct_balance(toll_amount)
                ticket_id = len(self.toll_tickets) + 1
                toll_ticket = Vehicle.TollTicket(ticket_id, vehicle, toll_amount)
                self.toll_tickets.append(toll_ticket)
                print(f"Toll collected for vehicle {vehicle_number}. Ticket ID: {ticket_id}")
            else:
                print(f"Insufficient balance for vehicle {vehicle_number}. Toll not collected.")
        else:
            print(f"Vehicle {vehicle_number} not found in the toll plaza.")

    def display_tickets(self):
        for ticket in self.toll_tickets:
            ticket.display_ticket()

    def calculate_revenue(self):
        total_revenue = sum(ticket.toll_amount for ticket in self.toll_tickets)
        return total_revenue
    
    def display_vehicles(self):
        for vehicle in self.vehicles:
            vehicle.display_vehicle()
            print("--------------------")

toll_plaza = TollPlaza([], [])
Vehicle1 = Vehicle("Car", "V001", "John Doe", "ABC123", 100)    
Vehicle2 = Vehicle("Truck", "V002", "Jane Smith", "XYZ789", 30)
Vehicle3 = Vehicle("Bus", "V003", "Alice Johnson", "LMN456", 70)
toll_plaza.add_vehicle(Vehicle1)
toll_plaza.add_vehicle(Vehicle2)    
toll_plaza.add_vehicle(Vehicle3)
toll_plaza.display_vehicles()
toll_plaza.collect_toll("V001", 20)
toll_plaza.collect_toll("V002", 40) 
toll_plaza.collect_toll("V003", 50)
toll_plaza.display_tickets()    
toll_plaza.show_low_balance_vehicles()
toll_plaza.calculate_revenue()
toll_plaza.remove_vehicle("V002")
toll_plaza.display_vehicles()
        