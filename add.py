import csv
import os

# Importing required modules
import view


# For making some bold print
class add:
    bold = '\033[1m'
    end = '\033[0m'


# Clear function depending on operating system
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Calculating 'multiplier' for price determination
def mplier_calc(size):
    if size == "small":
        cls()
        return 1
    elif size == "medium":
        cls()
        return 1.1
    elif size == "large":
        cls()
        return 1.15


# Returns the price of a package
def pricing(zone, weight, package, mplier):

    # Sets 'r' to appropriate row index for CSV file reading
    if 0 < weight <= 500:
        r = 1
    elif 500 < weight <= 1000:
        r = 2
    elif 1000 < weight <= 1500:
        r = 3
    elif 1500 < weight <= 2000:
        r = 4
    elif 2500 <= weight <= 3000:
        r = 1
    elif 3000 < weight <= 5000:
        r = 2
    elif 5000 < weight <= 10000:
        r = 3
    elif 10000 < weight <= 15000:
        r = 4
    elif 15000 < weight <= 20000:
        r = 5

    if package == "letter":
        with open('letter_pricing.csv') as f:
            data = list(csv.reader(f))  # Reads data from pricing as a list

    if package == "parcel":
        with open('parcel_pricing.csv') as f:
            data = list(csv.reader(f))  # Reads data from pricing as a list

    return round(float(data[int(r)][int(zone)]) * mplier, 2)  # Uses index to locate the price, and applies multiplier


# Inputting package type
def package_input():
    while True:
        package = input("Letter (L) or Parcel (P)? ").upper()
        cls()
        if package == "L" or package == "l":
            package = "letter"
            cls()
            return package
        elif package == "P" or package == "p":
            package = "parcel"
            cls()
            return package
        else:
            print("Please enter L for letter, or P for parcel." + '\n')
            continue


# Inputting weight of letter/parcel
def weight_input(package):
    if package == "letter":
        while True:
            weight = input("How many" + " grams " + "is your letter? ")
            cls()
            if not weight.isdigit():
                print("Weight must be entered with digits only." + '\n')
                continue
            elif int(weight) > 2000:
                print("Letters can have a maximum weight of 2000g (2kg)." + '\n')
                continue
            elif int(weight) <= 0:
                print("Letters must be above 0g in weight." + '\n')
                continue
            else:
                return int(weight)

    if package == "parcel":
        while True:
            weight = input("How many" + " grams " + "is your parcel? ")
            cls()
            if not weight.isdigit():
                print("Weight must be entered with digits only." + '\n')
                continue
            if not 2500 <= int(weight) <= 20000:
                print("Parcels must be in between, or equal to, 2500g and 20000g (2.5kg and 20kg)." + '\n')
                continue
            else:
                return float(weight)


# Inputting size of package
def size_input(package):
    while True:
        size = input("What is the size of your " + package + "? (S, M or L) ").upper()
        cls()
        if size == "S":
            size = "small"
            cls()
            break
        elif size == "M":
            size = "medium"
            cls()
            break
        elif size == "L":
            size = "large"
            cls()
            break
        else:
            print("Please enter S, M or L depending on the size of your " + package + "." + '\n')
            continue

    return size


# Inputting country of destination (also returning zone)
def country_input(package):
    while True:
        country = input("Please enter the country of destination for this " + package + ": ").title()
        cls()
        if country_zone(country)[0] == "Z":  # If first letter of returned value is "Z", i.e. is on the list, then:
            zone = country_zone(country)[5]
            return country, zone
        else:
            print(country_zone(country))
            continue


# Returns the zone of a country
def country_zone(country):
    with open('countries_zones.csv', 'r') as f:
        f.seek(0)
        index = -1
        for i in [line[:line.find(',')] for line in f.readlines()]:
            # Retrieves all elements before the comma for each line in the file by using split syntax [:]
            index += 1
            if i == country:
                f.seek(0)
                zone = f.readlines()[index].split(',')[-1]  # Obtain matching zone
                return zone[:-1]  # Trims to "Zone" + Zone number
            else:
                continue
        else:
            return "We do not currently post to " + country + "." + '\n'


# Where user can confirm or cancel their new item
def confirm_item(cart, package, weight, size, country, price):
    if input("Please confirm by pressing enter! (Otherwise enter 'b' to cancel item) ") != "b":
        cls()
        new_order = [package, weight, size, country, price]
        for i in cart:
            if new_order == i:  # Checking for duplicates
                while True:
                    print("-> 1x " + add.bold + size.title() + " " + package +
                          add.end + " weighing " + add.bold + str(weight) + "g " + add.end + "for " +
                          add.bold + country + "." + add.end + '\n')
                    dupe = input("You are about to add this as a duplicate item! Confirm with Y or N: ").upper()
                    if dupe == "Y":
                        cls()
                        cart.append(new_order)
                        view.main(cart)
                        break
                    elif dupe == "N":
                        cls()
                        break
                    else:
                        print("Please enter Y or N only." + '\n')
                        continue
                break
        else:
            cart.append(new_order)  # If no duplicate, append new item to cart
    else:
        cls()


# Where user chooses to add another item or exit to menu
def another_item(cart):
    while True:
        view.main(cart)  # Displays cart
        restart = input("Would you like to add another item to your cart? (Y or N) ").upper()
        cls()
        if restart == "Y":
            loop = 1
            cls()
            break
        elif restart == "N":
            loop = 0
            cls()
            break
        else:
            print("Please enter Y or N only." + '\n')
            continue
    return loop


def main(cart):
    while True:  # Allows for multiple items to be added in one run
        print("Please begin to enter your new package details." + '\n')
        package = package_input()
        weight = weight_input(package)
        size = size_input(package)
        country, zone = country_input(package)
        mplier = mplier_calc(size)
        price = pricing(zone, weight, package, mplier)  # Price determination
        print("You are about to add a " + add.bold + size + " " + package +
              add.end + " weighing " + add.bold + str(weight) + "g " + add.end + "for " +
              add.bold + country + "." + add.end)
        print("This " + add.bold + package + add.end + " will cost you " + add.bold +
              "$" + str(price) + add.end + " to ship to your destination." + '\n')
        confirm_item(cart, package, weight, size, country, price)  # Feeds current cart and new item details
        loop = another_item(cart)  # Returns users choice of adding another item, or exiting

        # If 'loop' is set to 0, user has chosen to add another item, otherwise returns cart
        if loop == 0:
            cls()
            return cart
        else:
            continue


if __name__ == "__main__":
    main()
