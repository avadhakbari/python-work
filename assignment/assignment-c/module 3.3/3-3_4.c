#include <stdio.h>
long int multiplyNumber(int n);
int main()
{
    int n;
    
    printf("enter the number :");
    scanf("%d", &n);
    
    printf("factorial of %d is %ld",n,multiplyNumber(n));
    return 0;
}

long int multiplyNumber(int n)
{
    if(n>=1)
    {
        return n*multiplyNumber(n-1);
        
    }
    else
    {
        return 1;
    }
}