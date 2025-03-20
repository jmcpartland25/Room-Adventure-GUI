###########################################################################################
# Room Adventure
# Jamie McPartland
# 9/26/22
# brings you through a scary asylum and challenges you as you try to escape 
###########################################################################################
###Questions for office hours
#how to make thing update/change with item is grabbed
#how to say if in this room say this like when you win or lose
###########################################################################################
# import libraries
from tkinter import *
from functools import partial
###########################################################################################
# constants
VERBS = ["go", "look", "take"]  # the supported vocabulary verbs
QUIT_COMMANDS = ["exit", "quit", "bye"]  # the supported quit commands


###########################################################################################
# the blueprint for a room
class Room:
    # the constructor
    def __init__(self, name, image):
        # rooms have a name, image, description, exits (e.g., south), exit locations (e.g., to the
        # south is room n), items (e.g., table), item descriptions (for each item), and grabbables
        # (things that can be taken into inventory)
        self._name = name
        self._image = image
        self._description = ""
        self._exits = []
        self._exitLocations = []
        self._items = []
        self._itemDescriptions = []
        self._grabbables = []

    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc):
        # append the item and description to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)

    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item):
        # append the item to the list
        self._grabbables.append(item)

    # returns a string description of the room as follows:
    #  <name>
    #  <description>
    #  <items>
    #  <exits>
    # e.g.:
    #  Room 1
    #  You look around the room.
    #  You see: chair table 
    #  Exits: east south 
    def __str__(self):
        # first, the room name and description
        s = "{}\n".format(self._name)
        s += "{}\n".format(self._description)

        # next, the items in the room
        s += "You see: "
        for item in self._items:
            s += item + " "
        s += "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self._exits:
            s += exit + " "

        return s


