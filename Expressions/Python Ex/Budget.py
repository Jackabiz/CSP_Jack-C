# Jackson Clark, Financial Calculator Python

point_two = .2
print("Hello! And welcome to our budget calculator! make sure to put everything in plain numbers, so no dollar signs please! \n")
income = input("how much money do you make each month on average? \n")
rent = input("how much money does your monthly rent cost?\n")
utilities = input("how much money do you spend on utilities on average each month?\n")
groceries = input("how much money do you spend on groceries each month on average?\n")
transportation = input("how much money do you spend on transportation each month on average?\n")
expenses = int(rent)+int(utilities)+int(groceries)+int(transportation)
savings = int(income)*point_two
total = int(income)-float(savings)-int(expenses)
print("your montly expenses total to $", expenses)
print("your montly income is $", income, "\n")
print("assuming 20 percent of your money goes into savings, you put $", savings, "into your savings each month\n")
print("your total disposable income is $", total, "\n")
prent = int(rent)/int(income) *100
putilities = int(utilities)/int(income)*100
pgroceries = int(groceries)/int(income) *100
ptransportation = int(transportation)/int(income) *100
pexpenses = int(expenses)/int(income) *100
psavings = int(savings)/int(income) *100
print("your expenses are", pexpenses, "% of your income \n")
print("your utilities are", putilities, "% of your income \n")
print("your rent is", prent, "% of your income \n")
print("your groceries are", pgroceries, "% of your income \n")
print("your transportation is", ptransportation, "% of your income \n")
print("your savings are", savings,"% of your income \n")