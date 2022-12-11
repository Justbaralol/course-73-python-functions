#def make_pizza(*toppings):
#    """The purpose of this function is to make pizza"""
#    print(toppings)

#make_pizza("quadroformaggi")
#make_pizza("cranberries", "extra cheese", "chicken")

def make_pizza(*toppings):
    """Summarizes the pizza we are about to make"""
    print("You pizza is being made with the following toppings: ")
    for topping in toppings:
        print(f" - {topping}")

make_pizza("mushroom", "cheese", "cranberries")
