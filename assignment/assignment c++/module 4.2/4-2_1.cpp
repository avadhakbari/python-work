#include <iostream>
using namespace std;

class Calculator
{
    public:

    void add(float a, float b)
    {
        float addition= a + b;
        cout<<"addition of a and b is :"<<addition;
    }

    void sub(float a, float b)
    {
        float substrection= a - b;
        cout<<"substrection of a and b is :"<<substrection;
    }

    void mul(float a, float b)
    {
        float multiplication= a * b;
        cout<<"multiplication of a and b is :"<<multiplication;
    }

    void div(float a, float b)
    {
        float division= a / b;
        cout<<"division of a and b is :"<<division;
    }
};

int main()
{
    Calculator cal;
    float a,b;
    char op;

    cout<<"enter the number :";
    cin>>a;

    cout<<"+, -, *, /" ;
    cout<<"enter the opretor :";
    cin>>op;

    cout<<"enter the number ";
    cin>>b;

    switch(op)
    {
        case '+':
        cal.add(a,b);
        break;

        case '-':
        cal.sub(a,b);
        break;

        case '*':
        cal.mul(a,b);
        break;

        case '/':
        if(a/2 == 0)
        {
         cal.div(a,b);
        }
        else
        {
            cout<<"use valid number ";
        }
        break;

        default :
        cout<<"please enter valid opretor ";
        break;

    }
    return 0;

}