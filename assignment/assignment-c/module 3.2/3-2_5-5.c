#include <stdio.h>

int main()
{
    int numbers[10];
    int evenCount = 0;
    int evenSum = 0;

        for (int i = 0; i < 10; i++)
       {
        printf("Enter number %d: ", i + 1);
        scanf("%d", &numbers[i]);

        if (numbers[i] % 2 == 0) 
        {
            evenCount++;
            
            evenSum += numbers[i];
        
        }
    }

    printf("Number of even numbers: %d\n", evenCount);
    printf("Sum of even numbers: %d\n", evenSum);

    return 0;
}
