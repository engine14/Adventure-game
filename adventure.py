import sys
from game_data import Player, Location, Item, Keys
import winsound #used to play music
import os 

class World:
    """A class used to store all map, location and item data for game world."""

    def __init__(self, mapfile, locfile, itemfile):
        """
        (World, str filename, str filename, str filename) -> None
        
        Initialize a World using data from the given filenames.
        """
        
        self.map = []
        self.locations = {}
        self.location = []
        self.items = {}

        self.load_map(mapfile)
        self.load_locations(locfile)
        self.load_items(itemfile)

    def load_map(self, filename):
        '''
        (World, str filename) -> None
        Store map from filename in self.map as a nested list
        of strings like so:
            1 2 5
            3 -1 4
        becomes [['1','2','5'], ['3','-1','4']]
        '''
        
        mapfile = open ('map.txt', 'r')
        
        for number in mapfile:
            number = number.strip().split(' ') #removes the white spaces and makes a list
            self.map.append(number)
            
        mapfile.close()
       
    
    def load_locations(self, filename):
        '''
        (World, str filename) -> None
        Store all locations from filename in self.locations
        as a dictionary where integer location numbers are the keys,
        and Location objects are the values:
        {integer location number: Location object}.

        {3:[None, 'You are at the front of the UofT campus.', 'You are on outer circle road', True]}
        '''
        
        locfile = open('locations.txt', 'r')

        for line in locfile:
            newlocation = line.split('\n')[0].split('*') 
            self.location.append(newlocation)
        locfile.close()
        location_id = line.strip()
        
        while line.isnumeric():
            location_id = int(location_id)
            line = locfile.readline().strip() #short description
            line2 = locfile.readline().strip() #long description
            locations[location_id] = Location (items, line, line2, True)
            
        locfile.close()
       
    def load_items(self, filename):
        '''
        (World, str filename) -> None
        Store all items from filename in self.items
        with item name as the key, and an Item object as the value.
        Each item should also be added into self.locations as
        based on the item's starting location as given in text file.
        
        {'T-card': ['15'], 'Cheat-sheet': ['30'], 'Lucky-pen': ['4']}
        '''

        itemfile = open ('items.txt','r')
   
        for line in itemfile:
            line = itemfile.read().split()
            
            tcard = line[0] #key for the t-card
            self.items[tcard] = line[1:2] #value for the t-card
            self.locations.items()
            
            lucky_pen = line[2]
            self.items[lucky_pen] = line[3:4]
            self.locations.items()

            cheat_sheet = line[4]
            self.items[cheat_sheet] = line[5:]
            self.locations.items()
            
        itemfile.close() 
            
            
    def get_room(self, x, y):
        '''
        (World, int, int) -> Location
        Return the Location object associated with x, y values given, like so:

        'You are at the front of the UofT campus. You are on outer circle road.'
        '''
        loc_on_map = self.map[x][y]
        
        if loc_on_map != '-1':
            for destination in self.location:
                if destination[0] == loc_on_map:
                    return destination[1] #description

# --- END of World class --- #


