#include <stdio.h>

int main()
{
 
    int a, b, add, sub, mul, di, mod ;
    
    printf("enter first digit");
    scanf("%d", &a);
    
    printf("enter second digit");
    scanf("%d", &b);
    
    add=a+b;
    sub=a-b;
    mul=a*b;
    di=a/b;
    mod=a%b;
    
    
    printf("addition is:- %d\n", add);
    printf("substraction is:- %d\n", sub);
    printf("multiplication  is:- %d\n", mul);
    printf("division is:- %d\n", di);
    printf("modulo is:- %d\n", mod);
    
    return 0;
}
