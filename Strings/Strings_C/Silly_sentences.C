#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (void){

    int num_ints = 3;
    char noun[30];
    char adjective[30];
    char verb[30];
    char cool[] = "cool";


    printf("Welcome to the silly sentance generator! Please input a noun.\n");
    scanf("%s", noun);
    printf("Great! now input an adjective.\n");
    scanf("%s", adjective);
    printf("Fantastic! now input a verb.\n");
    scanf("%s", verb);
    printf("The %s is %sing and %s", noun, verb, adjective);


    return 0;
}