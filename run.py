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
        print('Welcome to the meet department')
        get_all_columns(SHEET.worksheet(dep))
    elif case == '2':
        dep = 'dairy'
        print('Welcome to the dairy department')
        get_all_columns(SHEET.worksheet(dep))
    elif case == '3':
        dep = 'vegetables'
        print('Welcome to the vegetables department')
        get_all_columns(SHEET.worksheet(dep))
    elif case == '4':
        dep = 'fruits'
        print('Welcome to the fruits department')
        get_all_columns(SHEET.worksheet(dep))
    elif case == '5':
        dep = 'candies'
        print('Welcome to the candies department')
        get_all_columns(SHEET.worksheet(dep))
    else:
        print('Please enter a valid department')
        
    









def get_all_columns(sheet):
    
    # Get all data from the sheet
    data = sheet.get_all_values()
    
    # Transpose the data to get columns as lists
    columns = list(zip(*data))
    
    print(columns)

# Get all columns from the "goods" worksheet
    
    
def main ():
    print('Welcome to Grocery Store!\n')
    choose_dep()
    
main()
    

            

    

    
    
    


