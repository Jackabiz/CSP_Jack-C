#include <stdio.h>

int main (void){
    for (int x=0;x<51;x++){
        int i = x%3;
        int e = x%5;
        if (i+e==0)
         printf("FizzBuzz\n");
        else if (i==0)
         printf("Fizz\n");
        else if (e==0)
         printf("Buzz\n");
        else
         printf("%d\n", x);
     
    }

    return 0;
}