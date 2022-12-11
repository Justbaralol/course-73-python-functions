def country_capital(country_name, capital_name):
    """This function uses lists"""


    country_name = list(map(str, input("Enter names of some countries: ").split()))
    #firstcountry, secondcountry, thirdcountry, fourthcountry, fifthcountry = input("Can you please tell me a name of some countries: ").split()
    #country_name.append(firstcountry, secondcountry, thirdcountry, fourthcountry, fifthcountry .format(firstcountry, secondcountry, thirdcountry, fourthcountry, fifthcountry))


    capital_name = list(map(str, input("Enter names of their capitals in the same order: ").split()))
    #firstcapital, secondcapital, thirdcapital, fourthcapital, fifthcapital = ("Can you please tell me a name of their capitals in the same order: ").split()
    #capital_name.append(firstcapital, secondcapital, thirdcapital, fourthcapital, fifthcapital .format(firstcapital, secondcapital, thirdcapital, fourthcapital, fifthcapital))

    #countries = {firstcountry[0] : firstcapital[0], secondcountry[1] : secondcapital[1], thirdcountry[2] : thirdcapital[2], fourthcountry[3] : fourthcapital[3], fifthcountry[4] : fifthcapital[4]}
    #print(countries)

    information = {}
    for country in country_name:
        for capital in capital_name:
            information[country] = capital
            capital_name.remove(capital)
            break

    print("Countries and their capitals: " + str(information).title())

country_capital("","")

    
