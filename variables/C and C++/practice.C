// Jackson Clark, Practice C

#include <stdio.h>

int main(void){

char username[30];

printf("What is your name?: \n");

scanf("%s", username);

char schoolname[30];

printf("What school do you go to?: \n");

scanf("%s", schoolname);

int smallnum[3];

printf("Name a number between 1 and 100: \n");

scanf("%s", &smallnum);

int bignum[4];

printf("Name a number between 100 and 1000: \n");

scanf("%s", &bignum);

char breakfast[30];

printf("What did you have for breakfast today?: \n");

scanf("%s", breakfast);

char Col[30];

printf("What is your favorite color?: \n");

scanf("%s", Col);

char eyeCol[30];

printf("What is your eye color?: \n");

scanf("%s", eyeCol);

int yr[30];

printf("What year is it?: \n");

scanf("%s", &yr);

int age[30];

printf("How old are you?: \n");

scanf("%s", &age);

char favsub[30];

printf("what is your favorite academic subject?: \n");

scanf("%s", favsub);

printf("%s, %s, %d, %d, %s, %s, %s, %d, %d, %s,", username, schoolname, smallnum, bignum, breakfast, Col, eyeCol, yr, age, favsub);

return 0;
}