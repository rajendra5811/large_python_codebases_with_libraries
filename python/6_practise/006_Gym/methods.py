#1state change
class Ticket:
    def __init__(self, ticket_price):
        self.ticket_price = ticket_price
    def update_ticket_price(self, ticket_price):
        self.ticket_price = ticket_price
        return True
    
#2Search for a movie
class Movie:
    def __init__(self, movie):
            self.movie = movie
            movies = ["The Batman", "The Flash", "The Marvels", "Barbie", "Oppenheimer"]    
    def search_movie(self, movie1):
         for movie1 in self.movies:
              if movie1 == self.movie:
                   print(f"{self.movie} found")
                   return True
              else:
                    print(f"{self.movie} not found")
                    return False
#3Add method
    def add_movie(self, movie):
        self.movies.append(movie)
        print(f"{movie} added to the list")
        return True
#4Remove method
    def remove_movie(self, movie):
        if movie in self.movies:
            self.movies.remove(movie)
            print(f"{movie} removed from the list")
            return True
        else:
            print(f"{movie} not found in the list")
            return False
        
#5Filter
   """ def available_movies1(self, movie):
         self.available = []
    for movie in self.movies:
         if movie == self.available:
              self.available.append(movie)
        return available"""
         
def available_movies(self):
    self.available = []
    for movie in self.movies:
        if movie.is_available:  # or whatever your availability flag is
            self.available.append(movie)
    return self.available
#display
def display_bookings(self, bookings):
     for booking in self.bookings:
          bookings.display()
def is_available(self, tickets_needed):
        return self.available_seats >= tickets_needed
#Validation
def validate_age(self, age):
     if age >18 or age<100:
          raise ValueError("invalid age")
     else:
           if not self.movie.is_available(self.tickets):
            return False
     return True
#Coordination
def booking_ticket(self, ticket, movie, booking, manager):
     if validate_age():
          return
    # elif search_movie(): return movie
     elif is_available(): 
          
               
def book_ticket(self, pnr, passenger_name, train_no, seats):

    train = self.find_train(train_no)

    if train is None:
        return False

    if seats > train.available_seats:
        return False

    train.available_seats -= seats

    reservation = Reservation(
        pnr,
        passenger_name,
        train,
        seats
    )

    self.reservations.append(reservation)

    return True
     

                                                                                                                                                    