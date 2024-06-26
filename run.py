import gspread
from google.oauth2.service_account import Credentials


# Google Sheets API scope and credentials setup
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
spreadsheet_id = "1jwVRtZF2Qd35Wlwrlh4km0jNPHN_qd-uEvJV6k8ekGU"
# Replace with your actual spreadsheet ID
SHEET = GSPREAD_CLIENT.open_by_key(spreadsheet_id)


# Customer class for handling cash and payment
class Customer:
    # Initial cash amount for demonstration
    cash = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def pay(self):
        if self.__class__.cash >= self.price:
            self.__class__.cash -= self.price
            print(f'You have paid {self.price}€')
            print(f'You have {self.cash} € left.\n')
            return True
        else:
            print('You do not have enough money to pay for your cart.')
            return False

# Function to welcome the user


def welcome():
    print('''

██╗    ██╗  ███████╗  ██╗      ██████╗    ██████╗     ███╗   ███╗   ████████
██║    ██║  ██╔════╝  ██║      ██╔════╝  ███╔═████╗   ████╗ ████║   ██╔════╝
██║ █╗ ██║  ███████╗  ██║      ██║       ███║██╔██║   ██╔████╔██║   █████╗
██║███╗██║  ██╔════╝  ██║      ██║       █████╔╝██║   ██║╚██╔╝██║   ██╔══╝
╚███╔███╔╝  ███████╗  ███████╗ ╚██████╗   ███████╔╝   ██║ ╚═╝ ██║   ███████╗
 ╚══╝╚══╝   ╚══════╝  ╚══════╝  ╚═════╝    ╚═════╝    ╚═╝     ╚═╝   ╚══════╝

        ████████╗    ██████╗          ████████╗   ██╗   ██╗    ████████
        ╚══██╔══╝   ███╔═████╗        ╚══██╔══╝   ██║   ██║    ██╔════╝
           ██║      ███║██╔██║           ██║      ████████║    █████╗
           ██║      ███║██╔██║           ██║      ██║   ██║    ██╔══╝
           ██║       ███████╔╝           ██║      ██║   ██║    ███████╗
           ╚═╝        ╚═════╝            ╚═╝      ╚═╝   ╚═╝    ╚══════╝


 ██████╗    ██████╗     ██████╗      ██████╗    ████████   ██████╗    ██╗   ██╗
 ██╔═══╝    ██╔══██╗   ███╔═████╗    ██╔════╝   ██╔════╝   ██╔══██╗   ██║   ██║
 ██║  ███╗  ██████╔╝   ███║██╔██║    ██║        █████╗     ██████╔╝   ╚██╗ ██╔╝
 ██║   ██║  ██╔══██╗   █████╔╝██║    ██║        ██╔══╝     ██╔══██╗    ╚████╔╝
 ╚██████╔╝  ██║  ██║    ███████╔╝    ╚██████╗   ███████╗   ██║  ██║     ╚██╔╝
  ╚═════╝   ╚═╝  ╚═╝     ╚═════╝      ╚═════╝   ╚══════╝   ╚═╝  ╚═╝      ██║
                                                                         ╚═╝

          ███████╗     ████████╗     ██████╗      ██████╗     ████████
          ██╔════╝     ╚══██╔══╝    ███╔═████╗    ██╔══██╗    ██╔════╝
          ███████╗        ██║       ███║██╔██║    ██████╔╝    █████╗
          ╚════██║        ██║       █████╔╝██║    ██╔══██╗    ██╔══╝
          ███████║        ██║        ███████╔╝    ██║  ██║    ███████╗
          ╚══════╝        ╚═╝         ╚═════╝     ╚═╝  ╚═╝    ╚══════╝

          ''')


# Function to choose department and show products
def choose_dep(case=None):
    if not case:
        print("\n" + "=" * 80)
        case = input('''Please, enter the department you want to visit\n
1. Meat
2. Dairy
3. Vegetables
4. Fruits
5. Candies
''')

    dep = ''
    if case == '1':
        dep = 'meat'
        show_dep(dep)
    elif case == '2':
        dep = 'dairy'
        show_dep(dep)
    elif case == '3':
        dep = 'vegetables'
        show_dep(dep)
    elif case == '4':
        dep = 'fruits'
        show_dep(dep)
    elif case == '5':
        dep = 'candies'
        show_dep(dep)
    else:
        print('Please enter a valid department')
        return choose_dep()


