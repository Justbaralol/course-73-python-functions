#def make_sandwich(*ingredients):
#   """This function receives ingredients the user wishes to add to their sandwich"""
#    print(ingredients)

#make_sandwich("veggies", "ham")
#make_sandwich("cheese", "cranberries", "bacon")
#make_sandwich("chedar", "tomatoes", "mozzarella", "olives")

def make_sandwich(*ingedients):
    """The purpose of this function is to summarize the ingredient the user has requested"""
    print("You sandwich is being made with the following ingredients:")
    for ingredient in ingedients:
        print(f" - {ingredient}")

make_sandwich("veggies", "ham")
make_sandwich("cheese", "cranberries", "bacon")
make_sandwich("chedar", "tomatoes", "mozzarella", "olives")


