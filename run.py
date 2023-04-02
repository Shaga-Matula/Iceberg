import gspread
from google.oauth2.service_account import Credentials
import json
import os

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

def create_game_board():
    os.system('cls')
    """
    This function writes the board on screen
    """
    print("|%%%%%%%%%%%%%-- ICEBURG ----%%%%%%%%%%%%|")
    print("   |A ||B ||C ||D ||E ||F ||G ||H ||I ||j |")
    print("   +--++--++--++--++--++--++--++--++--++--+")
    


    hits_var = [24,66,87]
    very_near = [1,5,9]
    miss_var = [3,7,88,22,44]
    grid_space_counter = 0 
    for x in range(30):
        insert_symbol = " "
        if x >= 10:
            insert_symbol = ""
        for y in range(10):
            symbol= "|---|"
            if grid_space_counter in hits_var:
                symbol= "|-x-|"
            if grid_space_counter in very_near:
                symbol= "|-1-|"
            if grid_space_counter in miss_var:
                symbol= "|-0-|"
            insert_symbol = insert_symbol + symbol
            grid_space_counter = grid_space_counter + 1 
            # if x == 10:




        #     """ Alows for double didgets in spacing """ 
        #     print(x,("|--|")*11)
        # else:
        
        
        print(x,"",insert_symbol) 
        # print(grid_space_counter)


create_game_board()





        #       if x == 10:
        #     """ Alows for double didgets in spacing """ 
        #     print(x,("|--|")*11)
        # else:
        #     print(x,"",("|--|")*11) 
        




# def print_board(board):
#     print("  A B C D E F G H")
#     print("  +-+-+-+-+-+-+-+")
#     row_number = 1
#     for row in board:
#         print("%d|%s|" % (row_number, "|".join(row)))
#         row_number += 1





















































































# def make_playbord_in_sheet(data):
#     """ 
#     Create a board for the game in ICEBERG sheet
#     """ 


# for cell in grids_sheet.range('a1:b2'):
#     print(cell.value)

# print(grids_sheet.acell('b1').value)
# print(grids_sheet.cell(1,1).value)


# i=1
# 

# def create_game_array(grid_size):
#     i = 1
    
#     alpha_var = '`' 
#     while i <= grid_size:
#         dump_num1 = bytes(alpha_var, 'utf-8')
#         dump_num2 = dump_num1[0] + 1
#         alpha_var = (chr(dump_num2))
#         i += 1
#         odin = 1
#         while odin  <= 18:
#             num_var = str(odin)
#             cell_var = str(alpha_var+num_var)
#             odin += 1
#             # print(cell_var)
#             my_array= []git ststus
#             my_array.append(cell_var)
#             print(my_array)
#             grids_sheet.update_acell(cell_var,0)
            
           
#         # 

#         # return my_array

# create_game_array(2)

