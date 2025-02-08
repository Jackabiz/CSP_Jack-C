// Jackson Clark, Financial Calculator C

#include <stdio.h>
#include <math.h>

int main (void){
float income, rent, utilities, groceries, transportation, savings, expenses, total;
float prent, putilities, pgroceries, ptransportation, psavings, pexpenses;
printf("Hello! And welcome to our budget calculator! make sure to put everything in plain numbers, so no dollar signs please! \n");
printf("how much money do you make each month on average? \n");
scanf("%f", &income);
printf("how much money does your monthly rent cost?\n");
scanf("%f", &rent);
printf("how much money do you spend on utilities on average each month?\n");
scanf("%f", &utilities);
printf("how much money do you spend on groceries each month on average?\n");
scanf("%f", &groceries);
printf("how much money do you spend on transportation each month on average?\n");
scanf("%f", &transportation);
expenses = rent + utilities + groceries + transportation;
savings = income * .2;
total = income - savings - expenses;
printf("your montly expenses total to $%.2f \n", expenses);
printf("your montly income is $%.2f\n", income);
printf("assuming 20 percent of your money goes into savings, you put $%.2f into your savings each month\n", savings);
printf("your total disposable income is $%.2f \n", total);
prent = rent/income *100;
putilities = utilities/income *100;
pgroceries = groceries/income *100;
ptransportation = transportation/income *100;
pexpenses = expenses/income *100;
psavings = savings/income *100;
printf("your expenses are %.1f%% of your income \n", pexpenses);
printf("your utilities are %.1f%% of your income \n", putilities);
printf("your rent is %.1f%% of your income \n", prent);
printf("your groceries are %.1f%% of your income \n", pgroceries);
printf("your transportation is %.1f%% of your income \n", ptransportation);
printf("your savings are %.1f%% of your income \n", psavings);
    return 0;
}