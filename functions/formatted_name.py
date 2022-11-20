def get_formatted_name(first_name, last_name):
    """The purpose of this function is to receive the user's name and return it neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

artist = get_formatted_name("vincent", "van gogh")
print(artist)