import os
import csv
from datetime import datetime


# Importing required modules
import view


# For making some bold print
class checkout:
    bold = '\033[1m'
    end = '\033[0m'


# Clear function depending on operating system
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Creates a [list] with the current cart information
def item_list(cart):
    item = 1
    items = []
    for i in cart:
        items.append("Item " + str(item) + " -> Type: " + i[0].title() + "    Weight: " + str(i[1] / 1000) +
                     "kg    Destination: " + i[3].upper() + "    Unit Price: " + "$" + str(i[4]))
        item += 1

    total = 0
    for i in cart:
        total += float(i[4])  # For each item in cart, take element at index 4 and produce sum
    items.append("Total price: $" + str(round(total, 2)))

    return items  # Returns 'items', which now contains all current cart information


# Creates a [list] with information for a particular item (for invoice.txt)
def show_item(item):
    names = {
        1: "Item Type: ",
        2: "Weight (g): ",
        3: "Destination: "
    }

    display_cart = [item[i] for i in [0, 1, 3]]  # Selecting only type, weight, destination from cart item
    display = []
    dict_index = 1
    for i in display_cart:
        display.append(names.get(dict_index) + str(i).title())  # Combining dictionary values with item details
        dict_index += 1

    return display


# Creating the invoice
def invoice(cart, dt):

    # Ensuring a folder called 'Invoices' exists in the current directory
    current_dir = os.getcwd()
    end_dir = os.path.join(current_dir, "Invoices")
    if not os.path.exists(end_dir):
        os.makedirs(end_dir)

    # Creating new file and writing invoice
    file_name = os.path.join(end_dir, dt + ".txt")
    with open(file_name, 'w') as inv:
        inv.write("---------------  Invoice  ---------------" + '\n' * 2)
        for i in item_list(cart):  # Writing cart details
            inv.write(i + '\n' * 2)
        inv.write("------------  End of Invoice  ------------" + '\n' * 3)
        item = 1
        for i in cart:  # For every item in current cart...
            inv.write("---------  Purchased Stamp No. " + str(item) + "  --------" + '\n' * 2)  # Write a title
            for d in show_item(i):  # For every detail in every cart item...
                inv.write(d + '\n')  # Write the detail + new line
            inv.write('\n' + "-------------------------------------------" + '\n' * 3)
            item += 1


# Writing to sales_history
def sales_history(cart, dt):

    # Determining sale_id
    with open('sales_history.csv', 'a+') as s:
        s.seek(0)
        data = list(csv.reader(s))
        if len(data) == 1:
            sale_id = 1  # If only one row in sales_history, sale_id is 1
        else:
            del data[0]
            ids = []
            for i in data:
                ids.append(int(i[0]))  # Creating list with all sale id's
            sale_id = max(ids) + 1  # New sale_id is equal to the max sale_id plus 1

        # Preparing items for writing to sales_history
        for i in cart:
            i.insert(0, dt)  # Inserting date and time to start of each cart item
            i.insert(0, sale_id)  # Inserting the sale_id to start of each cart item

        # Writing to sales_history
        csv.writer(s).writerows(cart)


def main(cart):
    view.main(cart)  # Displays current cart
    if input(
            "Please enter 'c' to confirm your current cart! (Or hit enter to go back) ").upper() == "C":
        if input("Please confirm checkout by again entering 'c'... (Or hit enter to go back) ").upper() == "C":
            dt = str(datetime.now().strftime("%Y-%m-%d %H.%M.%S"))  # Current date & time
            invoice(cart, dt)  # Printing invoice
            sales_history(cart, dt)  # Writing to sales_history
            cls()
            return "complete"  # Lets main menu know that checkout has completed
        else:
            cls()
    else:
        cls()

if __name__ == "__main__":
    main()
