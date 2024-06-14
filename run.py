import gspread
from google.oauth2.service_account import Credentials

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

def choose_dep():
    case = input('Please, enter the department you want to visit\n1. Meat\n2. Dairy\n3. Vegetables\n4. Fruits\n5. Candies\n')
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
 
def show_dep(dep):
    try:
        print(f'Welcome to the {dep} department')
        print('Here is a selection of our products:\n')
        columns = get_all_columns(SHEET.worksheet(dep))
        if columns:
            # Assuming the first row contains headers

            print('Product  |  quantity  |  price:\n')
            for product in columns:
                name = product[0]
                quantity = product[1]
                price = product[2]
                print(f'{name}  |  {quantity}  |  {price} €')
            print()
            print('Would you like to add any of these products to your cart?\n')
            i = input('1. Yes\n2. No, I want to choose different department\n')
            if i == '1':
                add_to_cart(columns)
            else: 
                print('Thank you for visiting the store')
                
                
            
        
        else:
            print(f'No data available for the {dep} department.')
        print()
    except gspread.exceptions.WorksheetNotFound:
        print(f'The department "{dep}" was not found. Please check the name and try again.')
       

def add_to_cart(columns):
    cart = []
    product = int(input('Please enter the number of the product you want to add to your cart\n')) - 1
    x = columns[product][0] 
    cart.append(x)
    print(f'{x} has been added to your cart')
    
    
    



def get_all_columns(sheet):
    try:
        # Get all data from the sheet
        data = sheet.get_all_values()
        
        # Transpose the data to get columns as lists
        columns = list(zip(*data))
        
        return columns
    except Exception as e:
        print(f"Error retrieving data from sheet: {e}")
        return None


    
    

def main():
    print('Welcome to Grocery Store!\n')
    choose_dep()

if __name__ == "__main__":
    main()


    

    
    
    


