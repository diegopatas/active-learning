#include <stdio.h>

// in: five numbers
// out: the biggest


// main program

int main(void){
    printf("Enter five (5) numbers. I will print the biggest one.\n");

    int numb1, numb2, numb3, numb4, numb5;

    scanf("%d %d %d %d %d", &numb1,  &numb2, &numb3, &numb4, &numb5);

    int big;
    big = numb1;

    if(numb2 > big){ big = numb2;}
    if(numb3 > big){ big = numb3;}
    if(numb4 > big){ big = numb4;}
    if(numb5 > big){ big = numb5;}

    printf("The biggest number is: %d", big);
    
}

