// ID: 
// Tag: [[clang]] [[basecamp]]
// Type: #type/tech
// Status: #status/sown 
// Cntxt: @mailund 
// Prvs: 
// Nxt: 
// Brnch: 
//
// #### C standard - size of a char
// ---
// - One char is the minimum size that c works with
// 
// ```c

#include <stdio.h>

int main(void)
{
    char    c;
    int     i;
    double  d;
    printf("sizeof char: %zu\n sizeof c (type char): %zu", sizeof(char), sizeof c);
    printf("sizeof int: %zu\n sizeof i (type int): %zu", sizeof(int), sizeof i);
    printf("sizeof double: %zu\n sizeof d (type double): %zu", sizeof(double), sizeof d);
    return (0);
}

// ```
