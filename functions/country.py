def country_capital(country_name, country_capital):
    """The purpose of this function is to return a string formatted answer"""
    country = {"country name" : country_name, "capital": country_capital} 
    return country

countries_names = ["spain", "the czech republic", "germany"]
countries_capital = ["madrid", "prague", "berlin"]
for country in countries_names:
    for capital in countries_capital:
        capital_temp = capital
    print(country, capital_temp)


#countries = country_capital(country,capital)
#print(countries)
#countries = {"spain" : "madrid", "the czech republic" : "prague"
#spain = country_capital("spain", "Madrid")
#czech = country_capital("the Czech Republic", "Prague")
#germany = country_capital("germany", "Berlin")
#print(spain, czech, germany)