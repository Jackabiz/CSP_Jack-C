#  Jack Clark, First program

positive = "yes" or "Yes"
negative = "no" or "No"
vent = "vent" or "Vent"
hallway = "hallway" or "Hallway" or "hall" or "Hall"
left = "left" or "Left"
right = "right" or "Right"
middle = "middle" or "Middle"

playing = "true"

while playing=="true":

   print("'hey, you!'")

   name = input("'what is your name?' ")

   print(f"'hello {name}!","I'm bartholemul! Do you know why we're in a basement?'")

   response = input("(yes or no)")

   if response==negative:
      print("'well, I suppose that makes sense... let's see if we can get out of here, shall we?'")
      print("there is a hallway stretching out in front of you, with a bend turning right. alternatively, you could try to go through an unusually large vent in the celling.")
      response = input("where do you go? (forward or vent)")
      if response==hallway:
         print("you proceed down the hallway, and as you turn the bend you find the hallway stretching into a central chamber with three hallways going to the left, right, and middle. \n all the halways have signs above them, with the middle saying 'lab', the right saying 'storage', and the left saying 'observatory'.")
         response = input("where do you go? (right, left, or middle)")
         if response==left:
            print("as you go to the left and enter the door, you begin to walk down a hallway, that takes you the same direction as you came from, but it is higher. You get to a room adjacent and above from the room you started in, and realize that you can see through the ceiling and into the vent, as well as down at the floor of the chamber. there is a standing desk with a computer terminal built into it and a key on top of it. the terminal simply says 'it's too late, the containment has failed'. would you like to take the key?")
            response = input("(yes or no")
      if response==vent:
         print("with bartholemul's help, you make it up the ventilation shaft")
   if response==positive:
      print("'you must be one of my captors! die!' \n \n you are dead")
      deathscreen = input("try again? (yes or no)")
      if deathscreen==negative:
       playing = "false"