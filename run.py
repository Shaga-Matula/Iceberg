"""
Welcome to the Iceberge Game Python Project PP_03
for Code Instatute By Paul Gleeson 21/04/2023
"""

# Gsheets and Json credintial file.
# importing the random module


import random
import os  # Import for screen refresh
import json
# Import for timer
import time
import gspread
from google.oauth2.service_account import Credentials


# Imports colored print
from colorama import Fore, Style
# ## ########### Gsheets connection ################
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

# Inform user of bad connection to gsheets
try:
    if SHEET.worksheet('grid'):
        print("Connect to Gsheets OK!!! ")
        input("\n\n       Press Enter to continue.")
except gspread.exceptions.GSpreadException as e:
    print(f"\n\n\n   A Gsheets exception occurred ==> {e}")
    print("\n     Cannot connect to Gsheets")
    print("\n     You can still play but cant save your score")
    input("\n\n       Press Enter to continue.")

# ## ##### Main program ########################

# Declair variables
very_near = []
direct_hit_list = []
miss_var = []
hit_list = []
user_shot_taken = []
user_number = ()
run_help = "help"

# Start the game timer
start_time = time.time()


def print_rules():  # Rules of the game
    """
    This function prints the help file to screen
    """
    global run_help
    if run_help == "help":
        print("\n\n")
        os.system('cls' if os.name == 'nt' else 'clear')
        print((Fore.YELLOW + "     |%%%%%%%%%%%%%--%%%  ICEBERG"
                             "%%%--%%%%%%%%%%%%|\n" + Style.RESET_ALL))
        print("  Hello and welcome to Iceberg, a game of cunning and guile.\n")
        print("  The object of the game is to destroy 3 Icebergs to clear a")
        print("  path for your ship to cross, but! It's foggy and you cannot ")
        print("  see, fortunately the sea is flat as a pancake and you can")
        print("  hear the sound of dripping water as the icebergs melt.")
        print("  'It's so quiet' you hear the first mate say,'It's so quiet'.")
        print("\n  Use this tranquility to your advantage, your crew will")
        print("  listen out for the sound of ice crushing under the ")
        print("  weight of your torpedoes as you hunt in the fog for")
        print("  the ICEBERG's")
        input("\n \n  Press Enter to continue." + Style.RESET_ALL)
        os.system('cls' if os.name == 'nt' else 'clear')
        print((Fore.YELLOW + "     |%%%%%%%%%%%%%--%%%  ICEBERG"
                             "%%%--%%%%%%%%%%%%|\n" + Style.RESET_ALL))
        print("  You can achieve your goal by selecting Coordinates to launch")
        print("  your torpedoes into the foggy night.\n")
        print("  Firstly select a letter from the top row of A to J.\n")
        print("  The first letter is not case sensitive")
        print("  Then insert a colon : to separate letters from numbers\n")
        print("  After the colon you can select a number from 01 to 20")
        print("  An example of this would be B:02, for Column b row 2.\n")
        print("  Row number under 10 it must be preceded with a 0")
        print("  An example of this for Column h row 2, would be H:02 \n")
        input("\n \n  Press Enter to continue." + Style.RESET_ALL)
        os.system('cls' if os.name == 'nt' else 'clear')
        print((Fore.YELLOW + "     |%%%%%%%%%%%%%--%%%  ICEBERG"
                             "%%%--%%%%%%%%%%%%|\n" + Style.RESET_ALL))
        print(
            "  Icebergs are huge and 90% is hidden underwater, so you will")
        print("  need to hit it dead centre to destroy the Iceberg.\n")
        print("  Thus you may hit outside of the Iceberg before you hit its")
        print("  center")
        print("\n  If so, the computer will display a 1, if it’s a miss you ")
        print("  get a 0. Icebergs take up 9 spaces, X in middle, surrounded")
        print("  by 1's.\n\n  The game is over when you sink all 3 Icebergs ")
        print("  or quit game. \n")
        print("  Good luck captain and God Speed! \n\n")
        input("  Press Enter to continue.")
        os.system('cls' if os.name == 'nt' else 'clear')
        print((Fore.YELLOW + "     |%%%%%%%%%%%%%--%%%  ICEBERG"
                             "%%%--%%%%%%%%%%%%|\n" + Style.RESET_ALL))
        print(Fore.BLUE + "\n  The game will reveal the complete Iceberg if")
        print(Fore.BLUE + "  you smash it's center")
        print(Fore.BLUE + "\n  If you smash all three Icebergs.. You Win!")
        print(Fore.BLUE + "  If you enter end_game and quit.... You Lose!.")
        print(Fore.BLUE + "\n  If you need to see the rules again.")
        print(Fore.BLUE + "  Input 'help' to the Coordinates with no ")
        print(Fore.BLUE + "\n  quotations. If you want to quit the game.")
        print(Fore.BLUE + "  Input 'end_game' to the Coordinates with no")
        print(Fore.BLUE + "  quotations")
        input("\n \n\n  Press Enter to continue." + Style.RESET_ALL)
        os.system('cls' if os.name == 'nt' else 'clear')
        run_help = "no_help"
        return run_help
    calculate_iceberg_squares()


