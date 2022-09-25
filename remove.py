import os


# For making some bold print
class remove:
    bold = '\033[1m'
    end = '\033[0m'


# Clear function depending on operating system
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Lists current items in the cart
def item_list(cart):
    item = 1
    for i in cart:
        print("Item " + str(item) + " -> Type: " + remove.bold + i[0].title() + remove.end + "    Weight: " +
              remove.bold + str(i[1] / 1000) + remove.end + "kg    Destination: " + remove.bold + i[3].upper() +
              remove.end + "    Unit Price: " + remove.bold + "$" + str(i[4]) + remove.end + '\n')
        item += 1


# Displays information for a particular item in cart
def show_item(r, item):
    print(remove.bold + "Item " + item + remove.end + " information:" + '\n')
    names = {
        1: "    Weight (g): ",
        2: "    Size: ",
        3: "    Country: ",
        4: "    Price ($): "
    }

    dict_index = 1
    for i in r[1:5]:
        print(names.get(dict_index) + str(i).title() + '\n')
        dict_index += 1


def main(cart):
    n = 0
    for _ in cart:
        n += 1  # Gets the number of items in cart

    while True:
        print(remove.bold + "YOUR CART" + remove.end + '\n')
        while True:
            item_list(cart)
            print("-------------------------" + '\n')
            item = input("Enter the number of the item you would like to remove, or enter 'b' to go back: ")
            cls()
            if item.lower() == "b":
                loop = 0
                break
            elif not item.isdigit():
                print("Please enter a valid item number." + '\n')
                continue
            elif n >= int(item) > 0:  # If input is a number of an item in cart
                show_item(cart[int(item) - 1], item)  # Displays all details of chosen cart item
                c = input("Please confirm by pressing enter! (Otherwise enter 'b' to go back) ").upper()  # Confirms
                cls()
                if c != "B":  # If 'b' wasn't entered...
                    del cart[int(item)-1]  # Remove item from cart
                    loop = 0
                    input("Item removed. Hit enter to return to menu...")
                    cls()
                else:
                    loop = 1
                break
            else:
                cls()
                print("Please enter a valid item number." + '\n')
                continue

        if loop == 1:  # Loops if an item has not been removed
            continue
        else:
            break

    return cart  # Returns the updated cart


if __name__ == "__main__":
    main()
