import os
import time
import sys

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
    EnemyName = "Goblin" 
    EnemyHP = 10
    PlayerHP = 15
    print("╔══════════════════════╦═════════════════════╗")
    print("║        TACKLE        ║        BLOCK        ║")
    print("║                      ║                     ║")
    print("╠══════════════════════╬═════════════════════╣")                                           
    print("║         QUIT         ║                     ║")
    print("║                      ║                     ║")
    print("╚══════════════════════╩═════════════════════╝")
    action = input("Which action would you like to preform? ")

    if action == "tackle":
        print("You hit for 2 damage")
        EnemyHP = EnemyHP - 2
        print("The", EnemyName, "has ")
        print(EnemyHP, "HP")
        time.sleep(0.5)
        print("you were hit for 2 HP")
        PlayerHP = PlayerHP - 2
        print("You have ", PlayerHP, "HP left")
    elif action == "TACKLE":
        print("You hit for 2 damage")
        EnemyHP = EnemyHP - 2
        print("The", EnemyName, "has ")
        print(EnemyHP, "HP")
    if action == "quit":
        gameMenu()
    elif action == "QUIT":
        gameMenu()
        
    else:
        fightmenu()


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
    else:
        fight()


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
    if menu == "quit":
        sys.exit(0)


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
