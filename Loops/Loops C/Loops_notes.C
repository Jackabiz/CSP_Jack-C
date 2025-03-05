//Jackson Clark, Loops notes

#include <stdio.h>

int main (void){
    int grades[] = {88, 19, 53, 36, 73};
    printf("%d", grades[2]);
    grades[2] = 80;
    printf("%d", grades[2]);
    int length = sizeof(grades);
        //Gives the space that the list takes up in bytes (in this case 20, as each # takes up 4 bytes)
    int length = sizeof(grades)/sizeof(grades[0]);
        //times 4 and divides by 4 to give the amount of items in the list
    return 0;
}
//What is a loop?
    //A line of code that runs lines of codes multiple times
//What are the two types of loops?
    //A for and a while loop
//What is iteration
    //Repeating something with minor changes, often to test results of said changes
        //An example of this is in a for loop, where every time it runs is an iteration
//What are arrays? 
    //A variable holding multiple values
        //An array is called a list in python
//How do you make lists in C? 
    //Arrays all need to be the same data type (because C hates you)
        //1. Set data type  2. Use brackets to specify how long the list is
//How do you make lists in python? 
    //List1 = [var1, var2, var3, etc.]
        //You can mix data types in Lists in python, because python hates you slightly less than C
//How do you make for loops in python? 
    //For var1 in var2:
//How do you make while loops in python?
    //while var1==var2:
//How do you make lists in C?
//How do you make for loops in C?
    //for (int i = 0; i < 10; i++){}
//How do you make while loops in C?
    //while(var1=var2){}