# Function to choose department for admin
def choose_dep_admin(case=None):
    if not case:
        print("\n" + "=" * 80)
        case = input('''Please, enter the department you want to add
a product to \n\n1. Meat\n2. Dairy\n3. Vegetables
4. Fruits\n5. Candies\n\n''')
    dep = ''
    if case == '1':
        dep = 'meat'
        return dep
    elif case == '2':
        dep = 'dairy'
        return dep
    elif case == '3':
        dep = 'vegetables'
        return dep
    elif case == '4':
        dep = 'fruits'
        return dep
    elif case == '5':
        dep = 'candies'
        return dep
    else:
        print('Please enter a valid department')
        return choose_dep_admin()


# Function to choose the department to update the quantity of a product
def choose_dep_update(case=None):
    if not case:
        print("\n" + "=" * 80)
        case = input('''Please, enter the department where you want to update
the quantity of product\n\n1. Meat\n2. Dairy
3. Vegetables\n4. Fruits\n5. Candies\n\n''')
    dep = ''
    if case == '1':
        dep = 'meat'
        return dep
    elif case == '2':
        dep = 'dairy'
        return dep
    elif case == '3':
        dep = 'vegetables'
        return dep
    elif case == '4':
        dep = 'fruits'
        return dep
    elif case == '5':
        dep = 'candies'
        return dep
    else:
        print('Please enter a valid department')
        return choose_dep_update()


# Function to display products in a department
def show_dep(dep):
    try:
        print("\n" + "=" * 80)
        print(f'Welcome to the {dep} department\n')
        print('Here is selection of our products:\n')
        columns = get_all_columns(SHEET.worksheet(dep))
        if columns:
            # Displaying products with headers
            print('Nº | Product  |  Quantity  |  Price:\n')
            for idx, product in enumerate(columns, start=1):
                name = product[0]
                quantity = product[1]
                price = product[2]
                print(f'{idx}. {name}  |  {quantity}  |  {price} €')
            print('')
            choice_1(columns)
        else:
            print(f'No data available for the {dep} department.')
        print()
    except gspread.exceptions.WorksheetNotFound:
        print(f'''The department "{dep}" was not found. Please check the name
and try again.''')


# Function to display products in a department for admin
def show_dep_admin(dep):
    try:
        print("\n" + "=" * 80)
        print(f'Welcome to the {dep} department\n')
        print('''Here you can see the products that we
currently have in stock:\n''')
        columns = get_all_columns(SHEET.worksheet(dep))
        if columns:
            # Displaying products with headers
            print('Nº | Product  |  Quantity  |  Price:\n')
            for idx, product in enumerate(columns, start=1):
                name = product[0]
                quantity = product[1]
                price = product[2]
                print(f'{idx}. {name}  |  {quantity}  |  {price} €')
            print('')
        else:
            print(f'No data available for the {dep} department.')
        print()
    except gspread.exceptions.WorksheetNotFound:
        print(f'''The department "{dep}" was not found. Please check the name
and try again.''')


# Cart and price tracking
cart = []  # List to store cart items
price = 0  # Total price of the cart


def choice_1(columns):
    print("\n" + "=" * 80)
    print('Would you like to add any of these products to your cart?\n')
    i = input('1. Yes\n2. No, I want to choose a different department\n')
    if i == '1':
        add_to_cart(columns)
    elif i == '2':
        choose_dep()
    else:
        print('Please enter a valid number')
        choice_1(columns)


# Function to get the amount of a product
def get_amount(columns, product):
    # Get the available quantity of the product
    available = int(columns[product][1])
    print("\n" + "=" * 80)
    amount = input('''Please enter the amount
of the product you want to add to your cart\n''')
    if not (amount.isdigit() and 1 <= int(amount) <= available):
        print('You have entered an invalid amount\n')
        print(f'The available quantity of {columns[product][0]}: {available}')
        return get_amount(columns, product)
    else:
        return int(amount)


def get_product_number(columns):
    print("\n" + "=" * 80)
    product = input('''Please enter the number of the product you want to
add to your cart:\n''')
    if not (product.isdigit() and 1 <= int(product) <= len(columns)):
        print('You have entered an invalid number\n')
        return get_product_number(columns)
    else:
        return int(product) - 1


# Function to add products to cart
def add_to_cart(columns):
    product = get_product_number(columns)
    # Get the amount of the product
    amount = get_amount(columns, product)
    x = columns[product][0]
    y = int(columns[product][2])
    z = x + ' ' + str(amount)
    # Add the product to the cart
    cart.append(z)
    global price
    price += y * amount
    print(f'{z} has been added to your cart')
    choice_2(columns)


