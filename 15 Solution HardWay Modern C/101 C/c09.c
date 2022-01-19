#include <stdio.h>

// in: c
// out: type of the char


// main program
int main(void){
    // input
    printf("Enter a character:\n>> ");

    char cht; // chartyped
    scanf("%c", &cht);

    if(cht >= 65 && cht <= 90){
        printf("You entered: %c\n", cht);
        printf("\tit is in Uppercase!");
    }

    if(cht >= 48 && cht <= 57){
        printf("You entered: %c\n", cht);
        printf("\tit is a digit!");
    }

    if(cht >= 97 && cht <= 122){
        printf("You entered: %c\n", cht);
        printf("\tit is in Lowercase!");
    }

    if((cht >= 33 && cht <= 47) || (cht >= 58 && cht <= 64) || (cht >= 91 && cht <= 96) || (cht >= 123 && cht <= 126)){
        printf("You entered: %c\n", cht);
        printf("\tit is a symbol!");
    }
}
