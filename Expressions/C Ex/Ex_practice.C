#include <stdio.h>
#include <math.h>

int main (void){

float eq_one = 7-24/8*4+6;
float eq_two = 18/3-7+2*5;
float eq_three = 6*4/12+72/8-9;
float eq_four = (17-6/2)+4*3;
float eq_five = -2*(1*4-2/2)+(6+2-3);
float eq_six = -1*((3-4*7)/5)-2*24/6;
float eq_seven= (3*(float)pow(5,2)/15)-(5-(float)pow(2,2));
float eq_eight= ((float)pow(1,4)*(float)pow(2,2)+(float)pow(3,3))-(float)pow(2,5)/4;
float eq_nine= (float)pow((22/2-2*5),2)+(float)pow((4-6/6),2);

printf("%d,%d,%d,%d,%d,%d,%d,%d,%d,", eq_one, eq_two, eq_three, eq_four, eq_five, eq_six, eq_seven, eq_eight, eq_nine);

    return 0;
}