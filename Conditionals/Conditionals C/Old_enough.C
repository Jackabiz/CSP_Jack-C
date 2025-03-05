//Jackson Clark, Old Enough C


#include <stdio.h>

int main(void){

    float age;
    printf("How old are you? \n");
    scanf("%f", &age);
    if (age >= 18)
        printf("you can go to school, drive, and even vote!");
    

    else if (age >= 16 && age < 18)
        printf("you can go to school and drive!");


    else if (age >= 15.5 && age < 16)
        printf("you can go to school and get your learner's permit!");
    

    else if (age >= 5 && age < 15.5)
        printf("you can go to school!");
    
    else
      printf("how are you even using this program?");
    
    return 0;
}