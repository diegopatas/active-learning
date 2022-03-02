ID: 
Tag: [[clang]] [[basecamp]]
Type: #type/tech
Status: #status/sown 
Cntxt: @mailund
Prvs: 
Nxt: 
Brnch: 

#### Literal address expressed in hexadecimal
---
***How to get the literal address in hexa

- operando `&`

```c

#include <stdio.h>

int main(void)
{
    char    c;
    int     i;
    double  d;

    c = 1;
    i = 2;
    d = 3.0;
    printf("Address of c: %p\n", (void *)&c);
    printf("Address of i: %p\n", (void *)&i);
    printf("Address of d: %p\n", (void *)&d);
    return (0);
}

```
