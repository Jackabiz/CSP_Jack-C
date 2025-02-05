#  Jack Clark, Variable notes

playing = true

while playing = true:


print("'hey, you!'")


name = input("'what is your name?' ")

print(f"'hello {name}!","I'm bartholemul! Do you know why we're in a basement?'")

response = input("(yes or no)")

positive = "yes" or "Yes"

negative = "no" or "yes"

if response==positive:
 print("'well, I suppose that makes sense... let's see if we can get out of here, shall we?'")
else:
 print("'you must be one of my captors! die!' \n \n you are dead")
 deathscreen = input("try again? (yes or no)")
 if deathscreen==negative:
    playing = false 