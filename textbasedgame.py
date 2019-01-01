import os
import time

path = "C:\\Users\\Owner\\Desktop\\name.txt"

print("welcome to TBRPG")

exist_check = open(path, "a")
exist_check.close()

def stats():
    level = 1
    defence = 10
    speed = 10
    damage = 10
    accuracy = 8
    health = 10
    print("╔══════════════════════╗")
    print("║      STAT            ║")
    print("║Level",level,"              ║")
    print("║                      ║")
    print("║defence",defence,"           ║")
    print("║                      ║")
    print("║speed",speed,"             ║")
    print("║                      ║")
    print("║damage",damage,"            ║")
    print("║                      ║")
    print("║Accuracy",accuracy,"           ║")
    print("║                      ║")
    print("║Health",health,"            ║")
    print("╚══════════════════════╝")
    gameMenu()


#fight menu
def fightmenu():
    print("╔══════════════════════╦═════════════════════╗")
    print("║                      ║                     ║")
    print("║                      ║                     ║")
    print("╠══════════════════════╬═════════════════════╣")                                           
    print("║                      ║                     ║")
    print("║                      ║                     ║")
    print("╚══════════════════════╩═════════════════════╝")



#fighting menu 14
def fight():
    GoblinHP = 10
    print("╔══════════════════════╗")
    print("║        ENEMYS        ║")
    print("║Goblin - 10HP         ║")
    print("║                      ║")
    print("║                      ║")
    print("║                      ║")
    print("║                      ║")
    print("║                      ║")
    print("║                      ║")
    print("║                      ║")
    print("║                      ║")
    print("║                      ║")
    print("║                      ║")
    print("╚══════════════════════╝")
    whotofight = input("Who would you like to fight?")
    if whotofight == "Goblin":
        fightmenu()


def gameMenu():
    menu = input("What would you like to do? (type HELP to see available commands)")

    help_commands = ["stats", "help", "fight"]
    
    if menu == "help":
        print("You can use the following commands: ")
        print( *help_commands, sep = ", ")
        gameMenu()
    if menu == "stats":
        stats()
    if menu == "fight":
        fight()


def newUser():
    print("Hello, we did not see that you have any profile saved onto this computer")
    name = input("So, what would you like your name to be")
    time.sleep(2) #delay for 3 seconds
    name_confirm = input("(Y/N) would you like your name to be  " +name)

    if name_confirm == "Y":
        name_save = open(path, "w")
        name_save.write(name)
        name_save.close()
        print("Your profile name has been saved!")
def welcomeBack():
    name_open = open(path, "r")
    name_for_welcome = name_open.read()
    name_open.close()
    print("Welcome back, ", name_for_welcome)
    gameMenu()


if os.stat(path).st_size == 0:
    newUser()
else:
    welcomeBack()
