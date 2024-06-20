#include <stdio.h>

int main()
{
                                                                                                    //circle= A=πr2
                                                                                                    //rec=A=wl
                                                                                                     //tri=A = ½ (b × h) 
                                                                                                     //3.14159265359
    float a, b, c, d, e, circle, rectangle, triangle;
    
    printf("enter the redius for circle :-");
    scanf("%f", &a);
    
    circle=3.14*a*a;
    
    printf("the area of cicrle is :-%f\n", circle);
    printf("---------------------------------------\n");
    
    printf("enter the width for rectangle :-");
    scanf("\n%f", &b);
    
    printf("enter the length for rectangle :-");
    scanf("%f", &c);
    
    rectangle=b*c;
    printf("the area of rectangle is :-%f\n", rectangle);
    
    printf("---------------------------------------\n");
    
    printf("enter the base for triangle :-");
    scanf("%f", &d);
    
    printf("enter the height for triangle :-");
    scanf("%f", &e);
    
    triangle=(d*e)/0.5;
    
    printf("the area of triangle is :-%f\n", triangle);
    printf("---------------------------------------\n");
   
     
   
   
    return 0;
}
