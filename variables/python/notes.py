#  Jack Clark, Variable notes

greeting = "'hey, you!'"

playing = "true"

positive = "Yes" or "yes" 

negative = "No" or "no"

while playing=="true":
  print(greeting)
  greeting = ""
  name = input("'what is your name?' ")
  print(f"'hello {name}!","I'm bartholemul! Do you know why we're in a basement?'")
  response = input("")
  if response==negative:
    print("'well, I suppose that makes sense... let's see if we can get out of here, shall we?'")
  if response==positive:
    print("'you must be one of my captors! die!' \n \n you are dead")
    deathscreen = input("try again? (yes or no)")
    if deathscreen==negative:
     playing = "false"
else:
  print("thanks for playing!")
     
     

  


