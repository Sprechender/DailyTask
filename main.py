import os
import platform
import questionary
import sys

# random fact: always when i define bools i first write "false" and then python annoys me with "False" and then i correct it
debug = False
debugStr = "[DEBUG] "

ignoreOS = False

# get running os
def get_os():
    system = platform.system()
    if system == "Windows":
        return "Windows"
    elif system == "Darwin":
        return "Mac"
    elif system == "Linux":
        return "Linux"
    else:
        return "Unknown"

def debugMode(enable):
    if enable == True:
        debug = True
        print(debugStr + "Set Debug Mode -> True")
    elif enable == False:
        debug = False

# clean the terminal
def clean():
    os.system('cls')

def languageSelect():
    print("gonna add sometime")
    print(debugStr + "Set language to English because no config was found.")

for arg in sys.argv:
        if arg == "debug":
            debugMode(True)
        elif arg == "ignore-os":
            ignoreOS = True

# if debug mode is on
if debug == True:
    if ignoreOS == True:
        print(debugStr + "Ignoring current OS\n   - please only activate this if you know what you are doing. \n  - Things are gonna break!")
    if ignoreOS == False:
        print(debugStr + "Running OS:", get_os())

def tasks():
    print("tasks")

def main():
    debugMode(True)
    welcomeMenu = questionary.select("Welcome to DailyTask!", choices=["Tasks", "Make a reservation", "Exit"]).ask()

    if welcomeMenu == "Tasks":
        tasks()

    if welcomeMenu == "2":
        print("2")

    if welcomeMenu == "Exit":
        exit()

currentOS = get_os()

if currentOS == "Windows" or currentOS == "Mac" or currentOS == "Linux":
    main()
elif currentOS == "Unknown":
    print("Your OS is not supported.\nIf you believe this is an Error check out the GitHub Issues Page.\nhttps://github.com/Sprechender/DailyTask/issues/")