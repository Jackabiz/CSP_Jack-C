//Jackson Clark, Time of Day C

#include <stdio.h>

int main (void){
   
    int time_of_day;
    printf("what time is it? use negatives to indicate AM and round to the nearest hour");
    scanf("%d", &time_of_day);



    if (time_of_day <= -5 && time_of_day >=-12){
     printf("good morning!");
    }
    else if (time_of_day >= 1 && time_of_day <6){      
        printf("good afternoon!");
    }
    else if (time_of_day >=6 && time_of_day <12){
     printf("good evening!");
    }
    else if (time_of_day <= -1 && time_of_day >-5){
        printf("what are you doing up at this hour?");
    }
    return 0;
}