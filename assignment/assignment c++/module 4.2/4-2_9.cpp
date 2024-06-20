#include <iostream>
using namespace std;

class Calculator
{
public:
    void calculate(double a, int b)
    {
        cout << "addition of two numbers is: " << a + b << endl;
    }

    void calculate(double c, double d)
    {
        cout << "subtraction of two numbers is: " << c - d << endl;
    }

    void calculate(int c, double f)
    {
        cout << "multiplication of two numbers is: " << c * f << endl;
    }

    void calculate(int m, int n)
    {
        if (n != 0)
        {
            cout << "division of two numbers is: " << m / n << endl;
        }
    }
};

int main()
{
    Calculator cal;
    cal.calculate(10.0, 20); // addition
    cal.calculate(7.0, 7.0); // subtraction
    cal.calculate(5, 20.0);  // multiplication
    cal.calculate(50, 5);    // division

    return 0;
}
