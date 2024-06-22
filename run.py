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
spreadsheet_id = "1jwVRtZF2Qd35Wlwrlh4km0jNPHN_qd-uEvJV6k8ekGU"  # Replace with your actual spreadsheet ID
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
            print(f'You have paid {self.price} €. You have {self.cash} € left.\n')
        else:
            print('You do not have enough money to pay for your cart.')

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
 
      
 ██████╗     ██████╗     ██████╗      ██████╗     ████████    ██████╗     ██╗   ██╗ 
 ██╔═══╝     ██╔══██╗   ███╔═████╗    ██╔════╝    ██╔════╝    ██╔══██╗    ██║   ██║
 ██║  ███╗   ██████╔╝   ███║██╔██║    ██║         █████╗      ██████╔╝    ╚██╗ ██╔╝
 ██║   ██║   ██╔══██╗   █████╔╝██║    ██║         ██╔══╝      ██╔══██╗     ╚████╔╝ 
 ╚██████╔╝   ██║  ██║    ███████╔╝    ╚██████╗    ███████╗    ██║  ██║      ╚██╔╝    
  ╚═════╝    ╚═╝  ╚═╝     ╚═════╝      ╚═════╝    ╚══════╝    ╚═╝  ╚═╝       ██║   
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
        case = input('Please, enter the department you want to visit\n\n1. Meat\n2. Dairy\n3. Vegetables\n4. Fruits\n5. Candies\n')
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
        choose_dep()

# Function to choose department for admin
def choose_dep_admin(case=None):
    if not case:
        print("\n" + "=" * 80)
        case = input('Please, enter the department you want to add a product to\n\n1. Meat\n2. Dairy\n3. Vegetables\n4. Fruits\n5. Candies\n')
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
        choose_dep()

# Function to display products in a department
def show_dep(dep):
    try:
        print("\n" + "=" * 80)
        print(f'Welcome to the {dep} department\n')
        print('Here is a selection of our products:\n')
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
        print(f'The department "{dep}" was not found. Please check the name and try again.')

# Cart and price tracking
cart = [] # List to store cart items
price = 0 # Total price of the cart
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
    available = int(columns[product][1]) # Get the available quantity of the product
    print("\n" + "=" * 80)
    amount = int(input('Please enter the amount of the product you want to add to your cart\n'))
    if amount > available:
        print(f'You have entered an invalid amount. We have only {available} items in stock\n')
        return get_amount(columns, product)
    else:
        return amount
    
# Function to add products to cart
def add_to_cart(columns):
    print("\n" + "=" * 80)
    product = int(input('Please enter the number of the product you want to add to your cart\n')) - 1
    # Validate the product number
    if (product > len(columns) - 1) or (product < 0):
        print('You have entered an invalid number\n')
        add_to_cart(columns)
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
    print('Would you like to add more products to your cart from this department?\n')
    i = input('1. Yes\n2. No\n')
    if i == '1':
        add_to_cart(columns)
    elif i == '2':
        choice_3(columns)
    else: 
        print('Please enter a valid number')
        choice_2(columns)

# Function to handle the choice to proceed to checkout or choose another department       
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
    

# checkout function to display the cart and total price and proceed to payment
def checkout(cart, current_price):
    global price  # Access the global price variable 

    # Display the cart and total price
    print("\n" + "=" * 80)
    print('Your cart contains the following items:\n')
    for item in cart:
        print(item)
    print()
    print(f'Total price: {current_price} €\n')
    # Create a new Customer instance and pay for the cart
    nazar = Customer('Nazar', current_price)
    nazar.pay()
    print('Thank you for shopping with us!')
    # Update the product quantities in the Google Sheet
    update_sheet(cart)
    # Ask the user if they want to continue shopping
    print("\n" + "=" * 80)
    print('Would you like to continue shopping?\n')
    i = input('1. Yes\n2. No\n')
    if i == '1':
        cart.clear()
        price = 0  # Reset the global price variable if needed
        choose_dep()
    else:
        print('Goodbye!')



# Function to update product quantities in the Google Sheet           
def update_sheet(cart):
    # Iterate through all items in the cart
    for item in cart:
        try:
            product_name, unit, quantity = item.split()  # Unpack item into product_name, unit, quantity
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
                    # Update the quantity in the next column (assuming quantity is in the next column)
                    sheet.update_cell(cell.row + 1, cell.col, new_quantity)
                    # Update the quantity in the next column (assuming 
                
                    # Print message indicating product quantity update
                    print("\n" + "=" * 80)
                    print(f"Updated {product_name} quantity to {new_quantity} in the '{sheet.title}' worksheet.")
                
                    #Set flag indicating product was found and updated
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
        data = sheet.get_all_values() # Get a list of rows
        columns = list(zip(*data)) # Transpose the rows to get columns
        return columns 
    except Exception as e:
        print(f"Error retrieving data from sheet: {e}")
        return None


