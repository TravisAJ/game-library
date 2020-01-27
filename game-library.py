#!/usr/bin/python3
# Taffea Avenevoli
# 01/27/20

import pickle

'''Database for a Game Library'''

def addedit():
    print("running addedit()...")
    
def printall():
    print("running printall()...")

def search():
    print("running search()...")
    
def remove():
    print("running remove()...")
    
def save():
    print("running save()...")

keep_going = True
quit = True

while keep_going:
    print("""
    Welcome to the Game Library
    ---------------------------
    
    MAIN MENU
    1) Add/Edit Game
    2) Print All Games
    3) Search by Title
    4) Remove a game
    5) Save Database
    
    Q) Quit
    """)
    choice = input("What would you like to do? ")
    if choice == "1":
        addedit()
    elif choice == "2":
        printall()
    elif choice == "3":
        search()
    elif choice == "4":
        remove()
    elif choice == "5":
        save()
    elif choice == "Q" or choice == "q":
        while quit:
            confirm = input("Are you sure you want to quit? (All unsaved progress will be lost) [Y/n] ")
            if confirm == "Y" or confirm == "y":
                quit = False
                keep_going = False
            elif confirm == "N" or confirm == "n":
                quit = False
            else:
                print("Please input either 'Y' or 'n'.")        
    else:
        print("*** NOT A VALID CHOICE ***\n")
        
print("Goodbye!")
    