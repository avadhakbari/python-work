#include <stdio.h>

int main() 
{
    float num1, num2, result;
    char operator;

    
    printf("Enter first number: ");
    scanf("%f", &num1);

    printf("Enter an operator (+, -, *, /): ");
    scanf(" %c", &operator); 

    printf("Enter second number: ");
    scanf("%f", &num2);

    
    switch (operator) 
    {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            if (num2 != 0)
            {
                result = num1 / num2;
            } 
            else
            {
                printf("Division by zero is not allowed.\n");
               
            }
            break;
            
        default:
            printf("enter not Invalid operator.\n");
            
    }

   
    printf("Result: %f\n", result);

    return 0; // Exit program normally
}