# Function to handle the choice to add more products to the cart
def choice_2(columns):
    print("\n" + "=" * 80)
    print('''Would you like to add more products to your cart from this
department?\n''')
    i = input('1. Yes\n2. No\n')
    if i == '1':
        add_to_cart(columns)
    elif i == '2':
        choice_3(columns)
    else:
        print('Please enter a valid number')
        choice_2(columns)


''' Function to handle the choice to proceed to checkout or choose
another department '''


def choice_3(columns):
    print("\n" + "=" * 80)
    print('Do you want to proceed to checkout?\n')
    a = input('1. Yes\n2. No, I want to choose another department\n')
    if a == '1':
        checkout(cart, price)
    elif a == '2':
        choose_dep()
    else:
        print('Please enter a valid number')
        choice_3(columns)


# Function to exit the program or continue shopping
def exit_program():
    print("\n" + "=" * 80)
    print('Would you like to continue shopping?\n')
    i = input('1. Yes\n2. No\n')
    if i == '1':
        cart.clear()
        global price  # Reset the global price variable if needed
        price = 0
        choose_dep()
    elif i == '2':
        print('Goodbye!')
    else:
        print('Please enter a valid number')
        exit_program()


# checkout function to display the cart and total price and proceed to payment
def checkout(cart, current_price):
    # Display the cart and total price
    print("\n" + "=" * 80)
    print('Your cart contains the following items:\n')
    for item in cart:
        print(item)
    print()
    print(f'Total price: {current_price} €\n')
    # Create a new Customer instance and pay for the cart
    nazar = Customer('Nazar', current_price)
    if nazar.pay():
        print('Thank you for shopping with us!')
    # Update the product quantities in the Google Sheet
        update_sheet(cart)
    # Ask the user if they want to continue shopping
        exit_program()


# Function to update product quantities in the Google Sheet
def update_sheet(cart):
    # Iterate through all items in the cart
    for item in cart:
        try:
            # Unpack item into product_name, unit, quantity
            product_name, unit, quantity = item.split()
            title = product_name + ' ' + unit
        except ValueError:
            print(f"Invalid format for item: {item}")
            continue

        # Flag to track if product was found in any worksheet
        product_found = False

        # Iterate through all worksheets in the spreadsheet
        for sheet in SHEET.worksheets():
            try:
                # Find the cell containing the product name
                cell = sheet.find(title)
                if cell is not None:
                    current_quantity = sheet.cell(cell.row + 1, cell.col).value
                    new_quantity = int(current_quantity) - int(quantity)
                    sheet.update_cell(cell.row + 1, cell.col, new_quantity)
                    # Update the quantity in the next column

                    # Print message indicating product quantity update
                    print("\n" + "=" * 80)
                    print(f'''Updated {product_name} quantity to {new_quantity}
in the '{sheet.title}' worksheet.''')

                    # Set flag indicating product was found and updated
                    product_found = True
                    break
            except gspread.exceptions.APIError as e:
                # Handle specific API errors
                print(f"API error occurred: {e}")

        # If product was not found in any worksheet, print a message
        if not product_found:
            print(f"Product '{product_name}' not found in any worksheet.")


# Function to retrieve all columns from a Google Sheet worksheet
def get_all_columns(sheet):
    # Retrieve all data from the worksheet
    try:
        data = sheet.get_all_values()  # Get a list of rows
        columns = list(zip(*data))  # Transpose the rows to get columns
        return columns
    except Exception as e:
        print(f"Error retrieving data from sheet: {e}")
        return None


# Function to validate the name
def validate_name(name):
    ''' Check if the name contains only alphabetic
symbols and is 3-15 characters long '''
    return name.isalpha() and 3 <= len(name) <= 15


# Function to get the name
def get_name():
    name = input('Please, enter your name:\n')
    print("\n" + "=" * 80)
    # Validating the name
    if not validate_name(name):
        print('You have entered invalid name')
        print('''Name should contain only alphabetic symbols and be 3-15
characters long\n''')
        return get_name()  # Return the result of the recursive call
    return name


# Function to update the quantity of a product
def get_cash():
    cash = input('Please, enter the amount of cash you would like to spend\n')
    # Validating the cash amount
    if cash.isdigit():
        if int(cash) < 5:
            print('You cant buy anything with this amount of money\n')
            return get_cash()
        elif int(cash) > 1000:
            print('''You have entered too much cash, less than 1000€ will be
enough\n''')
            return get_cash()
        else:
            return int(cash)
    else:
        print('You have entered invalid cash amount\n')
        return get_cash()


