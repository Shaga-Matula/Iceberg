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
    
   
    
    grid_space_counter = 1
    # loop will start at the 1 count for 20 more
    for x in range(1,21):
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
      

top_row = [1,2,3,4,5,6,7,8,9,10]
right_row = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
left_row = [11,21,31,31,41,51,61,71,81,91,101,111,121,131,141,151,161,171,181,191,201]
bottom_row = [202,203,204,205,206,207,208,209,210]
excluded_numbers = top_row + right_row + left_row + bottom_row
print(excluded_numbers)
def pick_calculate_iceberg_squares():
    # This function will pick a random number between 1,100 thet is not in the excluded list and 
    # return the value
    # excluded_numbers = [1,2,3,4,5,6,7,8,9,10,11,21,31,41,51,61,71,81,91,20,30,40,50,60,70,80,90,100,0]
    random_number = random.choice([i for i in range(1, 200) if i not in excluded_numbers])
    print(random_number)
    return random_number

def get_squares(num):
    my_iceberg_numbers = []
    new_num_box = num, num +1, num -1, num + 10, num -10, num -9, num + 9, num -11, num + 11
    print(f"First time cal new_num {new_num_box}")
    return new_num_box

iceberg_location_number = pick_calculate_iceberg_squares()

# The very_near var will hold iceberg cordanates and one surronding squair
# These numbers must be appended to the exclusion so there are no repeates 
very_near = get_squares(iceberg_location_number)
print(f"This is the iceberg squair {very_near}")
# Append the new iceberg location to excleded numbers 
excluded_numbers.append(very_near)
print(excluded_numbers)
# print(f"THE END {iceberg_location_number}")
create_game_board()




# get_num = 0
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

