#include <stdio.h>
#define MAX 10

int main(void){

    int interval[MAX];
    int average, sum;
    int i;
    char resp;

    resp = 'y';
    i = 0;

    // INIT
    printf("AVERAGE PROGRAM\n\n\tThis program calculates an average of given numbers.\n\tIt can reads 10 numbers maximum.\n");
   
    while(resp == 'y'){
        puts("Do you want to add a number?\n");
        scanf("%c", &resp);

        if(resp == 'y'){
            printf("Enter a number:\n>> ");
            scanf("%d", &interval[i]);
            i++;
        }
    }

    printf("You entered the following numbers:\n");

    for(int i = 0; i < MAX; i++){
        printf("\t%d", interval[i]);
    }

    printf("The average is:\n");

    for(int i = 0; i < MAX; i++){
        sum = sum + interval[i];
    }

    average = sum / (sizeof(interval[MAX]/(sizeof(int)));
    printf("%d", average);
}
