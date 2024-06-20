#include <stdio.h>

int main()
{
    float a,p,r,t, finalAmount;
    
    //this is a principal balance
    printf("enter the initial principal balance :-");
    scanf("%f", &p);
    
    //this is a interest rate
    printf("enter the annual interest rate :-");
    scanf("%f", &r);

    //this is a time 
    printf("enter the time (year) :-");
    scanf("%f", &t);

    //the formula of simple interest is a=p(1+r*t)
    a=1+r*t;
    finalAmount=p*a;
    
    printf("the final amount is %f", finalAmount);
    return 0;
}