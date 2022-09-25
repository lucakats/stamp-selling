import os

# Importing required modules
import user
import add
import remove
import view
import amend
import checkout


# For making some bold print
class home:
    bold = '\033[1m'
    end = '\033[0m'


# Clear function depending on operating system
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to check if cart is empty
def empty_cart(cart):
    if not cart:  # If the cart is empty
        print(home.bold + "YOUR CART" + home.end)
        print("(... is empty)" + '\n')
        input("Hit enter to return to menu...")
        return 0


def main():
    cls()
    print("Hi there. Welcome to the digital stamp shop!" + '\n')
    while True:
        name = user.main()  # Logging in
        cart = []  # 'cart' will be used to store the current users items - resets after every login
        cls()
        print("Welcome " + home.bold + name + home.end + "." + '\n')
        while True:
            print("Please input a menu option and hit enter..." + "\n" * 2 + "1. Add item" +
                  "\n" + "2. View cart" + "\n" + "3. Amend item" + "\n" + "4. Remove item" +
                  "\n" + "5. Checkout!" + "\n" + "6. Log Out" + '\n')
            choice = input("")  # Menu choice
            cls()
            if choice == "1":
                cart = add.main(cart)  # Feeds current cart and retrieves new cart

            elif choice == "2":
                if empty_cart(cart) == 0:
                    cls()
                else:
                    view.main(cart)  # Displays current cart
                    input("Hit enter to continue...")  # Pauses until user inputs anything
                    cls()

            elif choice == "3":
                if empty_cart(cart) == 0:
                    cls()
                else:
                    cart = amend.main(cart)  # Feeds current cart and retrieves new cart

            elif choice == "4":
                if empty_cart(cart) == 0:
                    cls()
                else:
                    cart = remove.main(cart)  # Feeds current cart and retrieves new cart

            elif choice == "5":
                if empty_cart(cart) == 0:
                    cls()
                else:
                    if checkout.main(cart) == "complete":
                        print("Thanks for shopping! Logging out..." + '\n')
                        break

            elif choice == "6":
                print("Thanks for shopping! Logging out..." + '\n')
                break

            else:
                print("Please enter a valid option.")
                continue


if __name__ == "__main__":
    main()
