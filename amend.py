import os

# Importing required modules
import add


# For making some bold print
class amend:
    bold = '\033[1m'
    end = '\033[0m'


# Clear function depending on operating system
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Lists current items in the cart
def item_list(cart):
    item = 1
    for i in cart:
        print("Item " + str(item) + " -> Type: " + amend.bold + i[0].title() + amend.end + "    Weight: " +
              amend.bold + str(i[1] / 1000) + amend.end + "kg    Destination: " + amend.bold + i[3].upper() + amend.end
              + "    Unit Price: " + amend.bold + "$" + str(i[4]) + amend.end + '\n')
        item += 1


# Displays information for a particular item in cart
def show_item(amend_item):
    names = {
        1: "    (W) Weight (g): ",
        2: "    (S) Size: ",
        3: "    (C) Country: "
    }

    dict_index = 1
    for i in amend_item[1:4]:
        print(names.get(dict_index) + str(i).title() + '\n')
        dict_index += 1


def main(cart):
    n = 0
    for _ in cart:
        n += 1  # Gets the number of items in cart

        while True:  # Loop for item number input
            print(amend.bold + "YOUR CART" + amend.end + '\n')
            item_list(cart)
            print("-------------------------" + '\n')
            item = input("Enter the number of the item you would like to amend, or enter 'b' to go back: ")
            cls()
            if item.lower() == "b":
                amend_item = ""
                break
            elif not item.isdigit():
                print("Please enter a valid item number." + '\n')
                continue
            elif n >= int(item) > 0:  # Ensures input is the number of an item in cart
                amend_item = cart[int(item) - 1]  # Retrieves the item of choice from the cart
                break
            else:
                print("Please enter a valid item number." + '\n')
                continue

        if amend_item == "":  # If 'b' was entered to go back...
            break
        else:  # Otherwise...
            while True:  # Loop to allow for multiple changing of details
                while True:  # Loop for inputting of new details
                    print(amend.bold + amend_item[0].title() + amend.end + " information:" + '\n')
                    show_item(amend_item)  # Displays changeable information for chosen cart item
                    zone = add.country_zone(amend_item[3])[5]  # Sets zone for price calc, in case country is unchanged
                    c = input("Which detail would you like to change? (Or enter 'b' to go back) ").upper()
                    cls()
                    if c == "W":
                        print("Please update your weight below: " + '\n')
                        new_weight = add.weight_input(amend_item[0])  # Input of new weight
                        amend_item[1] = new_weight  # Amends weight of the item
                        loop = 1
                        break
                    if c == "S":
                        print("Please update your size below: " + '\n')
                        new_size = add.size_input(amend_item[0])  # Input of new size
                        amend_item[2] = new_size  # Amends size of the item
                        loop = 1
                        break
                    if c == "C":
                        print("Please update your destination country below: " + '\n')
                        new_country, zone = add.country_input(amend_item[0])  # Input of new country
                        amend_item[3] = new_country  # Amends destination country of the item
                        loop = 1
                        break
                    elif c == "B":
                        loop = 0
                        break
                    else:
                        cls()
                        print("Please enter W, S or C (or b to go back). " + '\n')
                        continue

                if loop == 1:  # If a detail was successfully changed, keeps repeating until 'b' is inputted
                    print(amend.bold + "Done." + amend.end + '\n')
                    continue
                else:
                    amend_item[4] = add.pricing(zone, amend_item[1],
                                                amend_item[0], add.mplier_calc(amend_item[2]))  # Calculating new price
                    cart[int(item) - 1] = amend_item  # Amending new item to the cart
                    break

    return cart  # Returns the updated cart


if __name__ == "__main__":
    main()
