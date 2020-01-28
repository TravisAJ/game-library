import pickle

games = {1:['Rhythm', 'Beat Saber', 'Beat Games', 'Oculus', 'Virtual Reality', 
            '2018', '10', 'Single', '30.00', 'No', '12/25/19', 'My favorite VR Game!'], 
         2:['Action', 'Just Shapes and Beats', 'Berzerk Studio', 'Steam', 'Windows',
            '2018', '9', 'Either', '20.00', 'Yes', '7/31/19', 'Great Music!'], 
         3:['MOBA', 'Brawl Stars', 'Supercell', 'Supercell', 'Android',
            '2017', '8.5', 'Multiplayer', 'Free', '12/12/18', 'The best mobile game!']
         }

datafile = open("game_lib.pickle", "wb")
pickle.dump(games, datafile)
datafile.close()
print("Data Reseted. Go Back to the Game Library.")