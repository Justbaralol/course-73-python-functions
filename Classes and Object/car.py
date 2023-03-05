class Car:
    """This is a class convening all cars"""

    def __init__(self, make, model, year):
        """This is an attempt to initialize the car as an object"""
        self.make = make.title()
        self.model = model.title()
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        print(f"My dream car is {long_name}")
        return long_name
    
    def read_odometer(self):
        """statement showing distance the car has driven """
    #    print(f"I have already driven {self.odometer_reading} km")

    def increment_odometer(self):
        """The purpose of this method is to allow the user add in kilometers they have driven"""
        #self.odometer_reading += additional_kilometers
        additional_kilometers = input("How many kilometers have you driven today: ")
        print(f"Your total of driven kilometers today is: {additional_kilometers}km")

    def total_kilometers_driven(self, additional_kilometers, total_number_of_kilometers):
        """This method will count all kilometers driven"""
        additional_kilometers += total_number_of_kilometers

    
    
my_car = Car("ferrari", "F40", 1992)
print(my_car.get_descriptive_name())
#my_car.read_odometer()
my_car.increment_odometer()
my_car.total_kilometers_driven()

#xime_car = Car("ford", "ranger", 2003)
#print(xime_car.get_descriptive_name())
#xime_car.increment_odometer()

