class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passengers(self, name):
        if self.empty_seats() == 0:
            return False
        self.passengers.append(name)
        return True
    
    def empty_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
people = ["Harry", "Hermione", "Ron", "Ginny"]

for person in people:
    success = flight.add_passengers(person)
    if success:
        print(f"Add {person} to flight successfully.")
    else:
        print(f"No available seats for {person}.")