###########################################################################################
# the blueprint for a Game
# inherits from the Frame class of Tkinter
class Game(Frame):
    # the constructor
    def __init__(self, parent):
        # call the constructor in the Frame superclass
        Frame.__init__(self, parent)

    # creates the rooms
    def createRooms(self):
        # a list of rooms will store all of the rooms
        # r1 through r4 are the four rooms in the "mansion"
        # currentRoom is the room the player is currently in (which can be one of r1 through r4)
        Game.rooms = []

        # first, create the room instances so that they can be referenced below
        r1 = Room("The White Room", "whiteroom.gif")
        r2 = Room("The Corridors", "corridors.gif")
        r3 = Room("Hospital Room 24A", "hospital.gif")
        r4 = Room("Prison", "jail.gif")
        r5 = Room("Control Room", "controlroom.gif")
        r6 = Room("The Sewers", "congrats.gif")

        #the white room
        r1.description = 'This room is terrifying... '
        r1.addExit("east", r2)
        r1.addItem("walls", "Where am I? Am I really in a isolation room... with not-hing else. I need to get out of here.")
        Game.rooms.append(r1)

        #the corridors
        r2.description = "Is this a hallway? How can even a hallway be terrifying?"
        r2.addExit("north", r3)
        r2.addExit("east", r4)
        r2.addGrabbable("battery")
        r2.addItem("bed", "It is destroyed.. and EW! What are those stains from?")
        r2.addItem("nametag", "This must have been Rosemary Burtons Room. What a creepy name... I sure hope she is gone.")
        r2.addItem("chair", "AHHHHH! Is that a body??? But wait... What is she holding? Is that a battery? I must need this.")
        Game.rooms.append(r2)

        #the hospital room
        r3.description = "UGH this room does not smell very good... Is that blood?"
        r3.addExit("west", r5)
        r3.addGrabbable("paper")
        r3.addGrabbable("scalpel")
        r3.addItem("bed", "Oh my gosh. Why did I need to find another body? Did they really just leave everyone here and completely abandon this place???")
        r3.addItem("paper", "The paper says, 'I was so close. 6 letters. mad. crazy. irrational. I CAN'T DO THIS ANYMORE!!!!' Oh No. I should take this I might need it.")
        r3.addItem("hole", "WOW, that is dangerous... definetly should stay away from that!")
        r3.addItem("scalpel","Bloody and SO gross, but protection and I DEFINETLY need that.")
    
        #the prison
        r4.description = "OH NO NO NO. I am in a prison cell!!"
        r4.addExit("west", r2)
        r4.addItem("toilet", "ewww someone forgot to flush!!!!!!!")
        r4.addItem("notebook", "It says 'theres only one way out... I was so close but I chose the wrong door.'")
        r4.addItem("bed","this is so dirty.")
    
        #control room
        r5.description = "YES! The control room... this has got to be my way out"
        r5.addExit("east", r6)
        r5.addExit("west", None)
        r5.addExit("north", None)
        r5.addExit("south", None)
        r5.addItem("doors", "This must be the exits... and these must be 'THE Doors' that the notebook was talking about. I could guess which door is right... but what if I am wrong?")
        r5.addItem("desk", "")

        # set room 1 as the current room at the beginning of the game
        Game.currentRoom = r1

        # initialize the player's inventory
        Game.inventory = []

        # sets up the GUI

    def setupGUI(self):
        # organize the GUI
        self.pack(fill=BOTH, expand=1)

        # setup the player input at the bottom of the GUI
        # the widget is a Tkinter Entry
        # set its background to white
        # bind the return key to the function process() in the class
        # bind the tab key to the function complete() in the class
        # push it to the bottom of the GUI and let it fill horizontally
        # give it focus so the player doesn't have to click on it
        Game.player_input = Entry(self, bg="grey")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.bind("<Tab>", self.complete)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()

        # setup the image to the left of the GUI
        # the widget is a Tkinter Label
        # don't let the image control the widget's size
        img = None
        Game.image = Label(self, width=WIDTH // 2, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)

        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width=WIDTH // 2, height=HEIGHT // 2)
        # the widget is a Tkinter Text
        # disable it by default
        # don't let the widget control the frame's size
        Game.text = Text(text_frame, bg="grey")
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=TOP, fill=Y)
        text_frame.pack_propagate(False)
        # Creating a canvas for the bottom half to easily navigate between rooms
        # Add north and south arrows as well in the code.
        # Feel free to use your own directional images.
        # North and South arrows are also provided to you as well.
        #Adding an arrow pointing to the east.
        canvas = Frame(self, width=WIDTH // 2, height=HEIGHT // 2)
        Game.eastimage = PhotoImage(file="east.png")
        Game.east = Button(canvas, image=Game.eastimage, command=partial(self.runCommand, "go east"))
        Game.east.pack(side=RIGHT)
        #Adding an arrow pointing to the west.
        Game.westimage = PhotoImage(file="west.png")
        Game.west = Button(canvas, image=Game.westimage, command=partial(self.runCommand, "go west"))
        Game.west.pack(side=LEFT)
        
        Game.northimage = PhotoImage(file="north.png")
        Game.north = Button(canvas, image=Game.northimage, command=partial(self.runCommand, "go north"))
        Game.north.pack(side=TOP)
        
        Game.southimage = PhotoImage(file="south.png")
        Game.south = Button(canvas, image=Game.southimage, command=partial(self.runCommand, "go south"))
        Game.south.pack(side=BOTTOM)

        canvas.pack(side=TOP, fill=Y)
        canvas.pack_propagate(False)

    # set the current room image on the left of the GUI
    def setRoomImage(self):
        if (Game.currentRoom == None):
            # if dead, set the skull image
            Game.img = PhotoImage(file="skull.jpg")
        else:
            # otherwise grab the image for the current room
            Game.img = PhotoImage(file=Game.currentRoom.image)

        # display the image on the left of the GUI
        Game.image.config(image=Game.img)
        Game.image.image = Game.img

    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        # enable the text widget, clear it, set it, and disable it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == None):
            # if dead, let the player know
            Game.text.insert(END, "Wrong exit..a ghost has possessed\nyou and you have lost the game!\nThanks For Playing!\nTo exit -> press the red x on the broswer.\n")
        else:
            # otherwise, display the appropriate status
            Game.text.insert(END, "{}\n\n{}\nYou are carrying: {}\n\n".format(status, Game.currentRoom, Game.inventory))
        Game.text.config(state=DISABLED)

        # support for tab completion
        # add the words to support
        if (Game.currentRoom != None):
            Game.words = VERBS + QUIT_COMMANDS + Game.inventory + Game.currentRoom.exits + Game.currentRoom.items + Game.currentRoom.grabbables



#############################################################################################################################
  
  
  # play the game
    def play(self):
        # create the room instances
        self.createRooms()
        # configure the GUI
        self.setupGUI()
        # set the current room
        self.setRoomImage()
        # set the initial status
        self.setStatus('Welcome to Outlast: Escape the Asylum...')
        

    # processes the player's input
    def process(self, event, action=""):
        self.runCommand()
        Game.player_input.delete(0, END)

    def runCommand(self, action=""):
        if not action.startswith("go"):
            # grab the player's input from the input at the bottom of the GUI
            action = Game.player_input.get()
            # set the user's input to lowercase to make it easier to compare the verb and noun to known values
            action = action.lower().strip()

        # exit the game if the player wants to leave (supports quit, exit, and bye)
        if (action in QUIT_COMMANDS):
            exit(0)

        # if the current room is None, then the player is dead
        # this only happens if the player goes south when in room 4
        if (Game.currentRoom == None):
            # clear the player's input
            Game.player_input.delete(0, END)
            return

        # set a default response
        response = "I don't understand. Try verb noun. Valid verbs\nare {}.".format(", ".join(VERBS))
        # split the user input into words (words are separated by spaces) and store the words in a list
        words = action.split()

        if (action == "look desk"):
            from puzzle import puzzle
            
        # the game only understands two word inputs
        if (len(words) == 2):
            # isolate the verb and noun
            verb = words[0].strip()
            noun = words[1].strip()

            # we need a valid verb
            if (verb in VERBS):
                # the verb is: go
                if (verb == "go"):
                    # set a default response
                    response = "You can't go in that direction."

                    # check if the noun is a valid exit
                    if (noun in Game.currentRoom.exits):
                        # get its index
                        i = Game.currentRoom.exits.index(noun)
                        # change the current room to the one that is associated with the specified exit
                        Game.currentRoom = Game.currentRoom.exitLocations[i]
                        # set the response (success)
                        response = "You walk {} and enter another room.".format(noun)
                # the verb is: look
                elif (verb == "look"):
                    # set a default response
                    response = "You don't see that item."

                    # check if the noun is a valid item
                    if (noun in Game.currentRoom.items):
                        # get its index
                        i = Game.currentRoom.items.index(noun)
                        # set the response to the item's description
                        response = Game.currentRoom.itemDescriptions[i]
                # the verb is: take
                elif (verb == "take"):
                    # set a default response
                    response = "You don't see that item."

                    # Check if the noun is a valid grabbable and is also not already in inventory
                    if (noun in Game.currentRoom.grabbables and noun not in Game.inventory):
                        # Get its index
                        i = Game.currentRoom.grabbables.index(noun)
                        # Add the grabbable item to the player's inventory
                        Game.inventory.append(Game.currentRoom.grabbables[i])
                        response = "You take {}.".format(noun)
        


        # display the response on the right of the GUI
        # display the room's image on the left of the GUI
        # clear the player's input
        self.setStatus(response)
        self.setRoomImage()

    # implements tab completion in the Entry widget
    def complete(self, event):
        # get user input and the last word of input
        words = Game.player_input.get().split()
        # continue only if there are words in the user's input
        if (len(words)):
            last_word = words[-1]
            # check if the last word of input is part of a valid verb/noun
            results = [x for x in Game.words if x.startswith(last_word)]

            # initially, there is no matching verb/noun
            match = None

            # is there only a single valid verb/noun?
            if (len(results) == 1):
                # the result is a match
                match = results[0]
            # are there multiple valid verbs/nouns?
            elif (len(results) > 1):
                # find the longest starting substring of all verbs/nouns
                for i in range(1, len(min(results, key=len)) + 1):
                    # get the current substring
                    match = results[0][:i]
                    # find all matches
                    matches = [x for x in results if x.startswith(match)]
                    # if there are less matches than verbs/nouns
                    if (len(matches) != len(results)):
                        # go back to the previous substring
                        match = match[:-1]
                        # stop checking
                        break
            # if a match exists, replace the user's input
            if (match):
                # clear user input
                Game.player_input.delete(0, END)
                # add all but the last (matched) verb/noun
                for word in words[:-1]:
                    Game.player_input.insert(END, "{} ".format(word))
                # add the match
                Game.player_input.insert(END, "{}{}".format(match, " " if (len(results) == 1) else ""))

        # prevents the tab key from highlighting the text in the Entry widget
        return "break"


###########################################################################################
# START THE GAME!!!
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()
