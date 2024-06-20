#include<stdio.h>
int main()
{
    int a;
    char ch='A';
    printf("enter the number :-");
    scanf("%d", &a);
    
    for(int i=0; i<=a; i++)
    {
        for(int j=0; j<i; j++)
        {
            printf("%c\t", ch+j);
        }
        printf("\n");
    }
}