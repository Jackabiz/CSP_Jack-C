#  Jack Clark, First program

positive = "yes" or "Yes"
negative = "no" or "No"
vent = "vent" or "Vent"
hallway = "hallway" or "Hallway" or "hall" or "Hall"
left = "left" or "Left"
right = "right" or "Right"
middle = "middle" or "Middle"
back = "back" or "Back"

has_key = negative

has_crowbar = negative

playing = positive

in_crossroads = negative

while playing==positive:

   print("'hey, you!' you hear as you open your eyes to a moist, grey, and empty rectangular room, with only a dim lightbulb in the center for light")

   name = input("'what is your name?'(enter name here)")

   print(f"'hello {name}!","I'm bartholemul! Do you know why we're in what seems to be a basement?'")

   response = input("(yes or no)")

   if response==negative:
      print("'well, I suppose that makes sense... let's see if we can get out of here, shall we?'")
      print("there is a hallway stretching out in front of you, with a bend turning right. alternatively, you could try to go through an unusually large vent in the celling.")
      response = input("where do you go? (hallway or vent)")
      if response==hallway:
         in_crossroads = positive
         while in_crossroads==positive:
            print("you proceed down the hallway, and as you turn the bend you find the hallway stretching into a central crossroads with three hallways going to the left, right, and middle. \n all the halways have signs above them, with the middle saying 'lab', the right saying 'storage', and the left saying 'observatory'. \n of course, you can always go back to the original chamber if you want to try the vent as well.")
            response = input("where do you go? (right, left, middle, or back)")
            if response==left:
               print("as you go to the left and enter the door, you begin to walk down a hallway, that takes you the same direction as you came from, but it is higher. You get to a room adjacent and above from the room you started in, and realize that you can see through the ceiling and into the vent, as well as down at the floor of the chamber. there is a standing desk with a computer terminal built into it and a key on top of it. the terminal simply says 'it's too late, the containment has failed'. would you like to take the key?")
               response = input("(yes or no)")
               if response==negative:
                  print("you decide to ignore the key for now and go back to the crossroads")
               elif response==positive:
                  has_key = positive
                  print("you pick up the key and decide to go back to the crossroadds")
            elif response==right:
             if has_key==positive:
                print("althought the door is locked, you find that they key you picked up in the observatory is a perfect fit for the door, and it opens for you as you twist it in. bartholemul looks uneasy as you enter the damp, dark corridor.")
             elif has_crowbar==positive:
                  print("the door is locked, but you use the crowbar you found in the lab to force it open anyway. with your trusty weapon in hand, you and bartholemul are confident in going down the damp, dark corridor.")
             elif has_key==negative or has_crowbar==negative:
                  print("you walk up to the door to the storage room only to find it locked, and no amount of shoving will get you in.")
      elif response==vent:
         print("with bartholemul's help, you make it up the ventilation shaft.")
   elif response==positive:
      print("'you must be one of my captors! die!' \n \n you are dead.")
      deathscreen = input("try again? (yes or no)")
      if deathscreen==negative:
       playing = negative