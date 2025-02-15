#include <stdlib.h>
#include <stdio.h>

int main(void){

    int num_ints = 3;

    int rand_value1 = rand() % (num_ints+1);
    int rand_value2 = rand() % (num_ints+1);
    while (rand_value1 = rand_value2){
     int rand_value2 = rand() % (num_ints+1);
    }
    
    return 0;
}