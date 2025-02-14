#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main (void){
   // Set the upper bound for random numbers
   int upper_bound = 1000;
   // Set the lower bound for random numbers
   int lower_bound = 100;

   // Loop through 10 times
   for (int i = 0; i < 10; i++) {
       // Generate a random number within the specified
       // bounds
       int value = rand() % (upper_bound - lower_bound + 1)
                   + lower_bound;
       // Print the generated random value
       printf("%d ", value);
   }


    return 0;
}