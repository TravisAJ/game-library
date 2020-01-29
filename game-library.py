#!/usr/bin/python3
# Taffea Avenevoli
# 01/27/20

import pickle

'''Database for a Game Library'''

def addedit():
    print("running addedit()...") #not done yet
    
def printall():
    #print("running printall()...")
    key_list = games.keys()
    
    for key in key_list:
        game = games[key]
        print()
        print("--------------------------------")
        print("Title: ", game[1])
        print("Developer: ", game[2])
        print("--------------------------------")    

def search():
    def print_it():
        print("----------------------")
        print("Genre: ", games[key][0])
        print("Title: ", games[key][1])
        print("Developer: ", games[key][2])
        print("Publisher: ", games[key][3])
        print("System: ", games[key][4])
        print("Release Date: ", games[key][5])
        print("Rating: ", games[key][6])
        print("Single/Multi?: ", games[key][7])
        print("Price: ", games[key][8])
        print("Beat it?: ", games[key][9])
        print("Purchase Date: ", games[key][10])                  
        print("----------------------")        
    #print("running search()...")
    keep_going2 = True
    while keep_going2:
        print("""
                SEARCH MENU
        ---------------------------
                   Genre
                   Title
                 Developer
                 Publisher
                  System
                Release Date
                  Rating
                 Gamemode
                   Price
                 Progress
               Purchase Date
        ---------------------------
                    Quit
        """)        
        search = input("What would you like to search for? ")
        if search == "Genre" or search == "genre":
            found_one = False         
            genre = input("Insert Genre. ")
            for key in games.keys():
                if genre in games[key][0]:
                    found_one = True
                    print_it()
            if not found_one:
                print("*** NO MATCHES FOUND!***\n")

        elif search == "Title" or search == "title":
            found_one = False         
            title = input("Insert Title. ")
            for key in games.keys():
                if title in games[key][1]:
                    found_one = True
                    print_it()      
            if not found_one:
                print("*** NO MATCHES FOUND!***\n")
                
        elif search == "Developer" or search == "developer":
            found_one = False         
            develop = input("Insert Developer. ")
            for key in games.keys():
                if develop in games[key][2]:
                    found_one = True
                    print_it()
            if not found_one:
                print("*** NO MATCHES FOUND!***\n")
                    
        elif search == "Publisher" or search == "publisher":
            found_one = False         
            publish = input("Insert Publisher. ")
            for key in games.keys():
                if publish in games[key][3]:
                    found_one = True
                    print_it()
            if not found_one:
                print("*** NO MATCHES FOUND!***\n")                
                    
        elif search == "System" or search == "system":
            found_one = False         
            system = input("Insert System. ")
            for key in games.keys():
                if system in games[key][4]:
                    found_one = True
                    print_it()
            if not found_one:
                print("*** NO MATCHES FOUND!***\n")                
                    
        elif search == "Release Date" or "release date":
            found_one = False         
            release = input("Insert Release Date. ")
            for key in games.keys():
                if release in games[key][5]:
                    found_one = True
                    print_it()
            if not found_one:
                print("*** NO MATCHES FOUND!***\n")                
                    
        elif search == "Rating" or search == "rating":
            found_one = False         
            rating = input("Insert Rating. ")
            for key in games.keys():
                if rating in games[key][6]:
                    found_one = True
                    print_it()
            if not found_one:
                print("*** NO MATCHES FOUND!***\n")                
                    
        elif search == "Gamemode" or search == "gamemode":
            found_one = False         
            gamemode = input("Is it Singleplayer, Multiplayer, or Either? ")
            for key in games.keys():
                if gamemode in games[key][7]:
                    found_one = True
                    print_it()
            if not found_one:
                print("*** NO MATCHES FOUND!***\n")                    
                    
        elif search == "Price" or search == "price":
            found_one = False         
            price = input("Insert Price. ")
            for key in games.keys():
                if price in games[key][8]:
                    found_one = True
                    print_it()
            if not found_one:
                print("*** NO MATCHES FOUND!***\n")                
                    
        elif search == "Progress" or search == "progress":
            found_one = False         
            progress = input("Have you beaten the game yet? ")
            for key in games.keys():
                if progress in games[key][9]:
                    found_one = True
                    print_it()
            if not found_one:
                print("*** NO MATCHES FOUND!***\n")                    
                    
        elif search == "Purchase Date" or "purchase date":
            found_one = False         
            purchase = input("Insert Purchase Date. ")
            for key in games.keys():
                if purchase in games[key][10]:
                    found_one = True
                    print_it()
            if not found_one:
                print("*** NO MATCHES FOUND!***\n")                
                    
        elif search == "Quit" or search == "quit":
            keep_going2 = False
            
        else:
            print("\n*** NOT A VALID CHOICE ***")        
    
def remove():
    print("running remove()...") #not done yet
    
def save():
    #print("running save()...")
    datafile = open("datafile.pickle", "wb")
    pickle.dump(games, datafile)
    datafile.close()
    print("\nFile Saved.")

games = {}
datafile = open("game_lib.pickle", "rb")
games = pickle.load(datafile)
datafile.close()

keep_going1 = True
quit = True

while keep_going1:
    print("""
    Welcome to the Game Library
    ---------------------------
    
    MAIN MENU\n
    1) Add/Edit Game
    2) Print All Games
    3) Search Menu
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
                keep_going1 = False
            elif confirm == "N" or confirm == "n":
                quit = False
            else:
                print("Please input either 'Y' or 'n'.")        
    else:
        print("\n*** NOT A VALID CHOICE ***")
        
print("Goodbye!")
    