def create_game_board():
    """
        This function writes the board on screen
        """
    # This prints the headder fo the game
    print(Fore.YELLOW +
          "\n      |%%%%%%%%%%%%%--%%%  ICEBURG  %%%--%%%%%%%%%%%%|")
    print(Fore.BLUE + "       A || B || C || D || E || F || G || H || I || J ")
    grid_space_counter = 1
    # loop will start at the 1 count for 20 more
    color_ama = (Fore.BLUE)
    for x in range(1, 21):
        insert_symbol = " "
        if x >= 10:
            insert_symbol = ""
        for _ in range(10):
            symbol = "|---|"
            if grid_space_counter in hit_list:
                symbol = "|-X-|"  # Hit List:Reveal = direct_hit_list
            if grid_space_counter in very_near:
                symbol = "|-1-|"  # Very Near:Reveal = tree_icebergs
            if grid_space_counter in miss_var:  # Miss Var
                symbol = "|-0-|"
            insert_symbol = insert_symbol + symbol
            grid_space_counter = grid_space_counter + 1

        print(color_ama + " " + (f"{x}  {insert_symbol}"))


# These are the exclusions for the outer frame of the game/Shorten later
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

############################################################################

tree_icebergs = []
ice_burg_container = []
iceberg_one = []
iceberg_two = []
iceberg_three = []
outer_numbers = []
direct_hit_list = []

doit = "notdone"


def calculate_iceberg_squares():
    """
    This function will pick a random number between 1 and 200 that is not in
    the excluded list and return the value of 3 sets of 9 numbers
    Representing the icebergs
    """
    global doit
    if doit == ("notdone"):
        # Pick randam number and compair to exclusion list
        x = 1
        while x <= 3:
            num = random.choice(
                [i for i in range(1, 200) if i not in excluded_numbers])
            direct_hit_list.append(num)
            # Place all 8 surounding boxes into exclusion array
            ice_burg_container = num + 1, num - 1, num + 10, num - 10, \
                num - 9, num + 9, num - 11, num + 11
            # Calculate outer box from given randam number
            outer_top = num - 18, num - 19, num - 20, num - 21, num - 22
            outer_left_right = num - 2, num - 12, num - 8, \
                num + 2, num + 12, num + 8
            outer_bottom = num + 18, num + 19, num + 20, num + 21, num + 22
            outer_numbers = outer_bottom + outer_left_right + outer_top
            # Merge all 3 iceburg 3x3 into tree iceburg array
            tree_icebergs.extend(ice_burg_container)
            # Merge all numbers to exclusion array
            excluded_numbers.extend(tree_icebergs)
            excluded_numbers.extend(outer_numbers)

        # ########## Separate Icebergs for reveal ################

        # Note DRY if time
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


def error_1(chestnut):  # Prints out user errors
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n")
    print(chestnut)
    input("\n \n Press Enter to continue.")
    main()


