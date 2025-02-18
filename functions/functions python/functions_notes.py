# Jackson Clark, functions notes python

# a function holds and organizes actions
#set up function
def hello():
    hello1 = input("what is your standard greeting?")
    print(hello1)
hello()
#print(hello1) gives an error, as you cannot print a variable that is inside of the function outside of the function

#snake_case -> no capitals and underscores instead of spaces
#camelCase -> removes spaces and any word after the 1st one starts with a capital

#how to give information to a function:
    #parameter : #def hello(var1, var2, var3, etc.)
    #argument : hello(var12, var22, var23, etc.)
    #you have to give any argument the same number of variables as the parameter for the function
def add(num1, num2):
    return num1 + num2
    # return statements essentially turn the function into a variable, and it can be used as such (i.e. print(add)(parameters))
print (add(3, 132))

def values(type):
    return input(f"please give me a {type}\n")
    #this can be used to repeat things values("name")
name = values("place")
adjective = values("adjective")
place = values("place")
print(f"{name} was really {adjective} and went to {place}")
#you need to save the values in a variable

