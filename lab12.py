#Lab 11
#Team 10 - M. Mariscal, C. Piwarski, W. Robleh

# One object of Class Room represents a room in the game map
class Room:

    # Constructor method for class Room
    def __init__(self, name='', desc='', north=None, south=None, \
        west=None, east=None):
        self.name = name
        self.desc = desc
        self.items = []

        # set exits
        self.north = north
        self.south = south
        self.west = west
        self.east = east

    # This method returns the name of the room
    def getName(self):
        return self.name

    # This method returns the description of the room
    def getDesc(self):
        return self.desc
    
    # This method adds items to the room
    def printItems(self):
      for item in self.items:
        printNow('You see a %s' % item.getName())
        
    def getItems(self):
      return self.items

    # This method removes an item from the room
    def removeItem(self, item):
        self.items.remove(item)
      
    # This method adds an item to the room
    def addItem(self, item):
      self.items.append(item)
      
    def printExits(self):
      return_string = ''
      if self.north is not None:
        return_string += 'There is an exit to the north.\n'
      if self.south is not None:
        return_string += 'There is an exit to the south.\n'
      if self.east is not None:
        return_string += 'There is an exit to the east.\n'
      if self.west is not None:
        return_string += 'There is an exit to the west.\n'
      return return_string

    # This method returns the exit to the room based on the given direction
    def getExit(self, direction):
        if direction == 'n':
            return self.north
        elif direction == 's':
            return self.south
        elif direction == 'e':
            return self.east
        elif direction == 'w':
            return self.west
        else:
            return None

    # String method for class Room
    def __string__(self):
        return name + ' ' + desc + ' ' + exits

    # This method sets the name of the room
    def setName(self, name):
        self.name = name

    # This method sets the description of the room
    def setDesc(self, desc):
        self.desc = desc

    # This method sets the north exit for the room
    def setNorth(self, room):
        self.north = room

    # This method sets the south exit for the room
    def setSouth(self, room):
        self.south = room

    # This method sets the east exit for the room
    def setEast(self, room):
        self.east = room

    # This method sets the west exit for the room
    def setWest(self, room):
        self.west = room
        
# One object of Class Items represents an item in the game
class Items:
  
  #constructor
  def __init__(self, name='', desc='', loc=''):
    self.name = name
    self.desc = desc
    self.loc = loc
    
  # This method returns the name of the item
  def getName(self):
    return self.name
  
  # This method returns the description of the item
  def getDesc(self):
    return self.desc
  
  #This meth returns the location of the item
  def getLoc(self):
    return self.loc
    
  #This sets the name for this item
  def setName(self, name):
    self.name = name
    
  #This sets the description for this item
  def setDesc(self, desc):
    self.desc = desc
    
  #This sets the location for this item
  def setLoc(self):
    self.loc = loc

  
# Class Player represents the player character
class Player:

    # Constructor method for Class Player
    def __init__(self, inventory=[]):
        self.inventory = inventory
        self.location = None

    # This method returns the contents of the player's inventory
    def getInventory(self):
        return self.inventory

    # This method sets the location of the player
    def setLocation(self, location):
        self.location = location

    # This method returns the room that the player is currently in
    def getLocation(self):
        return self.location
      
    def addInventory(self, itemToAdd):
      self.inventory.append(itemToAdd)

    def printInventory(self):
        printNow('This is your inventory')
        for item in self.inventory: 
          printNow(item.getName())
          
