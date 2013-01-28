inv = []
def nl():
    print "~~~~~~~~~~~~~~~~~~~~~~"
def R1():
    print """You are, astonishingly, in a room. It is dark, and the floor is on a noticable slope. There is a door on each wall. Which door do you take?
    1) The door in front of you (uphill)
    2) The door to your left
    3) The door behind you (downhill)
    4) The door to your right"""
    answer = raw_input(">")
    if answer == "1":
        nl()
        corridor("r1")
    elif answer == "2":
        nl()
        #ballroom("r1")
        print "Unavailable"
        R1()
    elif answer == "3":
        nl()
        print "Unavailable"
        R1()
        #hydroponics()
    elif answer == "4":
        nl()
        #stairway()
        print "Unavailable"
        R1()
    else:
        nl()
        print "Command not recognised. Please type a number between 1 and 4"
        R1()

def corridor(origin):
    if origin == "r1":
        print "You are in a long, narrow, sloping corridor, furnished with a threadbare carpet and poorly painted portraits of cheap garden furniture. Ahead of you, uphill, is a heavy oak door. To your right is what appears to be a cupboard. Behind you, downhill, is the door you just walked through. Which door do you take?"
    if origin == "reception":
        print "You are in a long, narrow, sloping corridor, furnished with a threadbare carpet and poorly painted portraits of cheap garden furniture. Ahead of you, downhill, is a plain white door. To your left is what appears to be a cupboard. Behind you, uphill, is the door you just walked through. Which door do you take?"
    if origin == "wardrobe":
        print "You are in a long, narrow, sloping corridor, furnished with a threadbare carpet and poorly painted portraits of cheap garden furniture. To your left, downhill, is a plain white door. Behind you is the wardrobe you just walked out of. To your right, uphill, is a heavy oak door. Which door do you take?"
    print """
    1) The uphill door
    2) The downhill door
    3) The side door"""
    answer = raw_input(">")
    if answer == "1":
        nl()
        reception("corridor")
    elif answer == "2":
        nl()
        R1()
    elif answer == "3":
        nl()
        wardrobe()
    else:
        nl()
        print "Command not recognised. Please type a number between 1 and 4"
        corridor(r1)
            
def wardrobe():
    print "The 'cupboard' turns out to be an unfeasibly large walk-in wardrobe, replete with bizarre costumes. You explore it for a while, encountering a small, pungent dog, an unexpected goldfish pond, and Tom Baker, who asks you whether you are looking for anything in particular. You aren't, so you apologise for disturbing him and leave."
    nl()
    corridor("wardrobe")
    
def reception(origin):
    global inv
    if origin == "corridor":
        print "You walk into a tastelessly furnished office. Behind a formica desk, a receptionist is studiously ignoring you, while reading a magazine which, on closer inspection, turns out to be blank. It is unseasonably cold. There is a door behind the desk, with an illegible brass plate on it, and another to your left, which has been wallpapered over and lacks a handle. Behind you is the heavy oak door you just came through. You clear your throat, attempting to get the attention of the receptionist, to no avail."
    elif origin == "meatlocker":
        print "You dash through the door just before it slams shut. Behind a formica desk, a receptionist tells you to wipe your feet, then goes back to studiously ignoring you, while reading a magazine which, on closer inspection, turns out to be blank. It is unseasonably cold. There is a door behind the desk, with an illegible brass plate on it, and heavy oak door to your right. Behind you is the wallpapered door you which you just came through. You clear your throat, attempting to get the attention of the receptionist, to no avail."
    elif origin == "office": 
        print "You burst back into the reception room with your heart pounding. Behind a formica desk, a receptionist rings a bell on her desk, then goes back to studiously ignoring you, while reading a magazine which, on closer inspection, turns out to be blank. It is unseasonably cold. There is heavy oak a door ahead of you, and another to your right, which has been wallpapered over and lacks a handle. Behind you is the door you which you just came through, with the brass plate. You clear your throat, attempting to get the attention of the receptionist, to no avail."
    elif origin == "conversation": 
        print "You are standing in front of a formica desk, behind which the receptionist is studiously ignoring you once again. It is unseasonably cold. There is a door ahead of you, which bears an illegible brass plate, another to your left, which has been wallpapered over and lacks a handle, and a third one behind you, which is heavy and made of oak. You clear your throat, attempting to get the attention of the receptionist, to no avail."
    if "typewriter" in inv:
        print "The smashed remains of a typewriter litter the floor."
    print """
    What do you do?
    1) Go through the door with the brass plate
    2) Go through the wallpapered door
    3) Go through the heavy oak door
    4) Knock the receptionist's typewriter off the desk"""
    answer = raw_input(">")
    if answer == "1":
        if "appointmentcard" in inv:
            nl()
            office()
        else: 
            print "The receptionist jumps out of her seat, bars your way, and demands to see your appointment card. Try as you might, you can't get past her."
            nl()
            reception(origin)
    elif answer == "2":
        nl()
        meatlocker()
    elif answer == "3":
        nl()
        corridor("reception")
    elif answer == "4":
        print "The receptionist sits bolt upright, looks you in the eye, and barks \"Hello! What! Yes?\""
        inv.append("typewriter")
        reception_conversation()
    else:
        nl()
        print "Command not recognised. Please type a number between 1 and 4"
        reception(origin)
            
