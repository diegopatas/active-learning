#include <stdio.h>

// MAIN PROGRAM
int main(void){
    printf("Enter the first number:\n>> ");

    int numb1;
    scanf("%d", &numb1);

    printf("Enter the second number:\n>> ");

    int numb2;
    scanf("%d", &numb2);

    // interchange position algo
    int aux;
    aux = numb1;
    numb1 = numb2;
    numb2 = aux;

    printf("You typed:\n\tFirst number: %d\n\tSecond number: %d", numb1, numb2);
}
