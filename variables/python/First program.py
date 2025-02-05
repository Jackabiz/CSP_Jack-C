#  Jack Clark, First program

positive = "yes" or "Yes"

negative = "no" or "No"

vent = "vent" or "Vent"

hallway = "hallway" or "Hallway" or "hall" or "Hall"

playing = "true"

while playing=="true":

   print("'hey, you!'")

   name = input("'what is your name?' ")

   print(f"'hello {name}!","I'm bartholemul! Do you know why we're in a basement?'")

   response = input("(yes or no)")

   if response==negative:
      print("'well, I suppose that makes sense... let's see if we can get out of here, shall we?'")
      print("there is a hallway stretching out in front of you, with a bend turning right. alternatively, you could try to go through an unusually large vent in the celling.")
      response = input("where do you go? (hallway or vent)")
      if response==hallway:
         print("you proceed down the hallway")
      if response==vent:
         print("with bartholemul's help, you make it up the ventilation shaft")
   if response==positive:
      print("'you must be one of my captors! die!' \n \n you are dead")
      deathscreen = input("try again? (yes or no)")
      if deathscreen==negative:
       playing = "false"