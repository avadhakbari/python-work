#include <stdio.h>

int main()
{
    int even_count = 0;
    int num;

    printf("Enter 10 numbers:\n");

    for (int i = 0; i < 10; i++)
    {
        printf("Enter number %d: ", i + 1);
        scanf("%d", &num);
    
        if (num % 2 == 0) 
        {
           
            even_count++;
        }
    }

    printf("\nNumber of even numbers: %d\n", even_count);

    return 0;
}

