'''
T14 - Programming with User-defined Functions
Your task will be to calculate a user's total holiday cost, which includes the
plane cost, hotel cost, and car-rental cost
'''
import sys


def quit_query(user_quit):
    ''' Quit functionality used during each user input.'''
    if user_quit.upper() == "Q":
        sys.exit("Thank you for using our hotel booking system!".center(79,"_"))

def user_city():
    '''
    User input for city to fly to in a conditional to ensure
    a given city or a quit command is input.

    THIS REPLACES THE PLANE COST FUNCTION AS THE RETURN CONTAINS THE FLIGHT PRICE

    Input: No input
    Return: list containing all relevant info of the user's city
    '''

    while True:
        # Outputs all cities and their countries
        print("\u0332".join("City").ljust(28),"\u0332".join("Country"))
        for info in cities_info:
            print(f"{info[0]}".ljust(22), f"-  {info[1]}")

        # User input for the city they wish to travel to.
        city_flight = input("Please choose a city from the list above to continue "
                            "('Q' to quit): ").title()

        quit_query(city_flight)

        # If user's city is found in the avilable cities, all of the city's hotel info
        # is returned (city name, country, price)
        for city in cities_info:
            if city_flight == city[0]:
                return city

        print("_"*79,"\nThat city is not within our database, please use the list "
            "and try again\n","_"*79)

def integer_checker(input_string):
    ''' 
    Checks user input of integers to ensure they are integers
    between 0 and 90.

    Input: Specific question to the user to input an integer
    Return: User's integer
    '''
    # Conditional to ensure user's input is an integer between \
    # 0 and 90 before continuing.
    while True:
        integer_input = input(input_string)

        quit_query(integer_input)

        # Attempts type conversion to integer and check
        # whether the input is between 0 and 90.
        try:
            integer_input = int(integer_input)

            if 0 <= integer_input <= 90:
                return integer_input

        except ValueError:
            pass
        print("_"*79, "\n\nPlease enter an integer between 0 and 90.\n", "_"*79)

def hotel_cost(int_nights):
    '''
    Calculates the cost of the hotel per night.

    input: User inputted number of nights to stay
    Return: per night cost, total hotel cost
    '''
    hotel_per_night = 32
    total_hotel_cost = int_nights * hotel_per_night

    return hotel_per_night, total_hotel_cost

def car_rental(days_of_rent):
    ''' 
    Calculates the cost of the car rental per day

    Input: User inputted number of days to rent
    Output: Daily car rent price, total rental price
    '''
    car_daily_rent = 50
    total_rental_cost = car_daily_rent * days_of_rent

    return car_daily_rent, total_rental_cost

def holiday_cost(city_info, hotel_info, car_info):
    '''
    Output function to output relevant information to the user for booking

    input: city info (city name, country name, flight price), hotel info( hotel cost per night,
    total hotel cost), and car info( daily car rent, total rent cost)
    Return: The cost of the flight, hotel per night and total, car rental per night
    and total, and the total holiday cost. 
    '''
    print("_"*79,"\n")
    print(f"The price for the flight from London to {city_info[0]} "
          f"in {city_info[1]} is £{city_info[2]}")

    print(f"\nThe price per night at our hotel in {city_info[0]} is £{hotel_info[0]}."
          f"\nBy staying for {num_nights} night(s), you must pay a total of £{hotel_info[1]}.")

    print(f"\nThe price per day of car rental at our hotel is £{car_info[0]}."
          f"\nBy renting for {rental_days} day(s), you must pay a total of £{car_info[1]}.")

    print(f"\nThe total cost of your holiday is £{city_info[2] + hotel_info[1] + car_info[1]}.\n")
    quit_query("q")



print("CoGrammar Hotel".center(79,"_"))
print("Welcome to the CoGrammar hotel! Here are all the cities "
      "home to our hotels:")

cities_info = [
    ["Sydney", "Australia", 1200],
    ["Amsterdam", "Netherlands", 100],
    ["Rio De Janeiro", "Brazil", 1500],
    ["Bangkok", "Thailand", 800],
    ["San Francisco", "United States", 1400],
    ["Kuala Lumpur", "Malaysia", 900],
    ["Dublin", "Ireland", 50],
    ["Warsaw", "Poland", 150],
    ["Reykjavik", "Iceland", 300],
    ["Manila", "Philippines", 1000],
    ["Dallas", "United States", 1300],
    ["Casablanca", "Morocco", 400],
    ["Oslo", "Norway", 200],
    ["Santiago", "Chile", 1100],
    ["Ho Chi Minh City", "Vietnam", 950]
]

user_city_info = user_city()

num_nights = integer_checker("Please enter the number of nights that you'll be "
                             "staying at our hotel ('Q' to quit): ")

rental_days = integer_checker("Please enter the number of days that you'll be "
                              "hiring a car for ('Q' to quit): ")


# Main function that runs subsidiary functions and outputs
# the individual and total cost of the holiday
holiday_cost(user_city_info, hotel_cost(num_nights), car_rental(rental_days))
