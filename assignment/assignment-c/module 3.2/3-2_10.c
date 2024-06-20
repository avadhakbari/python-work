#include <stdio.h>
int main()
{
    int a,b, sum=0;
    
    printf("enter the number :-");
    scanf("%d", &a);
    
    while(a != 0)
    {
      b=a%10;                                    
      a/=10;                                       
    
      sum += b;
        
    }
    
    printf("%d", sum);
    return 0;
}