def get_user_input():
    """
     This function validates the input data from the user.
    """
    chestnut = []
    allowed_letters = "abcdefghijABCDEFGHIJ"
    user_shot = input("\n Please Choose Coordinates Captain:")

    if user_shot == "help":  # run the help file and display rules of play
        os.system('cls' if os.name == 'nt' else 'clear')
        global run_help
        run_help = ("help")
        print("\n\n\n\n\n\n\n\n\n\n You have chosen help.")
        print("\n You will be returned to game when finished!!")
        input("\n \n Press Enter to continue.")
        print_rules()
        calculate_iceberg_squares()
        return run_help

    if user_shot == "end_game":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(
            "\n\n\n\n\n\n\n\n\n\n You have chosen to end game.")
        print("\n Please come back soon!!")
        input("\n \n Press Enter to continue.")
        quit()

    if user_shot == "":  # If the string is empty
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n \n \n \n \n \n \n You have not entered any")
        print("\n characters, you must choose 4, eg b:12")
        print("\n Please Try Again :")
        input("\n \n Press Enter to continue.")
        os.system('cls' if os.name == 'nt' else 'clear')
        return "error"

    # If user inputs upper case make lower case

    if (user_shot[0].isalpha()):
        if user_shot[0].isupper():
            user_shot = user_shot.swapcase()

    if user_shot == "error":  # there was an error
        main()
    elif (len(user_shot)) != 4:  # Error if more than 4 digets
        chestnut = "\n\n\n\n\n\n\n\n\n\n Incorrect number" \
                   "of inputs, you must choose 4. Please try again"
        error_1(chestnut)
    elif not (user_shot[0].isalpha()):  # Error if not a letter
        chestnut = (
            f"\n\n\n\n\n\n\n\n\n\n Your first input was {user_shot[0]}."
            " This must be a letter between A and J. Please try again"
        )
        error_1(chestnut)
    elif user_shot[0] not in allowed_letters:  # Error if not in list a to j
        chestnut = (
            f"\n\n\n\n\n\n\n\n\n\n Your first input was {user_shot[0]}"
            " it must be between A and J. Please try again"
        )
        error_1(chestnut)
    elif (user_shot[1]) != ":":  # Error if not a colon :
        chestnut = (
            "\n\n\n\n\n\n\n\n\n\n Your second input. It must be a colon :"
        )
        error_1(chestnut)
    elif not (user_shot[2].isdigit()):  # Error if not a number diget
        chestnut = (
            "\n\n\n\n\n\n\n\n\n\n Third input must be a number => 0, 1 or 2 "
        )
        error_1(chestnut)
    elif int(user_shot[2]) >= 3:  # Error if value is over 20 in choce
        chestnut = (
            "\n\n\n\n\n\n\n\n\n\n  Out of range 3rd diget must be 0, 1 or 2 ")
        error_1(chestnut)
    elif int(user_shot[2]) == 2 and int(
            user_shot[3]) != 0:  # Error if value is over 20 in choce
        chestnut = (
            "\n\n\n\n\n\n\n\n\n\n First diget is 2 second diget can"
            "only be 0 as the range is 1 to 200"
        )
        error_1(chestnut)
    elif not (user_shot[3].isdigit()):  # Error if not a number
        chestnut = (
            f"\n\n\n\n\n\n\n\n\n\n Fourth input {user_shot[3]}"
            "must be a number => 1, 2, 3, 4 etc "
        )
        error_1(chestnut)
    elif user_shot in user_shot_taken:  # If Duplicate input
        chestnut = (
            "\n\n\n\n\n\n\n\n\n\n Sorry, you have already"
            "inputed these coordinates:... Please try again"
        )
        error_1(chestnut)
        # Error
    elif int(user_shot[2]) == 0 and int(user_shot[3]) == 0:
        chestnut = (
            "\n\n\n\n\n\n\n\n\n\n Sorry 00 is out of range"
        )
        error_1(chestnut)
    else:
        user_shot_taken.append(user_shot)

    return user_shot


