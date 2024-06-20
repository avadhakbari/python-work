#include <stdio.h>
int main()
{
    int a, b=0, c=1;
    int nextterm=a+b;
    
    printf("enter the number :-");
    scanf("%d", &a);
    
    for(int i=0; i<=a; i++)
    {
        printf("%d ", nextterm);
        b=c;
        c=nextterm;
        nextterm=b+c;
    }
}
