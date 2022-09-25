class view:
    bold = '\033[1m'
    end = '\033[0m'


def main(cart):
    item = 1
    print(view.bold + "YOUR CART" + view.end + '\n')
    for i in cart:
        print("Item " + str(item) + " -> Type: " + view.bold + i[0].title() + view.end + "    Weight: " +
              view.bold + str(i[1] / 1000) + view.end + "kg    Destination: " + view.bold + i[3].upper() + view.end
              + "    Unit Price: " + view.bold + "$" + str(i[4]) + view.end + '\n')
        item += 1

    total = 0
    for i in cart:
        total += float(i[4])  # For each item in cart, take element at index 4 (unit price) and produce sum
    print("Your total cost is $" + view.bold + str(round(total, 2)) + view.end + '\n')
    print("-------------------------" + '\n')


if __name__ == "__main__":
    main()
