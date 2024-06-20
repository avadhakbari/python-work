#include <stdio.h>

int main()
{
    
    int num;

    printf("Enter 10 numbers:\n");

    for (int i = 0; i < 10; i++)
    {
        printf("Enter number %d: ", i + 1);
        scanf("%d", &num);
    }


    return 0;
}

