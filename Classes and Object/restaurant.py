# Add an attribute called number_served with a default value of 0 = DONE
# Create an instance called restaurant from this class
# Print the number of the customers the restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of the customers that have been served
# Call this method with a new number and print the value again
# Create a method called increment_number_served() that lets you increment the number of customers who've been served.
# Call this method with any number you like that could represent how many customers were served in, say, a day of business.

#------------------------------------------------------------------------------------------------------


class Restaurant():
    """A class representing a restaurant"""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant"""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant"""
        msg = f"{self} serves wonderful {self.cuisine_type} food"
        print(msg)

    def open_restaurant(self):
        """Introducing the restaurant via message"""
        print(f"The {self.name} is now open")

    def set_number_served(self, number_served):
        """This function will count the number of customers the restaurant has served"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """The purpose of this function is to increment the number of customers served"""
        self.number_served += additional_served
    #    message = input("How many customers have visited?")
    #    print(message)
    #    print(f"The number customers served is: {additional_served}")

#------------------------------------------------------------------------------------------------------

bara_restaurant = Restaurant("muto", "italian")
bara_restaurant.describe_restaurant()
bara_restaurant.open_restaurant()

#print(f"Number of custumers served in Muto restaurant: {bara_restaurant.number_served}")

bara_restaurant.number_served = 30
print(f"Number of custumers served in Muto restaurant: {bara_restaurant.number_served}")

bara_restaurant.increment_number_served(40)
print(f"Number of custumers served in Muto restaurant: {bara_restaurant.number_served}")

bara_restaurant.increment_number_served(60)
print(f"Number of custumers served in Muto restaurant: {bara_restaurant.number_served}")

#------------------------------------------------------------------------------------------------------

#samuel_restaurant = Restaurant("samstaurant", "chinese")
#samuel_restaurant.describe_restaurant()

#------------------------------------------------------------------------------------------------------

#jacob_restaurant = Restaurant("ouioui", "french")
#jacob_restaurant.describe_restaurant


