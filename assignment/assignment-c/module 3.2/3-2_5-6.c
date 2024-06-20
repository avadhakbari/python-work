#include <stdio.h>

int main()
{
    int numbers[10];
    int oddCount = 0;
    int oddSum = 0;
    int total;

        for (int i = 0; i < 10; i++) {
        printf("Enter number %d: ", i + 1);
        scanf("%d", &numbers[i]);

        if (numbers[i] % 2 != 0) 
        {
            oddCount++;
            
            oddSum += numbers[i];
        
        }
    }

    printf("Number of even numbers: %d\n", oddCount);
    printf("Sum of even numbers: %d\n", oddSum);
    
    for(int j=1; j<=10; j++)
    {
        total=oddSum*j;
        
        printf("%d * %d = %d\n",oddSum, j, total);
    }

    return 0;
}
