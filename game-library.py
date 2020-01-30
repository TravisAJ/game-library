#!/usr/bin/python3
# Taffea Avenevoli
# 01/27/20

import pickle

'''Database for a Game Library'''

def addedit():
    #print("running addedit()...")
    keep_going3 = True
    while keep_going3:
        print("""
               ADD/EDIT MENU
        ---------------------------
                    Add
                   Edit
        ---------------------------
                   Quit
        """)        
        choice = input("Would you like to add/edit? ")
        
        if choice.lower() == "add":
            new_key = len(games) + 1
            new_entry = []
            valid = False
            while not valid:
                genre = input("What is the genre? ")
                new_entry.append(genre)
                
                title = input("What is the title? ")
                new_entry.append(title)
                
                develop = input("Who is the developer? ")
                new_entry.append(develop)
                
                publish = input("Who is the publisher? ")
                new_entry.append(publish)
                
                system = input("What system do you have it on? ")
                new_entry.append(system)
                
                release = input("What was the release date? ")
                new_entry.append(release)
                
                rating = input("What is your personal rating? ")
                new_entry.append(rating)
                
                mode = input("Is it singleplayer/multiplayer? ")
                new_entry.append(mode)
                
                price = input("What is the price? ")
                new_entry.append(price)
                
                completion = input("Have you beaten the game? ")
                new_entry.append(completion)
                
                purchase = input("When did you purchase the game? ")
                new_entry.append(purchase)
                
                print("----------------------")
                print("Genre: ", genre)
                print("Title: ", title)
                print("Developer: ", develop)
                print("Publisher: ", publish)
                print("System: ", system)
                print("Release Date: ", release)
                print("Rating: ", rating)
                print("Single/Multi?: ", mode)
                print("Price: ", price)
                print("Beat it?: ", completion)
                print("Purchase Date: ", purchase)                  
                print("----------------------")            
                answer = input("Is this Correct? [Y/n] ")
                if answer.lower() == "y":
                    valid = True
                elif answer.lower() == "n":
                    pass
                else:
                    print("\n*** NOT A VALID CHOICE ***") 
                games[new_key] = new_entry                                                                         
        elif choice.lower() == "edit":
            pass
        elif choice.lower() == "quit" or choice.lower() == "q":
            keep_going3 = False
        else:
            print("\n*** NOT A VALID CHOICE ***") 
            
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
        if search.lower() == "genre":
            found_one = False         
            genre = input("Insert Genre. ")
            for key in games.keys():
                if genre in games[key][0]:
                    found_one = True
                    print_it() == "Quit" or search == "quit"
            if not found_one:
                print("*** NO MATCHES FOUND!***\n")

        elif search.lower() == "title":
            found_one = False         
            title = input("Insert Title. ")
            for key in games.keys():
                if title in games[key][1]:
                    found_one = True
                    print_it()      
            if not found_one:
                print("*** NO MATCHES FOUND!***\n")
                
        elif search.lower() == "developer":
            found_one = False         
            develop = input("Insert Developer. ")
            for key in games.keys():
                if develop in games[key][2]:
                    found_one = True
                    print_it()
            if not found_one:
                print("*** NO MATCHES FOUND!***\n")
                    
        elif search.lower() == "publisher":
            found_one = False         
            publish = input("Insert Publisher. ")
            for key in games.keys():
                if publish in games[key][3]:
                    found_one = True
                    print_it()
            if not found_one:
                print("*** NO MATCHES FOUND!***\n")                
                    
        elif search.lower() == "system":
            found_one = False         
            system = input("Insert System. ")
            for key in games.keys():
                if system in games[key][4]:
                    found_one = True
                    print_it()
            if not found_one:
                print("*** NO MATCHES FOUND!***\n")                
                    
        elif search.lower() == "release date":
            found_one = False         
            release = input("Insert Release Date. ")
            for key in games.keys():
                if release in games[key][5]:
                    found_one = True
                    print_it()
            if not found_one:
                print("*** NO MATCHES FOUND!***\n")                
                    
        elif search.lower() == "rating":
            found_one = False         
            rating = input("Insert Rating. ")
            for key in games.keys():
                if rating in games[key][6]:
                    found_one = True
                    print_it()
            if not found_one:
                print("*** NO MATCHES FOUND!***\n")                
                    
        elif search.lower() == "gamemode":
            found_one = False         
            gamemode = input("Is it Singleplayer, Multiplayer, or Either? ")
            for key in games.keys():
                if gamemode in games[key][7]:
                    found_one = True
                    print_it()
            if not found_one:
                print("*** NO MATCHES FOUND!***\n")                    
                    
        elif search.lower() == "price":
            found_one = False         
            price = input("Insert Price. ")
            for key in games.keys():
                if price in games[key][8]:
                    found_one = True
                    print_it()
            if not found_one:
                print("*** NO MATCHES FOUND!***\n")                
                    
        elif search.lower() == "progress":
            found_one = False         
            progress = input("Have you beaten the game yet? ")
            for key in games.keys():
                if progress in games[key][9]:
                    found_one = True
                    print_it()
            if not found_one:
                print("*** NO MATCHES FOUND!***\n")                    
                    
        elif search.lower() == "purchase date":
            found_one = False         
            purchase = input("Insert Purchase Date. ")
            for key in games.keys():
                if purchase in games[key][10]:
                    found_one = True
                    print_it()
            if not found_one:
                print("*** NO MATCHES FOUND!***\n")                
                    
        elif search.lower() == "quit" or search.lower() == "q":
            keep_going2 = False
            
        else:
            print("\n*** NOT A VALID CHOICE ***")        
    
def remove():
    print("running remove()...") #not done yet
    
def save():
    #print("running save()...")
    datafile = open("game_lib.pickle", "wb")
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
    elif choice.lower() == "q":
        while quit:
            confirm = input("Are you sure you want to quit? (All unsaved progress will be lost) [Y/n] ")
            if confirm.lower() == "y":
                quit = False
                keep_going1 = False
            elif confirm.lower() == "n":
                quit = False
            else:
                print("Please input either 'Y' or 'n'.")        
    else:
        print("\n*** NOT A VALID CHOICE ***")
        
print("Goodbye!")