# Main function for the game
def Main():

    # Create Map 
    descCell = 'A cold, lonely prison cell, your home for the last 15 years for a crime you did not do!'
    descHall = 'The hallway of a prison. All your prisonmates are sound asleep. If you are loud, they will wake up and your cover will be blown.'
    descKitchen = 'The kitchen for the prison. Where the food is disgusting.'
    descCloset = 'Closet in the Kitchen. It smells like somethind died in here. You are in the wrong location!'
    twoHall = 'Another hallway, the prison cat is sound asleep.'
    
    threeHall = 'Entering a third hallway. This place seemingly goes on forever.'
    twoCell = 'Entering another Cell. Your old prisonmate who assaulted you is reading a book. He waves as you walk through the cell.'
    
    guardRoom = 'You enter and see about three guards. What should you do now?'
    endDescription = 'This is the exit. You\'re happy to make it out Alive!'
    
    room1 = Room('Your cell', descCell)
    room2 = Room('Hall', descHall)
    room3 = Room('Kitchen', descKitchen)
    room4 = Room('Closet', descCloset)
    room5 = Room('2nd Hall', twoHall)
    room6 = Room('2nd Cell', twoCell)
    room7 = Room('3rd Hall', threeHall)
    room8 = Room('Guard Room', guardRoom )
    room9 = Room('Exit', endDescription)
    
    
    # Connect Rooms
    room1.setNorth(room2)
    room2.setSouth(room1)
    room2.setEast(room3)
    room3.setWest(room2)
    room3.setNorth(room4)
    room4.setSouth(room3)
    
    room3.setEast(room5)
    room5.setWest(room3)
    room5.setSouth(room6)#entering second cell
    room6.setNorth(room5) #would like this to be a gameOver later on - Wais
    room5.setEast(room7)#entering third hallway
    room7.setWest(room5)
    
    room7.setNorth(room8)
    room7.setEast(room9)
    
    # Item Descriptions
    keyDescription = 'Use this key to get out of the prison gate.'
    catDescription = 'Pet the cat to make sure the cat does not wake up.'
    locpickDescription ='Use this picklock to unlock a secret '
    
    # Create Items
    key = Items('key',keyDescription,room4)
    cat = Items('cat',catDescription,room5)
    lockpick = Items('lockpick', locpickDescription, room6)
    
    # Add items
    room4.addItem(key)
    room5.addItem(cat)
    room6.addItem(lockpick)

    # Create Player
    player1 = Player()
    player1.setLocation(room1)

    # Define Extra Variables
    commands = ['examine', 'n', 's', 'e', 'w', 'get', 'use', 'exit', 'help', 'print']
    directions = ['n', 's', 'e', 'w']
    gameWon = False
    welcomeMessage = 'Welcome to Jailbreak\n You are a prisoner who is looking to escape from one of the most dangerous prisons in the world.\n 
    helpMessage = 'Type exit to quit your game.\n''To move your player type n,s,e,and w.\n''Type get to pick up objects\n''Type in examine to look at your surroundings.\n' 
    
    # print welcome message
    printNow(welcomeMessage)
    printNow(helpMessage)
    
    # Main game loop
    while gameWon != True:
        printNow(player1.getLocation().getName())
        printNow(player1.getLocation().getDesc())
        printNow(player1.getLocation().printExits())
        player1.getLocation().printItems()
        
        # input loop. Keep asking for input until a valid command is received
        inputValidation = False
        while inputValidation == False:
            input = requestString('What would you like to do?')
            if input in commands:
              inputValidation = True
            else:
              printNow('Invalid Command. Try Again')

        # handle a request to exit
        if input == 'exit':
          printNow('Quitting game. Have a nice day.')
          break
        
        # handle a request for help
        if input == 'help':
            printNow(helpMessage) 

        # handle request to print inventory
        if input == 'print':
            player1.printInventory()
        
        # handle an examine request
        if input == 'examine':
          whatToExamine = requestString('What would you like to examine? room or items?')
          if whatToExamine == 'room':
            printNow(player1.getLocation.getDesc())
          elif whatToExamine == 'items':
            for item in player1.getInventory():
              printNow('%d. %s' % (item, item.getName()))
            itemToExamine = requestString('Which item to examine?')
            printNow(itemToExamine.getDesc())
            
        if input == 'get':
          getWhat = requestString('Get what?')
          roomItems = player1.getLocation().getItems()
          for item in roomItems:
            if item.getName() == getWhat:
                foundItem = item
                player1.addInventory(item)
                player1.getLocation().removeItem(item)
                printNow('Took item')
        
        
        # handle movement requests
        if input in directions:
          nextRoom = player1.getLocation().getExit(input)
          if nextRoom is not None:
            player1.setLocation(player1.getLocation().getExit(input))
          else:
            printNow('There is no exit in that direction')
        
        #######If there is a better way of doing this let me know ######
        # game over conditions
        if player1.getLocation() == room9:
          gameWon = True
          print 'Congratulations, you escaped!'
        
       ##want to check if player is in guard room and tries to leave he will be caught and game ends.
        if player1.getLocation() == room8 and input:
          gameWon = True
          print 'You entered the Guard\'s Room. You got caught!!!'
          

          


