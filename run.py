import gspread
from google.oauth2.service_account import Credentials
import json

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

creds = json.load(open('creds.json'))
CREDS = Credentials.from_service_account_info(creds)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Iceberg")

grids_sheet = SHEET.worksheet('grid')
data = grids_sheet.get_all_values()


# def make_playbord_in_sheet(data):
#     """ 
#     Create a board for the game in ICEBERG sheet
#     """ 


# for cell in grids_sheet.range('a1:b2'):
#     print(cell.value)

# print(grids_sheet.acell('b1').value)
# print(grids_sheet.cell(1,1).value)

i = 1
o = 'b'
b = o,i
c = str(b)
print(c)


# while i  <= 18:
#     grids_sheet.update_acell(('A4'),'30000000')
#     i += i

# grids.write(1, 0, 'ISBT DEHRADUN')