#include <stdio.h>

int main()
{
    int a, b;
    
    printf("enter the value of a :-");
    scanf("%d", &a);
    
    printf("enter the value of b :-");
    scanf("%d", &b);
    
    a=a+b;   //a=30
    b=a-b;   //b=10
    a=a-b;   //a=20
    
    printf("value of a :-%d\n", a);
    printf("value of b :-%d", b);
    return 0;
}
