# Jackson Clark, Financial Calculator 2 python
print("Hello! And welcome to our budget calculator! make sure to put everything in plain numbers, so no dollar signs please! \n")

def user_in(spend):
    return input(f"how much money do {spend} each month?\n")

income = user_in("you make")

rent = user_in("you spend on rent")

utilities = user_in("you spend on utilities")

groceries = user_in("you spend on groceries")

transportation = user_in("you spend on transportation")

expenses = int(rent)+int(utilities)+int(groceries)+int(transportation)

savings = int(income) *float(0.2)

total = int(income)-float(savings)-int(expenses)

print(f"your montly expenses total to ${expenses}\n")

print(f"your montly rent is ${rent}\n")

print(f"your montly utilities bill is ${utilities}\n")

print(f"your montly grocery bill is ${groceries}\n")

print(f"your montly transportation bill is ${transportation}\n")

print(f"your montly income is ${income}\n")

print(f"assuming 20 percent of your money goes into savings, you put ${savings} into your savings each month\n")

print(f"your total disposable income is ${total}\n")

def Perc(var1, income):
    return int(var1)/int(income) *100

prent = Perc(rent, income)

putilities = Perc(utilities, income)

pgroceries = Perc(groceries, income)

ptransportation = Perc(transportation, income)

pexpenses = Perc(expenses, income)

psavings = Perc(savings, income)

print(f"your expenses are {pexpenses}% of your income \n")

print(f"your utilities are{putilities}% of your income \n")

print(f"your rent is {prent}% of your income \n")

print(f"your groceries are {pgroceries}% of your income \n")

print(f"your transportation is  {ptransportation}% of your income \n")

print(f"you put {psavings}% of your income into savings each month")