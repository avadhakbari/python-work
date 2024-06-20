#include <stdio.h>
int main()
{
    int n,original,reverse=0,remainder;
    
    printf("enter the number :");
    scanf("%d", &n);
    
    original = n;
    
    while(n != 0)
    {
        remainder = n % 10;
        reverse =reverse * 10 + remainder;
        n/=10;
    }
    
    if(original==reverse)
    {
        printf("this number is pelendrom.");
    }
    else
    {
        printf("this number is not pelendrom.");
    }
    
    return 0;
}