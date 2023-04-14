
import json

#This allows identity of operating system
import os

#Imports colored print
from colorama import Fore, Back, Style

# importing the random module
import random
# importing string for alpha betic calculation
import string
#import sys for break in loops
import sys


very_near = []
direct_hit_list = []
miss_var = []
hit_list = []
user_shot_taken = []
user_number = ()


def print_rules():# Rules of the game
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.YELLOW +
          "\n     |%%%%%%%%%%%%%--%%%  ICEBURG  %%%--%%%%%%%%%%%%|" +
          Style.RESET_ALL)
    print("\n   Hello and welcome to Icebberge, a game of cunning and guile\n")
    print("   The object of the game is to destroy 3 Icebergs to clear a")
    print("   path for your shipto cross, but! its fogy and you cant see.")
    print("\n   This is done by selecting Coordinates to launch your torpedos")
    print("   Firstly select a letter from the top row of A to J.\n")
    print("   Then insert a colon : to seperate letters from numbers\n")
    print("   After the colon you can select a number from 1 to 20")
    print(Fore.BLUE + "   Please note the input must be 4 char long" +
          Style.RESET_ALL)
    print("   An example of this would be B:12, for colume b row 12\n")
    print("   If you choose row number under 10 it must be precede with an 0")
    print("   An example of this for colum h row 2, would be H:02 \n")
    print(
        "   Icebures are huge and 90% is hidden underwater, so you will need")
    print("   hit it dead center to destroy the Iceberg.")
    print(
        "   Thus you may hit outside of the Iceberg before you can hit its center."
    )
    print("   If so the computer will display a 1, if its a miss you get a 0")
    print("   An example of this for colum h row 2, would be H:02 \n\n")


def create_game_board():
  
    """
        This function writes the board on screen
        """
    #This prints the headder fo the game
    print(Fore.YELLOW +
          "\n     |%%%%%%%%%%%%%--%%%  ICEBURG  %%%--%%%%%%%%%%%%|")
    print(Fore.BLUE + "    | A || B || C || D || E || F || G || H || I || J |")
    # print(Fore.GREEN + "    +---++---++---++---++---++---++---++---++---++---+")
    grid_space_counter = 1
    # loop will start at the 1 count for 20 more
    color_ama = (Fore.BLUE)
    for x in range(1, 21):
        insert_symbol = " "
        if x >= 10:
            insert_symbol = ""
        for y in range(10):
            symbol = "|---|"
            if grid_space_counter in hit_list:  #Hit List:Reveal = direct_hit_list
                symbol = "|-X-|"
            if grid_space_counter in very_near:  #Very Near:Reveal = tree_icebergs
                symbol = "|-1-|"
            if grid_space_counter in miss_var:  #Miss Var
                symbol = "|-0-|"
            insert_symbol = insert_symbol + symbol
            grid_space_counter = grid_space_counter + 1

        print(color_ama + (f"{x}  {insert_symbol}"))


#These are the exclusions for the outer frame of the game/Note to shorten later if time
top_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
right_row = [
    10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170,
    180, 190
]
left_row = [
    11, 21, 31, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 151, 161,
    171, 181, 191
]
bottom_row = [192, 193, 194, 195, 196, 197, 198, 199, 200]
excluded_numbers = top_row + right_row + left_row + bottom_row

##########################################################################################

tree_icebergs = []
ice_burg_container = []
iceberg_one = []
iceberg_two = []
iceberg_three = []
outer_numbers = []
direct_hit_list = []

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
            num = random.choice(
                [i for i in range(1, 200) if i not in excluded_numbers])
            direct_hit_list.append(num)
       
            #Place all 8 surounding boxes into exclusion array
            ice_burg_container = num + 1, num - 1, num + 10, num - 10, num - 9, num + 9, num - 11, num + 11
            
         
            #Calculate outer box from given randam number
            outer_top = num - 18, num - 19, num - 20, num - 21, num - 22
            outer_left_right = num - 2, num - 12, num - 8, num + 2, num + 12, num + 8
            outer_bottom = num + 18, num + 19, num + 20, num + 21, num + 22
            outer_numbers = outer_bottom + outer_left_right + outer_top

            #Merge all 3 iceburg 3x3 into tree iceburg array
            tree_icebergs.extend(ice_burg_container)

            #Merge all numbers to exclusion array
            excluded_numbers.extend(tree_icebergs)
            excluded_numbers.extend(outer_numbers)

        ############# seperate Iceburgs for reveal ################
            if x == 1:
                iceberg_one.append(num)   
                for element in ice_burg_container:
                    iceberg_one.append(element)
            elif x == 2:
                iceberg_two.append(num)   
                for element in ice_burg_container:
                    iceberg_two.append(element)
            elif x == 3:
                iceberg_three.append(num)   
                for element in ice_burg_container:
                    iceberg_three.append(element)
            
            x += 1
            doit = "done"

        return tree_icebergs


#############################################################################

user_shot_taken = []

def error_1(chestnut):  #Prints out user errors
    os.system('cls' if os.name == 'nt' else 'clear')
    print(chestnut)
    wait = input("\n \n Press Enter to continue.")
    user_shot = "error"
    main()


