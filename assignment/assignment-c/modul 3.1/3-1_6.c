#include <stdio.h>

int main()
{
    float years, days, year, day;
    
    printf("enter the year :-");
    scanf("%f", &year);
    
    printf("enter the day :-");
    scanf("%f", &day);
    
    days=year*365;
    years=day/365;
    
    printf("the day is %f\n ", days);
    printf("the year is %f", years);
}