# Function to validate the name
def validate_name(name):
    # Check if the name contains only alphabetic symbols and is 3-15 characters long
        return name.isalpha() and 3 <= len(name) <= 15 
# Function to get the name    
def get_name():
    name = input('Please, enter your name:\n')
    print("\n" + "=" * 80)
    # Validating the name
    if not validate_name(name):
        print('You have entered invalid name')
        print('Name should contain only alphabetic symbols and be 3-15 characters long\n')
        return get_name()  # Return the result of the recursive call
    return name

# Function to update the quantity of a product
def get_cash():
    cash = input('Please, enter the amount of cash you Would like to spend\n')
    print("\n" + "=" * 80)
    # Validating the cash amount
    if cash.isdigit():
        if int(cash) < 5:
            print('You cant buy anything with this amount of money\n')
            return get_cash()
        elif int(cash) > 1000:
            print('You have entered too much cash, less than 1000€ will be enough\n')
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

    print(f'Hello, {name}! Here are the instructions on how to use our online store:')
    print()

    print("1. Explore Departments:")
    print("   - Enter the number of the department you want to visit (e.g., 1 for Meat).")
    print("   - Browse through products in the chosen department.")

    print()

    print("2. Add Items to Cart:")
    print("   - Select products by entering their corresponding numbers.")
    print("   - Input the quantity of each product you wish to add to your cart.")

    print()

    print("3. Proceed to Checkout:")
    print("   - Review your cart and total price.")
    print("   - Confirm your purchase and update product quantities.")

    print()

    print("4. Additional Options:")
    print("   - If you want to switch to another department, select the department option again.")
    print("   - After checkout, decide whether to continue shopping or exit the program.")

    print()

# Function to choose the role of the user
def choose_user():
    user = input('Please choose the type of user you are:\n\n1. Customer\n2. Admin\n')
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
    

# Function fot admin to choose the action    
def admin_choice():
    choice = input('1. Add a new product\n2. Update product quantity\n3. Check all stock\n4.Exit\n')
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
        print(f'The department "{dep.title}" was not found. Please check the name and try again.')
        
# Function to get a new products name
def product_name_info():
    name = input('Please enter the name of the product you want to add (e.g., "pork (kg)")\n')
    print("\n" + "=" * 80)
    # Validate the name
    if not name or len(name) < 2 or len(name) > 20:
        print('Invalid name. Please enter a valid product name.\n')
        print('Name should contain only be 2-20 characters long\n')
        return product_name_info()
    elif name.isdigit():
        print('Invalid name. Please enter a valid product name.\n')
        return product_name_info()
    return name

# Function to get a new products quantity
def product_quantity_info():
    quantity = input('Please enter the quantity of the product you want to add\n')
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
           
# Function to add a new product to the stock
def add_product():
    dep = choose_dep_admin()
    print(f'Welcome to the {dep} department!\n')
    try:
        # Access the worksheet for the given department
        sheet = SHEET.worksheet(dep)
        columns = get_all_columns(sheet)
        data = sheet.get_all_values()
        print('-' * 50)
        print('')
        print('The products that we currently have in stock:\n')
        if columns:
            # Displaying products with headers
            print('Nº | Product  |  Quantity  |  Price:\n')
            for idx, product in enumerate(columns, start=1):
                name = product[0]
                quantity = product[1]
                price = product[2]
                print(f'{idx}. {name}  |  {quantity}  |  {price} €')
            print('')
            print("\n" + "=" * 80)
        else:
            print(f'No data available for the {dep} department.')
        print()
        
        # Get new product details from the admin
        name = product_name_info()
        quantity = product_quantity_info()
        price = product_price_info()
              
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
        print(f'Product {name} with quantity {quantity} and price {price} € has been added to the {dep} department.\n')
    
    except gspread.exceptions.WorksheetNotFound:
        print(f'The department "{dep}" was not found. Please check the name and try again.')

# Main main admin function 
def admin_func():
    while True:  # Loop until the correct password is entered
        if get_password(): # Check the password
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
    case = input('Please, enter the department you want to visit:\n'
                 '1. Meat\n'
                 '2. Dairy\n'
                 '3. Vegetables\n'
                 '4. Fruits\n'
                 '5. Candies\n')
    choose_dep(case) 

# Main function to run the program
def main():                                                                                                                                                                                                                                                                                                                                                                                                                
    choose_user()

# Run the main function
if __name__ == "__main__":
    main()


    

    
    
    


