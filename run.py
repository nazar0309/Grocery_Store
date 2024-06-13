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



def get_all_columns(sheet):
    # Get all data from the sheet
    data = sheet.get_all_values()
    
    # Transpose the data to get columns as lists
    columns = list(zip(*data))
    
    return columns

# Get all columns from the "goods" worksheet
all_columns = get_all_columns(SHEET.worksheet("goods"))

# Example: Print all columns
for i, col in enumerate(all_columns, start=1):
    print(col)

    

    
    
    


