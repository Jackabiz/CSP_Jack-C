#include <stdio.h>

int main (void){
    char name[30];
    printf("what is your name?");
    scanf("%s", name);
    printf("<<< %s >>>", name);

    return 0;
}