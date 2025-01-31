#include <stdio.h>

int main(void){

char username[30];

printf("What is your name?:");

scanf("%s", username);

char schoolname[30];

printf("What school do you go to?:");

scanf("%s", schoolname);

int smallnum[3];

printf("Name a number between 1 and 100:");

scanf("%s", smallnum);

int bignum[4];

printf("Name a number between 100 and 1000:");

scanf("%s", bignum);

char breakfast[30];

printf("What did you have for breakfast today?:");

scanf("%s", breakfast);

char C[30];

printf("What is your favorite color?:");

scanf("%s", C);

char eyeC[30];

printf("What is your eye color?:");

scanf("%s", eyeC);

int yr[30];

printf("What year is it?:");

scanf("%s", yr);

int age[30];

printf("How old are you?:");

scanf("%s", age);

char favsub[30];

printf("what is your favorite academic subject?:");

scanf("%s", favsub);

printf("%s" username, "%s" schoolname, smallnum, bignum, breakfast, C, eyeC, yr, age, favsub);

return 0;
}