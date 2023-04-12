# import gspread
# from google.oauth2.service_account import Credentials
import json
import os
from colorama import Fore, Back, Style
import json
import os
from colorama import Fore, Back, Style

# importing the random module
import random
# importing string for alpha betic calculation
import string
#import sys for break in loops
import sys

# SCOPE = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive.file",
#     "https://www.googleapis.com/auth/drive"
# ]

# creds = json.load(open('creds.json'))
# CREDS = Credentials.from_service_account_info(creds)
# SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# SHEET = GSPREAD_CLIENT.open("Iceberg")

# grids_sheet = SHEET.worksheet('grid')
# data = grids_sheet.get_all_values()

very_near = []
print(f"Very near here = {very_near}")
direct_hit_list = []
miss_var = []
hit_list = []
played_shot_hist = []
user_number = ()

def create_game_board():
        print(f"Ice berg List {direct_hit_list}")
        print(f"Mises {miss_var}")
    
        """
        This function writes the board on screen
        """
        #This prints the headder fo the game
        print(Fore.YELLOW + "\n     |%%%%%%%%%%%%%--%%%  ICEBURG  %%%--%%%%%%%%%%%%|")
        print(Fore.BLUE + "    | A || B || C || D || E || F || G || H || I || J |")
        # print(Fore.GREEN + "    +---++---++---++---++---++---++---++---++---++---+")
        grid_space_counter = 1
        # loop will start at the 1 count for 20 more
        color_ama = (Fore.BLUE)
        for x in range(1,21):
            insert_symbol = " "
            if x >= 10:
                insert_symbol = ""
            for y in range(10):
                symbol= "|---|"
                if grid_space_counter in hit_list:
                    # if grid_space_counter in direct_hit_list:
                    symbol= "|-X-|"
                if grid_space_counter in very_near:
                    symbol= "|-1-|"
                if grid_space_counter in miss_var:
                    symbol= "|-0-|"
                insert_symbol = insert_symbol + symbol
                grid_space_counter = grid_space_counter + 1 
            
            print(color_ama + (f"{x}  {insert_symbol}"))
        

#These are the exclusions for the outer frame of the game/Note to shorten later if time
top_row = [1,2,3,4,5,6,7,8,9]
right_row = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190]
left_row = [11,21,31,31,41,51,61,71,81,91,101,111,121,131,141,151,161,171,181,191]
bottom_row = [192,193,194,195,196,197,198,199,200]
excluded_numbers = top_row + right_row + left_row + bottom_row

##########################################################################################

tree_icebergs = [] 
ice_burg_container = []
outer_numbers = []
direct_hit_list= []

doit = "notdone"
def calculate_iceberg_squares():
    global doit 
    if doit == ("notdone"):
        # This function will pick a random number between 1,200 that is not in the excluded list and 
        # return the value of 3 sets of 9 numbers representing the icebergs
        
        # Declair variables needed
    

        # Pick randam number and compair to exclusion list
        x = 1
        while x <= 3:
            print(x)
            num = random.choice([i for i in range(1, 200) if i not in excluded_numbers])
            direct_hit_list.append(num)
            print(f"core excluded numbers == {num}") 
            #Place all 8 surounding boxes into exclusion array  
            ice_burg_container = num +1, num -1, num + 10, num -10, num -9, num + 9, num -11, num + 11
            
            #Calculate outer box from given randam number
            outer_top = num -18, num -19, num -20, num -21, num -22
            outer_left_right = num -2, num -12, num - 8, num + 2, num + 12, num +8
            outer_bottom = num + 18, num + 19, num + 20, num + 21, num +22
            outer_numbers = outer_bottom + outer_left_right + outer_top
            
            #Merge all 3 iceburg 3x3 into tree iceburg array
            tree_icebergs.extend(ice_burg_container)
            
            #Merge all numbers to exclusion array 
            # excluded_numbers.extend(tree_icebergs)
            excluded_numbers.extend(outer_numbers)
            x += 1
        
        
            print(f"excluded numbers == {excluded_numbers}") 
            print(f"core excluded numbers == {direct_hit_list}") 
            doit = "done"
        print(f"Outer Numbers == {tree_icebergs}") 
        return tree_icebergs


