#include <stdio.h>

/*
 * This program is an utility that calculates
 * the sum, the product, and the average of 
 * 5 given numbers by the user.
 * */

void funSumProAv(int, int, int, int, int, int *, int *, int *);
void funcSPA(int n1, int n2, int n3, int n4, int n5, int s, int p, int av);
int funcAvg(void);

// MAIN PROGRAM
int main(void){
    // Var
    int interv;
    int num1, num2, num3, num4, num5;
    int sum, prod, ave;

    int *s = &sum;
    int *p = &prod;
    int *av = &ave;

    // init
    printf("\t---Welcome to the Utilities Program---\n");
    printf("It calculates the SUM, the PRODUCT, and the AVERAGE of five numbers.\n\n");
    
    printf("Please enter 5 numbers:\n>> ");
    scanf("%d %d %d %d %d", &num1, &num2, &num3, &num4, &num5);
    printf("%d %d %d %d %d\n", num1, num2, num3, num4, num5);

    // method 1: passing par by pointer/address (reference)
    funSumProAv(num1, num2, num3, num4, num5, &sum, &prod, &ave);
    printf("\nSECOND RESULT:\n");
    printf("\tSum: %d\n\tProd: %d\n\tAver: %d", *s, *p, *av);

    // method 2: void function 
    funcSPA(num1, num2, num3, num4, num5, sum, prod, ave);
    printf("\nFIRST RESULT:\n");
    printf("\tSum: %d\n\tProd: %d\n\tAver: %d", *s, *p, *av);

    interv = funcAvg();
    printf("You entered:\n");

    for(int i = 0; i < 5; i++){
       printf("%d", interv);
    }
}

// function definition area

void funSumProAv(int n1, int n2, int n3, int n4, int n5, int *sum, int *prod, int *ave){
    // It could not be passed &var because we are accepting addresses as param.
    // We have to pass *p pointers as param instead.

    // I need to init the pointer
    *sum = n1 + n2 + n3 + n4 + n5;
    *prod = n1 * n2 * n3 * n4 * n5;
    *ave = *sum / 5;
}

void funcSPA(int n1, int n2, int n3, int n4, int n5, int s, int p, int av){
    s = n1 + n2 + n3 + n4 + n5 + 10;
    p = n1 * n2 * n3 * n4 * n5 * 2;
    av = s / 5;

    printf("Show output for function using parameters by value.");
    printf("\n\tSum: %d\n\tProduct: %d\n\tAverage: %d", s, p, av);
}

int funcAvg(void){
    
    int interv[5]; 
    int i;
    int aux;
    char flag;

    i = 0;
    aux = 0;
    flag = 'y';

    while(flag != 'n'){
        printf("\nDo you want to add a number? [y]es or [n]o?\n>> ");
        scanf("%c", &flag);

        if(flag == 'y'){
            scanf("%d", &aux);
            printf("Enter a number:\n>> ");
            scanf("%d", &aux);

            interv[i] = aux;
                i++ ;
        }
        else if(flag == 'n') {
            printf("\nThank you!");
            
        }
        else {
            printf("\nInvalid option, please try again.");
        }
    }
}
