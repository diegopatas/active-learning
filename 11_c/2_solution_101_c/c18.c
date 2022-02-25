#include <stdio.h>

/*Monthly Bill Calculator*/

int Residential(void){
    // init case 1
    char resOption;

    float price,
          fixedCost,
          unitConsumed,
          totalBill;

    scanf("%c", &resOption);
    // init fixed cost
    printf("Choose your type of cost:\n\t[1] 1-phase meter\n\t[2] 3-phase meter\n>> ");
    scanf("%c", &resOption);

    if(resOption == '1') {
        fixedCost = 50;

    } else if(resOption == '2'){
        fixedCost = 200;

    } else {
        fixedCost = 50;
        printf("\nInvalid option.\nIt's going to be add the lower value: %.2f", fixedCost);
    }

    // first total
    totalBill = fixedCost;

    // init consume
    printf("Now, enter your consume in Unit(s):\n>> ");
    scanf("%f", &unitConsumed);

    if(unitConsumed < 0) {
        printf("Invalid value! The Unit most be positive. Try again.");

    } else if(unitConsumed >= 0 && unitConsumed <= 100) {
        price = 3.76;

    } else if(unitConsumed > 100 && unitConsumed <= 300) {
        price = 7.21;

    } else if(unitConsumed > 300 && unitConsumed <= 500) {
        price = 9.95;

    } else {
        price = 11.31;

    }

    // calculation
    totalBill = totalBill + unitConsumed * price;

    // return 
    printf("\n\t---REPORT---\n");
    printf("\n\tFixed Cost: %.2f\n\tPrice: %.2f\n\tUnit(s) consumed: %.2f\n\tYour bill: %.2f\n", fixedCost, price, unitConsumed, totalBill);
    printf("\n\t---END REPORT---");
}

int Comercial(void){
    // init var
    float totalBill,
          price, 
          fixedCost,
          unitConsumed;

    // first total
    fixedCost = 220;
    totalBill = fixedCost;

    // enter consume
    printf("Now, enter your consume in Unit(s):\n>> ");
    scanf("%f", &unitConsumed);

    if(unitConsumed < 0){
        printf("Invalid value. Please enter a positive one.");

    }else if(unitConsumed >= 0 && unitConsumed <= 200){
        price = 6.60;
    }else{
        price = 9.62;
    }

    // calc
    totalBill = totalBill + unitConsumed * price;

    // return 
    printf("\n\t---REPORT---\n");
    printf("\n\tFixed Cost: %.2f\n\tPrice: %.2f\n\tUnit(s) consumed: %.2f\n\tYour bill: %.2f\n", fixedCost, price, unitConsumed, totalBill);
    printf("\n\t---END REPORT---");
}

int Industrial(void){
    // init var
    float price,
          unitConsumed,
          fixedCost,
          totalBill;

    // first total
    fixedCost = 250;
    totalBill = fixedCost;

    // enter consume
    printf("Now, enter your consume in KW:\n>> ");
    scanf("%f", &unitConsumed);

    if(unitConsumed < 0){
        printf("Invalid value. Please enter a positive one.");
    } else if(unitConsumed <= 20){
        price = 5.53;
    } else {
        price = 6.88;
    }

    // calc
    totalBill = totalBill + unitConsumed * price;

    // return
    printf("\n\t---REPORT---\n");
    printf("\n\tFixed Cost: %.2f\n\tPrice: %.2f\n\tUnit(s) consumed: %.2f\n\tYour bill: %.2f\n", fixedCost, price, unitConsumed, totalBill);
    printf("\n\t---END REPORT---");
}


// MAIN PROGRAM
int main(void){
    char resp;

    printf("Welcome to the <Eletricity Bill Calculator>\n\n");
    printf("--------\n\nMenu:\n");

    printf("Choose your category.\n\t[1] Residential\n\t[2] Commercial\n\t[3] Industrial\n\t[q] to quit\n>> ");
    scanf("%c", &resp);

    switch(resp){
        case '1':
            Residential();
            break;

        case '2':
            Comercial();
            break;

        case '3':
            Industrial();
            break;

        case 'q':
            break;

        default:
            printf("Invalid option, please choose a valid one.");
            break;
    }
}
