// Jackson Clark, Financial Calculator 2 C
#include <stdio.h>

float user_in(char spend[]){
    float user_in_2;
    printf("how much money do %s each month?\n", spend);
    scanf("%f", &user_in_2);
    return user_in_2;
}  
int Perc(float var1, float income){
    return var1/income *100;
}
int main(void){
    float savings, expenses, total;
    float prent, putilities, pgroceries, ptransportation, psavings, pexpenses;
    float income = user_in("you make");
    float rent = user_in("you spend on rent");
    float utilities = user_in("you spend on utilites");
    float groceries = user_in("you spend on groceries");
    float transportation = user_in("you spend on transportation");
    expenses = rent + utilities + groceries + transportation;
    savings = income * .2;
    total = income - savings - expenses;
    printf("your montly expenses total to $%.2f \n", expenses);
    printf("your montly income is $%.2f\n", income);
    printf("assuming 20 percent of your money goes into savings, you put $%.2f into your savings each month\n", savings);
    printf("your total disposable income is $%.2f \n", total);
    prent = Perc(rent, income);
    putilities = Perc(utilities, income);
    pgroceries = Perc(groceries, income);
    ptransportation = Perc(transportation, income);
    pexpenses = Perc(expenses, income);
    psavings = Perc(savings, income);
    printf("your expenses are %.1f%% of your income \n", pexpenses);
    printf("your utilities are %.1f%% of your income \n", putilities);
    printf("your rent is %.1f%% of your income \n", prent);
    printf("your groceries are %.1f%% of your income \n", pgroceries);
    printf("your transportation is %.1f%% of your income \n", ptransportation);
    printf("your savings are %.1f%% of your income \n", psavings);
    return 0;
}