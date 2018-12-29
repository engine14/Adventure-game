class Location:
    '''Class to represent each location in game world.'''
    
    def __init__(self, items, short_description, long_description, visited):
        '''Creates a new location.          
        
        Data that should be associated with each Location object:
        an integer location ID,
        a brief description,
        a long description,
        items that are available in the location,
        and whether or not the location has been visited before.
        '''

        self.items = []
        self.location_id = location_id
        self.short_description = short_description
        self.long_description = long_description
        self.visited = False 
        
    def get_short_description (self):
        '''
        (Location) -> str
        Return str brief description of location, like so,
        
        You are inside the communication, culture, and technology building (CCT).
        '''
        
        self.visited = True
        if self.visited:
            return get_short_description       

    def get_long_description (self):
        '''
        (Location) -> str
        Return str long description of location, like so,

        You are inside the communication, culture, and technology building (CCT).
        There you see a study space to your left, which you usally sit at,
        and there you see your lucky pen sitting there waiting for you.
        Go and quickly type "pick up" to pick up your lucky pen to add to your inventory.
        '''
    
        if self.visited:
            return get_long_description
        
# --- END of Location class --- #

class Item:
    '''Class to represent each item in game world.'''
    
    def __init__ (self, name, start, target, target_points):
        '''Create item referred to by string name, with integer "start"
        being the integer identifying the item's starting location,
        the integer "target" being the item's target location, and
        integer target_points being the number of points player gets
        if item is deposited in target location.
        '''
        
        self.name = name
        self.start = start
        self.target = target
        self.target_points = target_points

    def get_starting_location (self):
        '''
        (Item) -> int
        Return location (the integer id) of where item is first found, like so,

        >>> Item.get_starting_location()
        4
        '''

        for item in self.items:
            if self.name == ("Lucky pen"):
                return int ('4')
            elif self.name == ("T-Card"):
                return int('15')
            elif self.name == ("Cheat Sheet"):
                return int ('30')

    def get_name(self):
        '''
        (Item) -> str
        Return the str name of the item.

        >>> Item.get_name()
        'Lucky pen'
        '''
        
        return (self.name)

    def get_target_location (self):
        '''
        (Item) -> int
        Return item's target location (the integer id) of where it should be deposited.
        
        >>> Item.get_target_location ()
        30
        '''

        if target in WORLD.get_room():
            return int ('30')

    def get_target_points (self):
        '''
        (Item) -> int
        Return integer points awarded for depositing the item in its target location.

        >>> Item.get_target_points()
        20
        '''

        get_target_location()
        target_points = target_points + 20
        return target_points

# --- END of Item class --- #

class Player:
    '''Class to represent the player in game world.'''

    def __init__(self, x, y):
        '''
        (Player, int, int) -> None
        Creates a new Player at given x and y coordinates.
        '''
       
        self.x = x
        self.y = y
        self.victory = False # set to True once player has won game
        self.inventory = [] # store list of item names that are in player's inventory

    def move(self, dx, dy):
        '''
        (Player, int, int) -> None
        Given integers dx and dy, move player to new location
        '''

        self.x = self.x + dx
        self.y = self.y + dy

    def move_north(self):
        '''
        (Player) -> None
        Helper function to move Player one position north on map.
        These integer directions are based on how the map must be stored
        in our nested list self.map.
        '''
        self.move(-1,0)

    def move_south(self):
        '''
        (Player) -> None
        Helper function to move Player one position south on map.
        These integer directions are based on how the map must be stored
        in our nested list self.map.
        '''
        self.move(1,0)

    def move_east(self):
        '''
        (Player) -> None
        Helper function to move Player one position east on map.
        These integer directions are based on how the map must be stored
        in our nested list self.map.
        '''
        self.move(0,1)

    def move_west(self):
        '''
        (Player) -> None
        Helper function to move Player one position west on map.
        These integer directions are based on how the map must be stored
        in our nested list self.map.
        '''
        self.move(0,-1)
       
    def add_item(self, item):
        '''
        (Player, str item name) -> None
        Add given item name to player's inventory.
        '''
        
        if item not in self.inventory:
            self.inventory.append(item)

    def remove_item(self, item):
        '''
        (Player, str item name) -> None
        Remove given item name from player's inventory.
        '''

        if item in self.inventory:
            self.inventory.remove(item)

    def get_inventory(self):
        '''
        (Player) -> lst
        Return player's inventory.
        '''
        
        return self.inventory
    
# --- END of Player class --- #

class Keys:
    '''Class to represent the keys in game world.'''

    def __init__(self, green_key, orange_key, white_key):
        '''
        (Keys) -> None
        Creates three coloured keys: green, orange, and white.
        '''
        
        self.green_key = green_key
        self.orange_key = orange_key
        self.white_key = white_key

    def intro_key (self):
        '''
        (Keys) -> None
        Displays the introduction to finding the correct key.
        '''
        
        print ('Oh great just when you thought your day could not get any worst. In the early')
        print ('morning you find out that University of Toronto Mississauga (UofT) is locked!')
        print ('The janitor is nice enough to lend you the keys but is not sure about which')
        print ('key opens the door. There are three coloured keys: green key, orange key, and')
        print ('white key in front of you and you must choose the correct key to enter the UofT')
        print ('campus.\n')
        print ('CAUTION: Please be specific for example: "insert green key" or "insert orange')
        print ('key" or "insert white key."\n')
        
    def find_key(self):
        '''
        (Key) -> None
        The user must choose the correct key to enter the UofT campus.

        >>> Please choose the correct coloured key to open the doors of UofT: insert green key
        Sorry, wrong key, that key does not open the doors of UofT
        >>> Please choose the correct coloured key to open the doors of UofT: insert orange key
        Yes, that is the correct key! You have entered the UofT campus!
        '''   
         
        while True:
            
            enter = input ('Please choose the correct coloured key to open the doors of UofT: ')

            if (enter == 'insert green key') or (enter == 'insert white key'):
                print ('Sorry, wrong key, that key does not open the doors of UofT\n')

            elif (enter == 'insert orange key'):
                print ('Yes, that is the correct key! You have entered the UofT campus!')
                break

            else:
                print ('ERROR! Please enter "insert green key" or "insert orange key" or')
                print ('"insert white key"\n')

# --- END of Keys class --- #