def reception_conversation():
    global inv
    print """
    1) Ask whose office this is
    2) Attempt to slide the ruins of the typewriter under the desk with your foot
    3) Ask if you can make an appointment
    """
    answer = raw_input(">")
    if answer == "1":
        print "She answers \"Why, mine, of course!\" and refuses to say anything more."
        reception_conversation()
    elif answer == "2":
        print "This does not go as well as you hoped, and you just end up moving some of the bits around. The receptionist stares at you blankly."
        reception_conversation()
    elif answer == "3":
        print "The receptionist grins broadly and says \"Why, of course! We haven't had anyone in here for years!\" She writes you out a card, in what appears to be phonecian script, and goes back to her magazine."
        inv.append("appointmentcard")
        reception("conversation")
    else:
        nl()
        print "Command not recognised. Please type a number between 1 and 3"
        reception_conversation()
        
def office():
    print "You walk into a luxuriously appointed office. Behind a broad, leather-topped desk, a small, wizened man is muttering to himself. He looks up at you, eyes unfocused, and starts ranting about the dreadful state of 'the organisation'. As you draw breath to ask what he is talking about, he interrupts with a stream of regulation numbers, fine points of law, and incoherent imprecations. He does not seem to feel the need to pause for breath, and his eyes are shining with an unholy fervour. You can feel your life slipping away as he raves. You consider killing either yourself or him, but in the end you decide to flee for your life."
    reception("office")

def meatlocker():
    print """You push open the door, and find yourself in a freezing meatlocker. As the door swings shut behind you, you notice that there is no handle on the inside either. What do you do?
    1) Try to get out of the door before it closes
    2) Look around"""
    answer = raw_input(">")
    if answer == "1": 
        nl()
        reception("meatlocker")
    elif answer == "2": 
        stuckinfreezer()
    else:
        nl()
        print "Command not recognised. Please type a number between 1 and 2"
        meatlocker()
def stuckinfreezer():
    print """The door swings shut behind you. As the neon lights flicker on, you look around the freezer. You can find no other exits, only chilled pork products hanging from the ceiling and stacked on shelves. What do you do?
        1) Panic
        2) Wait"""
    result = raw_input(">")
    if result == "1":
        print "You go mad for a time, beating on the walls and debating the existence of an afterlife with the swaying pig carcasses. When you come to your senses, a hidden door has swung open in the wall, through which you can see nothing but darkness. No other options being apparent, you walk through the door."
    elif result =="2":
        print "You wait patiently, as you become increasingly cold. After a few minutes, a hidden door swings open in the left hand wall, through which you can see nothing but darkness. Seeing no other options, you walk through the door."
    else:
        nl()
        print "Command not recognised. Please type a number between 1 and 2"
        stuckinfreezer()
    #orcroom()
    print "The end, for now."

#def orcroom():
#def staircase():
#def ballroom(origin):
#def hydroponics():

R1()