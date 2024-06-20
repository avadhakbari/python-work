#include <iostream>
using namespace std;

class Calculator
{
    
    int num1, num2;

    public:
    Calculator(int a, int b)
    {
        num1 = a;
        num2 = b;
    }
    
    void add()
    {
        int ans = num1 + num2;
        cout<<"addiotion of num1 and num2 is :"<<ans<<endl;
    }

    void sub()
    {
        int ans = num1 - num2;
        cout<<"substrection of num1 and num2 is :"<<ans<<endl;
    }

    void mul()
    {
        int ans = num1 * num2;
        cout<<"multiplication of num1 and num2 is :"<<ans<<endl;
    }

    void div()
    {
        if(num1>num2)
        {
            int ans = num1 / num2;
            cout<<"division of num1 and num2 is :"<<ans<<endl;
        }
        else
        {
            cout<<"please enter valid number "<<endl;
        }
    }

};

int main()
{
    int a,b;

    cout<<"enter the number 1:";
    cin>>a;

    cout<<"enter the number 2: ";
    cin>>b;

    Calculator c(a,b);
    c.add();
    c.sub();
    c.mul();
    c.div();
    
    return 0;
}