create_game_board()


############################################################################


dict_1 = {}


def translate_user_input(user_input):
    """
This function compares the user input to its coordinates and
translates it to board grid.. A:01 = 01 B:01 = 02 and so on.
"""
    letters = []
    for i in range(97, 107):
        letters.append(chr(i))
        numbers = (list(range(1, 21)))

        # If the number is between 1 to 9 make double diget
        for i in range(len(numbers)):
            if numbers[i] <= 9:
                numbers[i] = str(numbers[i]).zfill(2)  # Adds leading zero to
        # Set format of string eg b:02
        final = []
        i = 0
        for i in (numbers):
            for content in (letters):
                num = content + ":" + str(i)
                alpha_num = num.strip()
                final.append(alpha_num)
        # Zip to directory
        values = (list(range(1, 201)))
        dict_1 = dict(zip(final, values))

    user_shot = (dict_1.get(user_input))

    return user_shot


def check_hits():  # User experience feedback
    """
    This function calculates hit and misses
    """
    usr_input = get_user_input()
    if usr_input == "error":
        usr_input = ""
        main()

    user_number = translate_user_input(usr_input)

    if user_number in direct_hit_list:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\n Its a hit Captain, its a hit!!, you've smashed an Iceberg"
              "captain")
        input("\n \n Press Enter to continue.")
        hit_list.append(user_number)
        #  ######################### Reveal if correct ######################

        # Note DRY
        
        if user_number in iceberg_one:  # If user hits iceberg
            del iceberg_one[0]          # reveal surounding
            for element in iceberg_one:
                very_near.append(element)
                user_shot_taken.append(element)
        elif user_number in iceberg_two:  # If user hits iceberg
            del iceberg_two[0]            # reveal surounding
            for element in iceberg_two:
                very_near.append(element)
                user_shot_taken.append(user_number)
        elif user_number in iceberg_three:  # If user hits iceberg
            del iceberg_three[0]            # reveal surounding
            for element in iceberg_three:
                very_near.append(element)
                user_shot_taken.append(user_number)

        ##############################
    elif user_number in tree_icebergs:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\n\n\n\n Youv'e cliped one Captain its a near hit!!!")
        print("\n You're close to a Iceberg Captain")
        input("\n \n Press Enter to continue.")
        very_near.append(user_number)
        user_shot_taken.append(user_number)
    else:
        miss_var.append(user_number)
        user_shot_taken.append(user_number)

    if (len(hit_list) == 3):  # Winner will call calculate_score()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\n\n\n\n You did it Captain, You did it, were saved ")
        print(" \n         Congratulations You WON!!!!!!!\n\n")
        calculate_score()


def calculate_score():
    """
    This function calculates the user time and rank
    using Gsheets.

    """
    if SHEET.worksheet('grid'):
        elapsed_time = time.time() - start_time  # Calculate time spent
        # Here we can update the spreadsheet with time spent
        users_time_score = [elapsed_time]
        grids_sheet.append_row(users_time_score)
        print("\n Updating Gsheets .... ")
        elapsed_time = time.strftime(
            "%M Min and %S Sec", time.gmtime(elapsed_time)
        )  # Format time for display
        print(f"\n Your time was {elapsed_time} Captain\n\n")
        input(" Press Enter to continue.")

        scors_list = []  # Call first 10 cells
        for cell in grids_sheet.range('A1:A10'):
            scors_list.append(cell.value)

        for element in users_time_score:
            scors_compair = []
            scors_list.append(str(element))
            scors_compair.append(str(element))

        scors_list.sort()  # Index the list and compair user time
        index = scors_list.index(scors_compair[0])
        print(f"\n You are ranked number {index + 1} in the score list")
        print("\n Well done captain ")
        input("\n Press enter to continue")
    else:
        print("Gsheets unavailable")


create_game_board()


def main():
    """
    Main program
    """
    print_rules()
    calculate_iceberg_squares()
    create_game_board()
    check_hits()
    main()


main()
