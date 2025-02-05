#  Jack Clark, Variable notes

positive = "yes" or "Yes"

negative = "no" or "yes"

playing = "true"

while playing=="true":

   print("'hey, you!'")

   name = input("'what is your name?' ")

   print(f"'hello {name}!","I'm bartholemul! Do you know why we're in a basement?'")

   response = input("(yes or no)")

   if response==negative:
      print("'well, I suppose that makes sense... let's see if we can get out of here, shall we?'")
      print("there is a hallway stretching out in front of you, with a bend turning right. alternatively, you could try to go through a hole in the celling.")
      print("where do you go? (hallway o)")
   if response==positive:
      print("'you must be one of my captors! die!' \n \n you are dead")
      deathscreen = input("try again? (yes or no)")
      if deathscreen==negative:
       playing = "false"