if __name__ == "__main__":

    WORLD = World("map.txt", "locations.txt", "items.txt") # variables to store world info and player info
    PLAYER = Player(0, 0) # starting location of player
    KEYS = Keys('green key','orange key', 'white key') #enhancement, variable to stores key info

    menu = ["look", "inventory", "score", "quit","pick up", "where am i?"]

    moves = 20
    score = 0

    print ('On the day of your CSC108 exam you realize that you have lost all')
    print ('three important items that you will need to write you exam. So you must')
    print ('complete your journey around University of Toronto (UofT)')
    print ('to find your lucky pen, T-card, and cheat sheet. Careful you only have one')
    print ('hour left before the exam starts. Hurry and good luck!')
    print ('You only have 20 moves to get to the exam room. For each move you make')
    print ('you get 2 points. For each item you collect you get additional 20 points.')
    print ('Here is some upbeat music to help you out. You will be automatically')
    print ('prompted with the next steps when the song is finished.\n')
    print ('A map of UofT will soon appear. Use it to navigate your player.\n')

    UofT
    
    winsound.PlaySound('music.wav', winsound.SND_ALIAS)# enhancement, plays music from wav file
    
    KEYS.intro_key() # decribes the find the correct key scenario 
    KEYS.find_key() # user must choose the correct coloured key
    
    while not PLAYER.victory:

        current_loc_room = WORLD.get_room(PLAYER.x, PLAYER.y)# location on map
        current_loc = WORLD.map[PLAYER.x][PLAYER.y] # interger associated with the location on map
        current_loc_north = WORLD.map[PLAYER.x - 1][PLAYER.y] # location when the player moves north
        current_loc_south = WORLD.map[PLAYER.x + 1][PLAYER.y] # location when the player moves south
        current_loc_east = WORLD.map[PLAYER.x][PLAYER.y + 1] # location when the player moves east
        current_loc_west = WORLD.map[PLAYER.x][PLAYER.y -1] # location when the player moves west

        
        print ('\n')
        print("Commands you can enter: \n")
        print ('-> go north')
        print ('-> go south')
        print ('-> go east')
        print ('-> go west\n')
        print ('Menu option:\n')

        for options in menu:
            print (options)

        choice = input("\nEnter action: ")
        
        if (choice == 'look'):
            print (current_loc_room)

        if (choice == 'inventory'):
            print(PLAYER.get_inventory())

        if (choice == 'score'):
            print('Your score right now is {0}.'.format(score))

        if (choice == 'quit'):
            print ('You have decided to quit the game.')
            
            while True:
                answer = input ('Do you want to save your game? Type "yes" or "no" ')
                
                if answer == 'yes':
                    
                    backup = open ('backup.py','w')

                    for line in open ('backup.py'):  # reads the old file
                        backup.write(line) # writes in a new backup file
                        
                    backup.close()
                    
                    print ('Please follow these instructions: ')
                    print ('In the Python Shell, press Ctrl+S and replace backup.py in the adventure file.')
                    break
                
                elif answer == 'no':
                    print ('You will do your exam during the deferred exam peroid.')
                    break
            break
        
        if (choice == 'where am i?'):
            print ('You are at location {0} on the map.'.format(current_loc))
            
        # item pickups
        if choice == 'pick up' and current_loc == '4':
            PLAYER.add_item("Lucky pen")
            score = score + 20
            print ("YES! You found your lucky pen!")

        elif choice == 'pick up' and current_loc == '15':
            PLAYER.add_item('T-card')
            score = score + 20
            print ("Finally, you found your T-Card!")

        elif choice == 'pick up' and current_loc == '30':
            PLAYER.add_item ('Cheat sheet')
            score = score + 20
            print ('GOOD JOB! You found your cheat sheet!')

        elif (choice == 'pick up') and(current_loc != '4' or current_loc != '15' or current_loc != '30'):
            print ('There is no item to pick up at this location!')
            
        # player movement    
        if (choice == 'go north' and current_loc_north != '-1'):
            PLAYER.move_north()
            score = score + 2
            print(WORLD.get_room(PLAYER.x,PLAYER.y))
            moves = moves - 1
            print ('You have {0} moves left.'.format(moves))
            
        elif (choice == 'go north' and current_loc_north == '-1'):
            print ("Sorry, that way is BLOCKED!")

        if (choice == 'go south' and current_loc_south != '-1'):
            PLAYER.move_south()
            score = score + 2
            print(WORLD.get_room(PLAYER.x ,PLAYER.y))
            moves = moves - 1
            print ("You have {0} moves left.".format(moves))
            
        elif (choice == 'go south' and current_loc_south == '-1'):
            print('Sorry, that way is BLOCKED!')

        if (choice == 'go east' and  current_loc_east != '-1'):
            PLAYER.move_east()
            score = score + 2
            print(WORLD.get_room(PLAYER.x,PLAYER.y))
            moves = moves - 1
            print ('You have {0} moves left.'.format(moves))
            
        elif (choice == 'go east' and current_loc_east == '-1'):
            print('Sorry, that way is BLOCKED!')

        if (choice == 'go west' and current_loc_west != '-1'):
            PLAYER.move_west()
            score = score + 2
            print(WORLD.get_room(PLAYER.x,PLAYER.y))
            moves = moves - 1
            print ("You have {0} moves left.".format(moves))
            
        elif (choice == 'go west' and current_loc_west == '-1'):
            print("Sorry, that way is BLOCKED!")

        # winning condition
        if PLAYER.get_inventory()== ['Lucky pen', 'T-card', 'Cheat sheet']:
            print("YES! You have collected all of your items before your exam starts!")
            print("You finished the game with {0} points!".format (score))
            break
        
        # losing condition
        if moves == 0:
            print ("Sorry, time is up! You did not get all of your items before the exam started. GAME OVER.")
            break

        
