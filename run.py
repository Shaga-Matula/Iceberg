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
        

top_row = [1,2,3,4,5,6,7,8,9]
right_row = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190]
left_row = [11,21,31,31,41,51,61,71,81,91,101,111,121,131,141,151,161,171,181,191]
bottom_row = [192,193,194,195,196,197,198,199,200]
excluded_numbers = top_row + right_row + left_row + bottom_row
# print(excluded_numbers)

def pick_calculate_iceberg_squares(iceburges):
    # This function will pick a random number between 1,200 that is not in the excluded list and 
    # return the value of 3 sets of 9 numbers representing the icebergs
    
    # Declair variables needed
    x = 1
    tree_icebergs = [] 
    ice_burg_container = []
    outer_numbers = []
    # Pick randam number and compair to exclusion list
    while x <= iceburges:
        num = random.choice([i for i in range(1, 200) if i not in excluded_numbers])
        #Place all 8 surounding boxes into exclusion array  
        ice_burg_container = num, num +1, num -1, num + 10, num -10, num -9, num + 9, num -11, num + 11
        #Calculate outer box from given randam number
        outer_top = num -18, num -19, num -20, num -21, num -22
        outer_left_right = num -2, num -12, num - 8, num + 2, num + 12, num +8
        outer_bottom = num + 18, num + 19, num + 20, num + 21, num +22
        outer_numbers = outer_bottom + outer_left_right + outer_top
        #Merge all 3 iceburg 3x3 into tree iceburg array
        tree_icebergs.extend(ice_burg_container)
        #Merge all numbers to exclusion array 
        excluded_numbers.extend(tree_icebergs)
        excluded_numbers.extend(outer_numbers)
        
        x += 1
    return tree_icebergs

very_near = pick_calculate_iceberg_squares(3)
excluded_numbers.append(very_near)
create_game_board()
# The very_near var will hold iceberg cordanates and one surronding squair
# These numbers must be appended to the exclusion so there are no repeates 

# very_near 
# print(f"This is the iceberg squair {very_near}")

# Append the new iceberg location to excleded numbers 
# excluded_numbers.append(very_near)
# print(excluded_numbers)
# print(f"THE END {iceberg_location_number}")
# create_game_board()




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

