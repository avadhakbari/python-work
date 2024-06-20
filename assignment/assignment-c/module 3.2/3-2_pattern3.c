#include <stdio.h>

int main()
{
    int a;
    printf("enter the value :-");
    scanf("%d", &a);

    for(int i=0; i<=a; i++)
    {
        for(int k=a; k>i; k--)
        {
            printf(" ");
        }
        for(int j=0; j<i*2-1; j++)
        {
            printf("*");
        }
        printf("\n");
    }
    
    return 0;
}