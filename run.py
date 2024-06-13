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
    case = input('Enter the department you want to visit?\n1. Meat\n2. Dairy\n3. Vegetables\n4. Fruits\n5. Candies\n')
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
    print(f'Welcome to the {dep} department')
    print('Here is a selection of our products:\n')
    columns = get_all_columns(SHEET.worksheet(dep))
    if columns:
        # Assuming the first row contains headers
        headers = columns[0]
        products = columns[1:]  # Skip headers

        for product in products:
            name = product[0]
            quantity = product[1]
            price = product[2]
            print(f'{name}  quantity: {quantity}  price: {price} EUR')
    else:
        print(f'No data available for the {dep} department.')
    print()

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


    

    
    
    


