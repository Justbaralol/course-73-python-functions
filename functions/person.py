def build_person(first_name, last_name, age = None ):
    """This is an attempt to create a person using return value in python"""
    person = {"first" : first_name.title(), "last": last_name.title()}
    if age:
        person["age"] = age
    return person

human = build_person("bara", "kopackova", age = 15)
print(human)
