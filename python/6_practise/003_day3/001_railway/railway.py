# create a railway Resevation system
class Train:
    def __init__(self, train_no, train_name, source, destination, seats, fare):
        self.train_no = train_no
        self.train_name = train_name
        self.source = source
        self.destination = destination
        self.totalSeats = seats
        self.available_seats = seats
        self.fare = fare

    def display(self):
        print(f"{self.train_no}\t{self.train_name} \t {self.source}\t{self.destination}\t{self.totalSeats}\t{self.available_seats}\t{self.fare}")


class Reservation:
    def __init__(self, pnr, passenger_name, train, seats, totalFare):
        self.pnr = pnr
        self.passenger_name = passenger_name
        self.train = train
        self.seats = seats
        self.totalFare = seats * train.fare

    def display(self):
        print(f"{self.pnr}\t{self.passenger_name}\t{self.train.train_name}\t{self.seats}\t{self.totalFare}")

class ReservationSystem:
    def __init__(self):
        self.reservations = []
        self.trains = []

    def find_train(self, train_no):
        for train in self.trains:
            if train.train_no == train_no:
                return train
        return None
    
    def find_reservation(self, pnr):
        for reservation in self.reservations:
            if reservation in self.reservations:
                return reservation
        return None
    
    def add_Train(self):
        train_no = int(input("Enter Train Number:"))
        train_name = input("Enter train Name:")
        source = input("Enter source:")
        destination = input("Enter destination:")
        seats = int(input("Enter Total Seats:"))
        fare = float(input("Enter train fare: "))

        self.trains.append(Train(train_no, train_name, source, destination, seats, fare))

        print("Train added successfully!")

    def view_Train(self):
        print("\nTrain No \t train name \t source \t destination \t seats \t fare ")
        print("----------------------------------------------------------------------")

        for train in self.trains:
            train.display()

    # Booking TIcket
    def book_Ticket(self):
        pnr = int(input("pnr number:"))
        passenger = input("Enter passenger name:")
        train_no = int(input("Enter train no:"))
        seats = int(input("Enter Number of seats:"))

        train = self.find_train(train_no)
        if train:
            if seats <= train.available_seats:
                train.available_seats -= seats
                
                reservation = Reservation(
                    pnr, passenger, train, seats
                )
                self.reservations.append(reservation)
                
                print("Ticket Booked Successfully")
                print("Total fare is:", reservation.totalFare)

            else:
                print("Seats not available")
        else:
            print("Train Not Found")

    def cancel_Ticket(self):
        pnr = int(input("Enter pnr number:"))

        reservation = self.find_reservation(pnr)

        if reservation:
            reservation.train.avilable_seats += reservation.seats

            self.reservations.remove(reservation)
           
            print("Ticket Cancelled Successfully")
        else:

            print("Reservation Not Found")

    def view_Reservations(self):
        print("\nPNR\tPassenger\tTrain\tSeats\tFare")
        print("----------------------------------------")

        for reservation in self.reservations:
            reservation.display()

    # Search Train
    def search_Train(self):
        train_no = int(input("Enter Train no to Search: "))
        train = self.find_train(train_no)

        if train:
            print("\nTrain No \t train name \t source \t destination \t seats \t fare")
            print("----------------------------------------------------")
            train.display()
        else:
             print("train not Found")
    def calculate_revenue(self):
        revenue = sum(r.total_fare for r in self.reservations)
        print(f"\n Total Revenue = Rs. {revenue}")

# Main Program 
system = ReservationSystem()

system.add_Train()
system.view_Train()
system.book_Ticket()
system.cancel_Ticket()
system.view_Reservations()
system.search_Train()
system.calculate_revenue()

            


                    