# Function to show the instructions for the customer
def show_instructions(name):
    print("\n" + "=" * 80)
    print(f'{"Instructions":^80}')
    print("=" * 80 + "\n")

    print(f'''Hello, {name}! Here are the instructions on how to use our online
store:''')
    print()

    print("1. Explore Departments:")
    print('''- Enter the number of the department you want to visit
(e.g., 1 for Meat).''')
    print('  - Browse through products in the chosen department.')

    print()

    print("2. Add Items to Cart:")
    print("- Select products by entering their corresponding numbers.")
    print("- Input the quantity of each product you wish to add to your cart.")

    print()

    print("3. Proceed to Checkout:")
    print("- Review your cart and total price.")
    print("- Confirm your purchase and update product quantities.")

    print()

    print("4. Additional Options:")
    print('''- If you want to switch to another department, select the
department option again.''')
    print('''- After checkout, decide whether to continue shopping or exit
the program.''')

    print()


# Function to choose the role of the user
def choose_user():
    user = input('''\nPlease choose the type of user you are:\n
1. Customer\n2. Admin\n\n''')
    print("\n" + "=" * 80)
    if user == '1':
        customer_func()
    elif user == '2':
        admin_func()
    else:
        print('You have entered an invalid number')
        choose_user()


# Function to get the password
def get_password():
    password = input('Please enter the password\n')
    if password == 'grocery':
        return True
    else:
        return False


def go_back():
    print("\n" + "=" * 80)
    print('Would you like to go back to the main menu?\n')
    i = input('1. Yes\n2. No, I want to leave a program\n')
    if i == '1':
        admin_choice()
    elif i == '2':
        print('Goodbye!')
    else:
        print('You have entered an invalid number')
        go_back()


# Function fot admin to choose the action
def admin_choice():
    print('')
    choice = input('''1. Add a new product\n2. Update product quantity
3. Check all stock\n4.Exit\n\n''')
    print("\n" + "=" * 80)
    if choice == '1':
        add_product()
    elif choice == '2':
        update_quantity()
    elif choice == '3':
        check_stock()
    elif choice == '4':
        print('Goodbye!')
    else:
        print('You have entered an invalid number. Please, try again\n')
        return admin_choice()


# Function to show all products in the stock
def check_stock():
    # Get all worksheets in the spreadsheet
    all_sheets = SHEET.worksheets()
    # Iterate through all worksheets
    try:
        print('Here is a selection of our products:\n')
        for dep in all_sheets:
            columns = get_all_columns(SHEET.worksheet(dep.title))
            if columns:
                # Displaying products with headers
                print(f'Products in the {dep.title} department:\n')
                print('Nº | Product  |  Quantity  |  Price:\n')
                for idx, product in enumerate(columns, start=1):
                    name = product[0]
                    quantity = product[1]
                    price = product[2]
                    print(f'{idx}. {name}  |  {quantity}  |  {price} €')
                print('')
                print("\n" + "=" * 80)
            else:
                print(f'No data available for the {dep.title} department.')
            print()
    except gspread.exceptions.WorksheetNotFound:
        print(f'''The department "{dep.title}" was not found. Please check
the name and try again.''')
    go_back()


# Function to get a new products name
def product_name_info():
    name = input('''Please enter the name of the product you want to add
    (e.g., "pork (kg)")\n''')
    print("\n" + "=" * 80)

    # Validate the name
    for char in name:
        if char.isdigit():
            print('Invalid name. Name should contain alphabetic characters.\n')
            return product_name_info()

    if not name:
        print('Invalid name. Please enter a valid product name.\n')
        return product_name_info()

    elif len(name) < 2 or len(name) > 20:
        print('Invalid length. Name should be between 2 and 20 characters.\n')
        return product_name_info()

    # If none of the above conditions were met, the name is valid
    return name


# Function to get a new products quantity
def product_quantity_info():
    quantity = input('''Please enter the quantity of the product you want
to add\n''')
    print("\n" + "=" * 80)
    # Validate the quantity
    if not quantity.isdigit():
        print('Invalid quantity. It can only be a numeric value.\n')
        return product_quantity_info()
    elif int(quantity) < 0:
        print('Quantity cannot be negative.\n')
        return product_quantity_info()
    elif int(quantity) == 0:
        print('Quantity cannot be zero.\n')
        return product_quantity_info()
    elif int(quantity) > 1000:
        print('Quantity is too high.\n')
        return product_quantity_info()
    return quantity


