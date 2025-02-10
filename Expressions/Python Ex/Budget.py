# Jackson Clark, Financial Calculator Python

print("Hello! And welcome to our budget calculator! make sure to put everything in plain numbers, so no dollar signs please! \n")

income = input("how much money do you make each month on average? \n")

rent = input("how much money does your monthly rent cost?\n")

utilities = input("how much money do you spend on utilities on average each month?\n")

groceries = input("how much money do you spend on groceries each month on average?\n")

transportation = input("how much money do you spend on transportation each month on average?\n")

expenses = int(rent)+int(utilities)+int(groceries)+int(transportation)

savings = int(income)*int(0.2)

total = int(income)-float(savings)-int(expenses)

print(f"your montly expenses total to ${expenses}\n")

print(f"your montly rent is ${rent}\n")

print(f"your montly utilities bill is ${utilities}\n")

print(f"your montly grocery bill is ${groceries}\n")

print(f"your montly transportation bill is ${transportation}\n")

print(f"your montly income is ${income}\n")

print(f"assuming 20 percent of your money goes into savings, you put ${savings} into your savings each month\n")

print(f"your total disposable income is ${total}\n")

prent = int(rent)/int(income) *100

putilities = int(utilities)/int(income)*100

pgroceries = int(groceries)/int(income) *100

ptransportation = int(transportation)/int(income) *100

pexpenses = int(expenses)/int(income) *100

psavings = int(savings)/int(income) *100

print(f"your expenses are {pexpenses}% of your income \n")

print(f"your utilities are{putilities}% of your income \n")

print(f"your rent is {prent}% of your income \n")

print(f"your groceries are {pgroceries}% of your income \n")

print(f"your transportation is  {ptransportation}% of your income \n")

print(f"you put {savings}% of your income into savings each month")