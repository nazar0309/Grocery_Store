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
    cash = 30  # Initial cash amount for demonstration
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def pay(self):
        if self.__class__.cash >= self.price:
            self.__class__.cash -= self.price
            print(f'You have paid {self.price} €. You have {self.cash} € left.\n')
        else:
            print('You do not have enough money to pay for your cart. Please remove some items.')

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
            print('Would you like to add any of these products to your cart?\n')
            i = input('1. Yes\n2. No, I want to choose a different department\n')
            if i == '1':
                add_to_cart(columns)
            else:
                choose_dep()
        else:
            print(f'No data available for the {dep} department.')
        print()
    except gspread.exceptions.WorksheetNotFound:
        print(f'The department "{dep}" was not found. Please check the name and try again.')

# Cart and price tracking
cart = []
price = 0

# Function to add products to cart
def add_to_cart(columns):
    product = int(input('Please enter the number of the product you want to add to your cart\n')) - 1
    if (product > len(columns) - 1) or (product < 0):
        print('You have entered an invalid number\n')
        add_to_cart(columns)
        
    amount = int(input('Please enter the amount of the product you want to add to your cart\n'))
    print('')
    x = columns[product][0] 
    y = int(columns[product][2])
    z = x + ' ' + str(amount)
    cart.append(z)
    global price 
    price += y * amount
    print(f'{z} has been added to your cart')
    print('Would you like to add more products to your cart from this department?\n')
    i = input('1. Yes\n2. No\n')
    if i == '1':
        add_to_cart(columns)
    else:
        print('Do you want to proceed to checkout?\n')
        a = input('1. Yes\n2. No, I want to choose another department\n')
        if a == '1':
            checkout(cart, price)
        else: 
            choose_dep()

# Function to handle checkout process
def checkout(cart, price):
    print('Your cart contains the following items:\n')
    for item in cart:
        print(item)
    print()
    print(f'Total price: {price} €\n')
    nazar = Customer('Nazar', price)
    nazar.pay()
    print('Thank you for shopping with us!')
    print('Would you like to continue shopping?\n')
    i = input('1. Yes\n2. No\n')
    if i == '1':
        choose_dep()
    else:
        print('Goodbye!')

# Function to retrieve all columns from a Google Sheet worksheet
def get_all_columns(sheet):
    try:
        data = sheet.get_all_values()
        columns = list(zip(*data))
        return columns
    except Exception as e:
        print(f"Error retrieving data from sheet: {e}")
        return None

# Main function to start the program
def main():
    name = input('Please enter your name\n')
    print(f'Welcome to Grocery Store, {name}! Explore our departments')
    print('and add items to your cart. When you\'re ready,')
    print('you can proceed to checkout. If you need to')
    print('quit, simply type "QUIT" as your input.')
    case = input('Please, enter the department you want to visit\n\n1. Meat\n2. Dairy\n3. Vegetables\n4. Fruits\n5. Candies\n')
    choose_dep(case)

if __name__ == "__main__":
    main()


    

    
    
    