def get_user_input():
    chestnut = []

    allowed_letters = "abcdefghijABCDEFGHIJ"
    """
    This function valadates the input data from the user.
    """

    user_shot = input("\n Please Choose Coordinates Captain:")

    if user_shot == "end_game":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(
            "\n\n\n\n\n\n\n\n\n\n You have chosen to end game. Come back soon!!"
        )
        wait = input("\n \n Press Enter to continue.")
        quit()

    if user_shot == "":  # If the string is empty
        print("Incorrect number of charictors, you must choose 4")
        print("Try Again :")
        return "error"
        main()

    if (user_shot[0].isalpha()
        ) == True:  # If user inputs upper case make lower case
        if user_shot[0].isupper() == True:
            user_shot = user_shot.swapcase()

    if user_shot == "error":  #there was an error
        main()
    elif (len(user_shot)) != 4:  #Error if more than 4 digets
        chestnut = "\n\n\n\n\n\n\n\n\n\n Incorrect number of inputs, you must choose 4. Please try again"
        error_1(chestnut)
    elif (user_shot[0].isalpha()) != True:  #Error if not a letter
        chestnut = (
            f"\n\n\n\n\n\n\n\n\n\n Your first input was {user_shot[0]}. This must be a letter between A and J. Please try again"
        )
        error_1(chestnut)
    elif user_shot[0] not in allowed_letters:  #Error if not in list a to j
        chestnut = (
            f"\n\n\n\n\n\n\n\n\n\n Your first input was {user_shot[0]} it must be between A and J. Please try again"
        )
        error_1(chestnut)
    elif (user_shot[1]) != ":":  # Error if not a colon :
        chestnut = (
            f"\n\n\n\n\n\n\n\n\n\n Your second input was {user_shot[1]} sorry it must be a colon => : "
        )
        error_1(chestnut)
    elif (user_shot[2].isdigit()) != True:  #Error if not a number diget
        chestnut = (
            f"\n\n\n\n\n\n\n\n\n\n Third input {user_shot[2]} must be a number => 0, 1 or 2 "
        )
        error_1(chestnut)
    elif int(user_shot[2]) >= 3:  #Error if value is over 20 in choce
        chestnut = (
            f"\n\n\n\n\n\n\n\n\n\n  Out of range 3rd diget must be 0, 1 or 2 ")
        error_1(chestnut)
    elif int(user_shot[2]) == 2 and int(
            user_shot[3]) != 0:  #Error if value is over 20 in choce
        chestnut = (
            f"\n\n\n\n\n\n\n\n\n\n If the first diget is 2 second diget can only be 0 as the range is 1 to 200"
        )
        error_1(chestnut)
    elif (user_shot[3].isdigit()) != True:  #Error if not a number
        chestnut = (
            f"\n\n\n\n\n\n\n\n\n\n Third input {user_shot[3]} must be a number => 1, 2,  etc "
        )
        error_1(chestnut)
    elif user_shot in user_shot_taken:  # If Duplicate input
        chestnut = (
            "\n\n\n\n\n\n\n\n\n\n Sorry, you have already inputed these coordinates:... Please try again"
        )
        error_1(chestnut)
    else:
        user_shot_taken.append(user_shot)
     
    return user_shot
create_game_board()

#################################################################################
"""
This function compaires the user input to its coradnents and translates to board

"""
dict_1 = {}


def translate_user_input(user_input):
    letters = []
    for i in range(97, 107):
        letters.append(chr(i))
        numbers = (list(range(1, 21)))

        #If the number is between 1 to 9 make double diget
        for i in range(len(numbers)):
            if numbers[i] <= 9:
                numbers[i] = str(numbers[i]).zfill(2)  #Adds leading zero to
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

    user_shot = (dict_1.get(user_input))

    
    return user_shot

def check_hits():#User experience feedback
    usr_input = get_user_input()
    if usr_input == "error":
        print("Its an error")
        usr_input = ""
        main()

    user_number = translate_user_input(usr_input)
 
    if user_number in direct_hit_list:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Its a hit Captain its a hit!!!, you sunk an Iceberg captain")
        wait = input("\n \n Press Enter to continue.")
        hit_list.append(user_number)
        ########################## Reveal if correct #########################
        if user_number in iceberg_one:# If user hits iceberg reveal surounding
            del iceberg_one[0]
            for element in iceberg_one:
                very_near.append(element)
                user_shot_taken.append(element)
        elif user_number in iceberg_two:# If user hits iceberg reveal surounding
            del iceberg_two[0]
            for element in iceberg_two:
                very_near.append(element)
                user_shot_taken.append(user_number)
        elif user_number in iceberg_three:# If user hits iceberg reveal surounding
            del iceberg_three[0]
            for element in iceberg_three:
                very_near.append(element)
                user_shot_taken.append(user_number)
        
        ##############################
    elif user_number in tree_icebergs:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Youv'e cliped one Captain its a near hit!!!, Your close to a Iceberg Captain")
        wait = input("\n \n Press Enter to continue.")
        very_near.append(user_number)
        user_shot_taken.append(user_number)
    else:
        miss_var.append(user_number)
        user_shot_taken.append(user_number)

    if (len(hit_list) == 3):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Yeaaaa You Win, your amazing .. you got all three Icebergs ")
        wait = input("Press Enter to continue.")
    
create_game_board()


def main():
    calculate_iceberg_squares()
    create_game_board()
    # usr_input = get_user_input()
    check_hits()
      

    main()


main()
