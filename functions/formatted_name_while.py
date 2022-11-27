def get_formatted_name(first_name, last_name):
    """The purpose of this function is to receive the user's name and return it neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

#this is an infinite loop
while True:
    print("\nPlease tell me your name: ")
    print("Enter 'q' if you wish to exit the program")
    f_name = input("First name: ")
    if f_name == "q":
        break
    elif f_name == "Q":
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break
    elif l_name == "Q":
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name.title()}!")

    #if formatted_name == "q":
    #    break
    
#artist = get_formatted_name("vincent", "van gogh")
#print(artist)