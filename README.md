
# Creator: Paul Gleeson

# Iceberg

![Start screen](assets/images/game_page.png)

&nbsp;
<hr style="border:1px solid white">

# Introduction

### Iceberg is a game of cunning and guile for one player, with an espamated play time of 15 minuets. The object of the game is to destroy 3 Icebergs to clear a path for your ship to cross. The game is cotroled by inputing coordanates to smash 3 virtual hidden Icebergs. 

## README Table Content

1. [Introduction](#Introduction)
    1. [Project Goals](#Project-Goals)
    2. [User Experience](#User-experience)
    3. [Target Audience](#Target-Audience)
2. [Technical Design](#Technical-Design)
    1. [Flowchart](#Flowchart)


<hr style="border:1px solid white">

## Project Goals

* Create a game using Python, that takes input data from the user and manipulate the data to present a game thats both interesting and enjoyable.
* Create a help file that display in clear and precice instructions on how to play.



## User experience


* Create an atmosphere using creative writing that that enbeds the user to the task.
* Create a game that gives instant and clear feed back to the user during the game.
* Create a game that track and reports all errors with feedback to the user.
* Create a game that challenging against a computer opponent.


## Target Audience
- Younger and older users who like playing games.
- Older users who want to retain ther connative abilites in later years. 
- People who want to play a 15 min game waiting for an apointment. 

<hr style="border:1px solid white">

## Technical Design


### Flowchart

<figure>
  <img src="assets/images/flowchart.png" width=500>
</figure>







### Languages
- Python 3

### Frameworks & Tools
- LucidChart
- Heroku
- Google Drive: Used as a cloud hosting platform for the spreadsheet.
- Google Spreadsheet: Used because Python does not have a built in library to store data in an external spreadsheet.
- pycodestyle: Used as a validation tool instead of pep8 online.
- gitHub
- Gitpod
- Git

## Features

### Welcome Message



### Game Board


### Game Inputs



### Game Over




## Validation

### PEP8 validation
At the time of creation, the PEP8 online Python validation website was inoperative. To validate the code, a PEP8 validator that is built into the GitPod Workspace was used.

1. Run the command 'pip3 install pycodestyle'. (Note that this extension may already be installed, in which case this command will do nothing.)
2. In the workspace, press Ctrl+Shift+P (or Cmd+Shift+P on Mac).
3. Type the word 'linter' into the search bar that appears. 
4. Click on 'Python: Select Linter' from the filtered results.
5. Select 'pycodestyle' from the list.
6. PEP8 errors will now be underlined in red, as well as being listed in the PROBLEMS tab beside the terminal.

There were no errors or warnings flagged in login.py.
There were no errors or warnings flagged in test_login.py
15 yellow warnings were flagged in run.py. These are down to the symbol combinations used in the ASCII art and logo. These are printed direct to the console and not used in any functions.


### Testing user stories


## Deployment
Use the following steps to deploy the poject to Heroku:
1. Use the "pip freeze -> requiremnts.txt" command in the gitPod terminal; to save any libraries that need to be installed to the project files in Heroku.
2. Login or create a Heroku account.
3. Click the "New" button in the upper right corner and select "Create New App".
4. Choose an app name and your region and click "Create App". Note: the app name must be unique.
5. Go to the "Settings" tab, add the python build pack and then the node.js build pack. This is to ensure the project functions correctly with the Code Institute pre-installed template.
6. Create a "Config VAR" with the 'CREDS' key and the enter the value of the creds.json file.
7. Create a second "Config VAR" with the key of 'PORT' and value of '8000'
8. Go to the "Deploy" tab and pick GitHub as a deployment method.
9. Search for a repository to connect to.
10. Click enable automatic deploys and then deploy branch.
11. Wait for the app to build and then click on the "View" link.

You can fork the repository by following these steps:
1. Go to the GitHub repository.
2. Click on the Fork button in the upper right-hand corner.

You can clone the repository by following these steps:
1. Go to the GitHub repository.
2. Locate the Code button above the list of files and click it.
3. Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard.
4. Open Git Bash.
5. Change the current working directory to the one where you want the cloned directory.
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY).
7. Press Enter to create your local clone.

## Credits

### Media
- ASCII art: https://asciiart.website/index.php?art=transportation/nautical

### Code
- Code Institute Python lessons.
- Code Institute Love Sandwiches project.
- Knowledge Mavens https://www.youtube.com/watch?v=alJH_c9t4zw&t=673s
- Corey Schafer https://www.youtube.com/watch?v=6tNS--WetLI

## Acknowledgments
I would like to take the opportunity to thank:
- My mentor Mo Shami for his feedback, advice, guidance and support.
- My beautiful wife, Megan, for her continued love and support.
- Jim, Sawyer, and the other fantasic members of Code Institute's community team.
- The great people of class June '22 for their ideas and humour.



/////////////////////////////////////////////
* Bug 1, grid alignment (2/4/2023)
* Installed Math random (2/4/2023)
* Bug 2, border bug fix (3/4/2023)
* INstalled pip install colorama (3/4/2023)
