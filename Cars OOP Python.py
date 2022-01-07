# Creating Classes for cars.

# Main Vehicle class

class Vehicle:
    # Class Attribute
    color = "White"

    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers" 

class Bus(Vehicle):
    # Attribute for busses only
    School_name : str
    Capacity : int
    # Assigning default value of seats
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity)

class Car(Vehicle):
    pass
    

# Setting the information into the Bus class whihc inherits the attributes from the Vehicle class. You have to call the different inheritances to print them. NB!!!
BusX = Bus("School Volvo",120,200000)
BusX.School_name = "Bridgeton"
BusX.color = "Red"


# This is wrong XXXX
# print(BusX)

# This is right.
print("Vehicle color: "+BusX.color+"\nVehicle name: "+BusX.name+"\n"+"Vehicle speed: ",BusX.max_speed,"\nVehicle mileage: ",BusX.mileage,"\nSchool name: "+BusX.School_name)
print(BusX.seating_capacity(100))

#BusX.School_name, BusX.color = "Bridgeton", "Red"

    
