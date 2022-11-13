def describe_pet(pet_name, animal_type = "dog"):
    """The purpose of this function is to describe the user's pet"""
    print(f"\nI have a {animal_type}")
    print(f"\nHe is a boy and his name is {pet_name.title()}")

describe_pet("Noisette")
#describe_pet("capybara", "bara")