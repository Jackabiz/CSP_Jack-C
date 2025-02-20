// Jackson Clark, update Hello World C

#include <stdio.h>


void hello(char name[30]){
    printf("hello %s\n", name);
}

int main(void){
 
    char name1[30] = "jeffry";
    char name2[30] = "jeffret";
    char name3[30] = "jefferson";
    char name4[30] = "jeff";
    char name5[30] = "jeffrina";
    hello(name1);
    hello(name2);
    hello(name3);
    hello(name4);
    hello(name5);

    return 0;
}