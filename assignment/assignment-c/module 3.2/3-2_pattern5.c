#include<stdio.h>
int main()
{
    int a,b=1;
    
    printf("enter the number :-");
    scanf("%d", &a);
    
    for(int i=1; i<=a; i++)
    {
        for(int j=0; j<i; j++)
        {
            printf("%d\t", b++);
        }
        printf("\n");
    }
}