#############################################################################
user_shot_taken = []
def get_user_input():
    allowed_letters = "abcdefghijABCDEFGHIJ"
    """
    This function valadates the input data from the user
    """
    # print("\n    ##################################################")
    # print("\n Please input target cordanance ...\n")
    # print("It must be a letter first then a number")
    # print("If the number is single diget please use a '0'") 
    # print("to fill. Eg one = 01 six = 06")
    # print("With a colon seperating eg.. b:06 or B:05 or c:16 \n")
    user_shot = input("\n Choose coordinates:" )
    
    
    
    # if user_shot in user_shot_taken:
        
    #     print(f"This is User shot before ==:  {user_shot} ")
    #     os.system('cls' if os.name == 'nt' else 'clear')
    #     print("\n \n You have already inputed these coordinates:... Please try again")
       
    #     wait = input("\n \n Press Enter to continue.")

    #     return "error"
    #     main()

    # user_shot = user_shot[0].lower() + user_shot[1:]
    # print(f"This is User shot before ==:  {user_shot} ")
    # user_shot_taken.append(user_shot)
    
    if user_shot == "":# if string is empty
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Incorrect number of charictors, you must choose 4. Please try again")
        wait = input("\n \n Press Enter to continue.")
        return "error"
        main()
    
    if (user_shot[0].isalpha()) == True:# If user inputs upper case make lower case
        if user_shot[0].isupper() == True:
            user_shot = user_shot.swapcase()
            print(f"its upper {user_shot[0]}")
        
    print(f"User shot ... After empty and Lower case ==  {user_shot}")
        
    if user_shot == "error":#there wans an error 
        print("################ error")
        print("Try Again :")
        main()
    elif (len(user_shot)) != 4: #Error if more than 4 digets
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Incorrect number of inputs, you must choose 4. Please try again")
        wait = input("\n \n Press Enter to continue.")
        user_shot = "error"
        main()
    elif (user_shot[0].isalpha()) != True: #Error if not a letter
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"You first input was {user_shot[0]}. This must be a letter betwwn A and J ")
        wait = input("\n \n Press Enter to continue.")
        user_shot = "error"
        main()
    elif user_shot[0] not in allowed_letters:#Error if not in list a to j
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Your first input was {user_shot[0]} it must be between A and J. Please try again")
        wait = input("\n \n Press Enter to continue.")
        user_shot = "error"
        main()
        wait = input("Press Enter to continue.")
    elif (user_shot[1]) != ":":# Error if not a colon :
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Second input {user_shot[1]} must be a colon => : ")
        wait = input("\n \n Press Enter to continue.")
        user_shot = "error"
        main()
    elif (user_shot[2].isdigit()) != True:#Error if not a number diget
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Third input {user_shot[2]} must be a number")
        wait = input("\n \n Press Enter to continue.")
        user_shot = "error"
        main()
    elif int(user_shot[2]) >= 3: #Error if value is over 20 in choce 
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Your third input was {user_shot[2]} It must be 0, 1 or 2 only ")
        wait = input("\n \n Press Enter to continue.")
        user_shot = "error"
        main()
    elif (user_shot[3].isdigit()) != True:#Error if not a number
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Your fourth input was {user_shot[3]} it must be a number. Please try again")
        wait = input("\n \n Press Enter to continue.")
        user_shot = "error"
        main()
    elif user_shot in user_shot_taken:# If Duplicate input
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n \n You have already inputed these coordinates:... Please try again")
        wait = input("\n \n Press Enter to continue.")
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
    else:
        print(f"After all checks User shot =  {user_shot}")
        user_shot_taken.append(user_shot)
        print(f"After append =  {user_shot_taken}")
    return user_shot
#################################################################################
"""
This function compaires the user input to its coradnents and translates to board

"""
dict_1 = {}

def translate_user_input(user_input):
    letters = []
    print(f"User input at start of tui = {user_input}")
    for i in range(97, 107):
        letters.append(chr(i))
        numbers = (list(range(1, 21)))
        # print(numbers)
        #If the number is between 1 to 9 make double diget  
        for i in range(len(numbers)):
            if numbers[i] <= 9:
                numbers[i] = str(numbers[i]).zfill(2)#Adds leading zero to
        #Set format of string eg b:12
        final = []
        i = 0
        for i in (numbers):
            for content in (letters):
                num = content + ":" + str(i)
                alpha_num = num.strip()
                final.append(alpha_num)
        #Zip to directory
        values = (list(range(1, 201)))
        dict_1 = dict(zip(final, values))
 

    # print(f"Final_zip =  {final}")
    # print(f"Values zip =  {values}")
    # print(f"Dict_1 =  {dict_1}")
    user_shot = (dict_1.get(user_input))
    print(f"User input =  {user_input}")
   

    return user_shot
    
   
# for cell in grids_sheet.range('a1:b2'):
#      print(cell.value)
    

def main():
    calculate_iceberg_squares()
    create_game_board()
    usr_input = get_user_input()
    if usr_input == "error":
        print("Its an error")
        usr_input = ""
        main()
    
    
    
    print(f"User input (Main) = {usr_input}")
    user_number = translate_user_input(usr_input)
    print(f"Main My User Num (return from transl) =  {user_number}")
    
    print(user_number)
    print(direct_hit_list)
    
    
    if user_number in direct_hit_list:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Its a hit Captain its a hit!!!, you sunk an Iceberg captain")
        wait = input("\n \n Press Enter to continue.")
        hit_list.append(user_number)
        played_shot_hist.append(user_number)
    elif user_number in tree_icebergs:
        very_near.append(user_number)
        played_shot_hist.append(user_number)
    else:
        miss_var.append(user_number)
        played_shot_hist.append(user_number)
    
    if  (len(hit_list) == 3):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Yeaaaa You Win, you got all three Icebergs ")
            wait = input("Press Enter to continue.")

        

    
    
    print(f"Very near 1 = {very_near}")
   
    main()



main()


