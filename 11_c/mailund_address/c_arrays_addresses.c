// ID: 
// Tag: [[clang]] [[basecamp]]
// Type: #type/tech
// Status: #status/sown 
// Cntxt: @mailund 
// Prvs: 
// Nxt: 
// Brnch: 
//
// #### how to get the addresses of an array
// ---
// 
// ***Array and memory allocation***
// - Arrays allocates several objects of the same type and puts them in consecutive memory locations
// 
// ***What does de snippet***
// 1. print the array address
// 1. print each element's address by a loop (uses a matriz notation)
// 1. print the array's size
// 1. print 5 times the sizeof int
//
// ```c

#include <stdio.h>

int main(void)
{
    int array[5];
    printf("array == %p\n", (void *)array);
    for (int i = 0; i < 5; i++)
    {
        printf("&array[%d] == %p\n", i, (void *)&array[i]);
    }
    printf("sizeof array == %zu\n", sizeof array);
    printf("5 * sizeof(int == %zu\n)", 5 * sizeof(int));
    return (0);
}

// ```
