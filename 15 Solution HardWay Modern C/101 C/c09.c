#include <stdio.h>

// main program
int main(void){
    // input
    printf("Enter a character:\n>> ");

    char cht; // chartyped
    scanf("%c", &cht);

    // 33 - 126
    
    if(cht >= 33 && cht <= 126){
        if((cht >= 48 && cht <= 57) || (cht >= 65 && cht <= 90) || (cht >= 97 && cht <= 122)){
            if(cht >= 48 && cht <= 57){
                printf("You entered '%c', which is a digit!", cht);
            }else if(cht >= 65 && cht <= 90){
                printf("You entered '%c', which is a Uppercase character!", cht);
            }else if(cht >= 97 && cht <=122){
                printf("You entered '%c', which is a Lowercase character", cht);
            }
        }
        else {
            printf("You entered '%c' which is symbol!", cht);
        }

    }
    else{
        printf("You entered a invalid character. Please try again.");
    }
}
