# Jackson Clark, Name Decorator Python

print("welcome to the name decorator!")

name = input("what is your name?")

decor1_a = "<<<"
decor1_b= ">>>"
decor2_a = "((("
decor2_b = ")))"
decor3_ab = "---"
decor4_a = ":3:"
decor4_b = ":3:3"
decor5_ab = "+++"
decor6_ab = "==="

selection = input(f"hello {name}! what would you like your decoration to be? please type in the first 3 characters of the decoration (i.e. <<< = <<<Name>>>)\n <<<Name>>>, \n (((Name))), \n ---Name---, \n :3:3Name:3:3, \n ###Name###, \n +++Name+++, \n ===Name=== \n")

if selection==decor1_a:
    print(decor1_a+name+decor1_b)
if selection==decor2_a:
    print(decor2_a+name+decor2_b)
if selection==decor3_ab:
    print(decor3_ab+name+decor3_ab)
if selection==decor4_a:
    print(decor4_b+name+decor4_b)
if selection==decor5_ab:
    print(decor5_ab+name+decor5_ab)
if selection==decor6_ab:
    print(decor6_ab+name+decor6_ab)