# Function to get a new products price
def product_price_info():
    price = input('Please enter the price of the product you want to add\n')
    print("\n" + "=" * 80)
    # Validate the price
    if not price.isdigit():
        print('Invalid price. Please enter a numeric value.\n')
        return product_price_info()
    elif int(price) < 0:
        print('Price cannot be negative. Please enter a valid price.\n')
        return product_price_info()
    elif int(price) == 0:
        print('Price cannot be zero. Please enter a valid price.\n')
        return product_price_info()
    elif int(price) > 100:
        print('Price is too high. Please enter a valid price.\n')
        return product_price_info()
    return price


# Function to update the quantity of a product as an admin
def get_number_to_update(columns):
    product = input('''Please, enter the number of the product you want to
update the quantity of\n''')
    # Validate the product number
    if not (product.isdigit() and 1 <= int(product) <= len(columns)):
        print('You have entered an invalid number\n')
        return get_number_to_update(columns)
    print("\n" + "=" * 80)
    return product


# Function to get the quantity to update
def get_quantity_to_update():
    number = input('Please, enter how much of this product you want to add\n')
    if not number.isdigit():
        print('Invalid quantity. Please enter a numeric value.\n')
        return get_quantity_to_update()
    elif int(number) < 0:
        print('Quantity cannot be negative. Please enter a valid quantity.\n')
        return get_quantity_to_update()
    elif int(number) == 0:
        print('Quantity cannot be zero. Please enter a valid quantity.\n')
        return get_quantity_to_update()
    elif int(number) > 1000:
        print('Quantity is too high. Please enter a valid quantity.\n')
        return get_quantity_to_update()
    print("\n" + "=" * 80)
    return number


# Function to update the quantity of a product
def update_quantity():
    dep = choose_dep_update()
    print(f'Welcome to the {dep} department!\n')
    show_dep_admin(dep)
    columns = get_all_columns(SHEET.worksheet(dep))
    number = get_number_to_update(columns)
    quantity = get_quantity_to_update()
    current_quantity = int(columns[int(number) - 1][1])
    updated_quantity = current_quantity + int(quantity)

    # Update the quantity in the worksheet
    sheet = SHEET.worksheet(dep)
    cell = sheet.find(columns[int(number) - 1][0])
    sheet.update_cell(cell.row + 1, cell.col, updated_quantity)

    print(f'''The quantity of the product has been updated successfully.\n
Now we have {str(updated_quantity)} items of
{columns[int(number) - 1][0]} in stock.\n
          ''')

    go_back()


# Function to add a new product to the stock
def add_product():
    dep = choose_dep_admin()
    print(f'Welcome to the {dep} department!\n')
    show_dep_admin(dep)

    # Get new product details from the admin
    name = product_name_info()
    quantity = product_quantity_info()
    price = product_price_info()
    sheet = SHEET.worksheet(dep)
    data = sheet.get_all_values()

    # Validate the inputs
    if not quantity.isdigit() or not price.isdigit():
        print('Invalid quantity or price. Please enter numeric values.\n')
        return add_product()

    # Append the new product details as a column
    new_column = [name, quantity, price]
    for i, value in enumerate(new_column):
        sheet.update_cell(i + 1, len(data[0]) + 1, value)
    print("\n" + "=" * 80)
    print('')
    print(f'''Product {name} with quantity {quantity} and price {price}
€ has been added to the {dep} department.\n''')
    go_back()


# Main main admin function
def admin_func():
    while True:  # Loop until the correct password is entered
        if get_password():  # Check the password
            break
        else:
            print('You have entered an invalid password. Please try again.')
    print('You have successfully logged in!\n')
    print("\n" + "=" * 80)
    print('Welcome to the admin panel!\nWhat would you like to do?\n')
    # Choose the action if the password is correct
    admin_choice()


# Main function for the customer
def customer_func():
    # Get the customer's name
    name = get_name()
    # Display the welcome message and instructions
    welcome()
    show_instructions(name)
    # Get the cash amount
    cash = get_cash()
    # Set the cash amount for the customer
    Customer.cash = int(cash)
    print("\n" + "=" * 80)
    choose_dep()


# Main function to run the program
def main():
    choose_user()


# Run the main function
if __name__ == "__main__":
    main()
