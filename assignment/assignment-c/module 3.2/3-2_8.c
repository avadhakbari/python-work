#include <stdio.h>

int main() 
{
    int a;

    printf("Enter a number: ");
    scanf("%d", &a);

    
    printf("Number in reverse order: ");
    while (a > 0)
    {
        printf("%d", a % 10);
        a /= 10;
    }

    return 0;
}
