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

# Function to display products in a department
def show_dep(dep):
    try:
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
cart = []
price = 0
def choice_1(columns):
    print('Would you like to add any of these products to your cart?\n')
    i = input('1. Yes\n2. No, I want to choose a different department\n')
    if i == '1':
        add_to_cart(columns)
    elif i == '2':
        choose_dep()
    else:
        print('Please enter a valid number')
        choice_1(columns)
def get_amount(columns, product):
    available = int(columns[product][1])  
    amount = int(input('Please enter the amount of the product you want to add to your cart\n'))
    if amount > available:
        print(f'You have entered an invalid amount. We have only {available} items in stock\n')
        return get_amount(columns, product)
    else:
        return amount
# Function to add products to cart
def add_to_cart(columns):
    product = int(input('Please enter the number of the product you want to add to your cart\n')) - 1
    if (product > len(columns) - 1) or (product < 0):
        print('You have entered an invalid number\n')
        add_to_cart(columns)
    amount = get_amount(columns, product) 
    x = columns[product][0]
    y = int(columns[product][2])
    z = x + ' ' + str(amount)
    cart.append(z)
    global price 
    price += y * amount
    print(f'{z} has been added to your cart')
    choice_2(columns)
    
def choice_2(columns): 
    print('Would you like to add more products to your cart from this department?\n')
    i = input('1. Yes\n2. No\n')
    if i == '1':
        add_to_cart(columns)
    elif i == '2':
        choice_3(columns)
    else: 
        print('Please enter a valid number')
        choice_2(columns)
        
def choice_3(columns):
    print('Do you want to proceed to checkout?\n')
    a = input('1. Yes\n2. No, I want to choose another department\n')
    if a == '1':
        checkout(cart, price)
    elif a == '2': 
        choose_dep()
    else: 
        print('Please enter a valid number')
        choice_3(columns)
    
# Function to handle checkout process
# Function to handle checkout process
def checkout(cart, current_price):
    global price  # Access the global price variable if necessary

    print('Your cart contains the following items:\n')
    for item in cart:
        print(item)
    print()
    print(f'Total price: {current_price} €\n')
    
    nazar = Customer('Nazar', current_price)
    nazar.pay()
    print('Thank you for shopping with us!')
    update_sheet(cart)
    print('Would you like to continue shopping?\n')
    i = input('1. Yes\n2. No\n')
    if i == '1':
        cart.clear()
        price = 0  # Reset the global price variable if needed
        choose_dep()
    else:
        print('Goodbye!')



            
def update_sheet(cart):
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
    try:
        data = sheet.get_all_values()
        columns = list(zip(*data))
        return columns
    except Exception as e:
        print(f"Error retrieving data from sheet: {e}")
        return None



def validate_name(name):
        return name.isalpha() and 3 <= len(name) <= 15
    
def get_name():
    name = input('Please, enter your name:\n')
    if not validate_name(name):
        print('You have entered invalid name')
        print('Name should contain only alphabetic symbols and be 3-15 characters long\n')
        return get_name()  # Return the result of the recursive call
    return name
def get_cash():
    cash = input('Please, enter the amount of cash you Would like to spend\n')
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
# Main function to start the program

def choose_user():
    user = input('Please choose the type of user you are:\n\n1. Customer\n2. Admin\n')
    if user == '1':
        customer_func()
    elif user == '2':
        admin_func()
    else:
        print('You have entered an invalid number')
        choose_user()

def get_password():
    password = input('Please enter the password\n')
    if password == 'grocery':
        return True
    else:
        return False  
    


    

 
def customer_func():
    name = get_name()
    welcome()
    show_instructions(name)
    cash = get_cash()
    Customer.cash = int(cash)
    case = input('Please enter the number of the department you want to visit:\n\n'
                 '1. Meat\n'
                 '2. Dairy\n'
                 '3. Vegetables\n'
                 '4. Fruits\n'
                 '5. Candies\n')
    choose_dep(case)      
def main():
    choose_user()


if __name__ == "__main__":
    main()


    

    
    
    


