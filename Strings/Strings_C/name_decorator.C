#include <stdio.h>
#include <string.h>

int main (void){
    char name[30];
    printf("what is your name?\n");
    scanf("%s", name);
    char name1[] = "<<<";
    char decor1_b[] = ">>>";
    strcat(name1, name);
    strcat(name1, decor1_b);
    printf("%s", name1);

    return 0;
}