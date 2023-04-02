import gspread
from google.oauth2.service_account import Credentials
import json
import os

# importing the random module
import random

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
    hits_var = []
    # very_near = [1,5,9]
    miss_var = []
    """
    This function writes the board on screen
    """
    print("     |%%%%%%%%%%%%%--%%%  ICEBURG  %%%--%%%%%%%%%%%%|\n")
    print("    | A || B || C || D || E || F || G || H || I || J |")
    print("    +---++---++---++---++---++---++---++---++---++---+")
    
   
    
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
        
        print(x,"",insert_symbol) 
      
def pick_calculate_iceberg_squares():
    """
    # This function will pick a random number between 1,100 thet is not in the excluded list and 
    # return the value
    """
    excluded_numbers = [1,2,3,4,5,6,7,8,9,10,11,21,31,41,51,61,71,81,91,20,30,40,50,60,70,80,90,100,0]
    random_number = random.choice([i for i in range(1, 280) if i not in excluded_numbers])
    print(random_number)
    return random_number

def get_squares(num):
    my_iceberg_numbers = []
    new_num = num, num +1, num -1, num + 10, num -10, num -9, num + 9, num -11, num + 11
    return new_num

the_number = pick_calculate_iceberg_squares()
very_near = get_squares(the_number)
print(very_near)

# print(f"THE END {the_number}")
create_game_board()




get_num = 0
    # print(f"This is the value before {get_num}")
    # get_num = random.randint(1,100)
    # print(f"This is the randam mumber {get_num}")
    # if not get_num in exclude:
    #     print(f"Its Not in the list {get_num} great")
    #     return get_num
    # else:
    #     get_num = get_num
    #     print(f"Yes its HEREEEEE {get_num}")
    
    #     # get_num = get_num.pop()



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

