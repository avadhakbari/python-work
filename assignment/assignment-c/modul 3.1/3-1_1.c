#include <stdio.h>

int main()
{
    int age,date;
    char add[50];
    char name[50];      
    
    printf("enter your name :");
    scanf("%s", &name);
    
    printf("enter your birth date :");
    scanf("%d", &date);
    
    printf("enter your age :");
    scanf("%d", &age);
    
    printf("enter your address :");
    scanf("%s", &add);
    printf("-------------------\n");
    printf("your name is %s\n", name);
    printf("your birth date is %d\n",date);
    printf("your age is %d\n", age);
    printf("your address is %s\n", add);
    
   
    return 0;
}
