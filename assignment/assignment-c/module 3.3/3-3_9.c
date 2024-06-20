#include <stdio.h>

struct Employee {
    int empno;
    char empname[50];
    char address[100];
    int age;
};

int main() 
{
    
    struct Employee employee;

    
    printf("Enter Employee Details:\n");
    printf("Employee Number: ");
    scanf("%d", &employee.empno);
    printf("Employee Name: ");
    scanf(" %[^\n]s", employee.empname); 
    printf("Address: ");
    scanf(" %[^\n]s", employee.address);
    printf("Age: ");
    scanf("%d", &employee.age);

   
    printf("\nEmployee Information:\n");
    printf("Employee Number: %d\n", employee.empno);
    printf("Employee Name: %s\n", employee.empname);
    printf("Address: %s\n", employee.address);
    printf("Age: %d\n", employee.age);

    return 0;
}
