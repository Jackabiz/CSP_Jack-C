#  Jack Clark, First program

positive = "yes" or "Yes"
negative = "no" or "No"
vent = "vent" or "Vent"
hallway = "hallway" or "Hallway" or "hall" or "Hall"
left = "left" or "Left"
right = "right" or "Right"
middle = "middle" or "Middle"
back = "back" or "Back"

def has_item(item):
   if item==negative:
      print("you don't have the correct tools for this. maybe explore a bit more and come back")
   if item==positive:
      return positive
def been_here(bool, room):
   if bool==positive:
      print(f"you come back to the {room}")
   else:
      return negative
def death_screen(play, bool):
  play = positive
  bool = input("try again? (yes or no)")
  if bool==negative:
       play = negative
       return play
  else:
      return play
has_key = negative

has_crowbar = negative

playing = positive

in_crossroads = negative

play_these_games_before = negative

while playing==positive:

   print("'hey, you!' you hear as you open your eyes to a moist, grey, and empty rectangular room, with only a dim lightbulb in the center for light")

   name = input("'what is your name?'(enter name here)\n")

   print(f"'hello {name}!","I'm bartholemul! Do you know why we're in what seems to be a basement?'")

   response = input("(yes or no)\n")

   if response==negative:
      print("'well, I suppose that makes sense... let's see if we can get out of here, shall we?'")
      print("there is a hallway stretching out in front of you, with a bend turning right. alternatively, you could try to go through an unusually large vent in the celling.")
      response = input("where do you go? (hallway or vent)\n")
      if response==hallway:
         in_crossroads = positive
         while in_crossroads==positive:
            been_here(play_these_games_before, "crossroads")
            if play_these_games_before==negative:
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
                  play_these_games_before = positive
            elif response==right:
             if has_key==positive:
                print("althought the door is locked, you find that they key you picked up in the observatory is a perfect fit for the door, and it opens for you as you twist it in. bartholemul looks uneasy as you enter the damp, dark corridor.")
                storage_access = positive
             elif has_crowbar==positive:
                  print("the door is locked, but you use the crowbar you found in the lab to force it open anyway. with your trusty weapon in hand, you and bartholemul are confident in going down the damp, dark corridor.")
                  storage_access = positive
             if storage_access==positive:
                print("you arrive at the so called storage room. It is dark and wet, and you can barely see anything, but as you feel around you ")
             elif has_key==negative or has_crowbar==negative:
                  print("you walk up to the door to the storage room only to find it locked, and no amount of shoving will get you in.")
            elif response==middle:
               print
      elif response==vent:
         print("with bartholemul's help, you make it up the ventilation shaft.")
         response = input("up here, you see a path to the left with steel bars blocking the way and a path and a path to the right stretching on to what seems like forever. where do you go?\n")
         if response==left:
            has_item(has_crowbar)
            if positive:
               print("you use the crowbar to wedge open the steel pipes and crawl through. ")
         if response==right:
            print("you crawl through the seemingly endless vents for hours. the hours turn into days, and although you didn't realize it, the vent was getting ever so slightly more narrow the further you crawled. you starve to death in the tunnel")
            deathscreen = input("try again? (yes or no)\n")
            if deathscreen==negative:
               playing = negative
               in_crossroads = negative
   elif response==positive:
      print("'you must be one of my captors! die!' \n \n you are dead.")
      deathscreen = input("try again? (yes or no)\n")
      if deathscreen==negative:
       playing = negative
print("thanks for playing the free demo! for the full version, please wait 999 years and pay $19318.09 right now!")
      