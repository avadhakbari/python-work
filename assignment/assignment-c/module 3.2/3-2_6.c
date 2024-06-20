#include <stdio.h>

int main() 
{
    int num;
    long factorial = 1;  

    printf("Enter a positive integer: ");
    scanf("%d", &num);

    if (num > 0) 
    {
         
        for (int i = 1; i <= num; i++) 
        {
            factorial *= i;
        }
        printf("Factorial of %d is %ld\n", num, factorial);
    
    }
    
    else 
    {
        printf("Factorial is not defined for negative numbers.\n");
    }
   

    return 0;
}
