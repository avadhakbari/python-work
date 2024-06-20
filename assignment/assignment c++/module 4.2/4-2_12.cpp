#include <iostream>
using namespace std;

class Find
{
    public:

    void calcualte(int a, int b)
    {
         
        cout<<"area of rectangle is "<<a * b <<endl;
    } 

    void calculate(double c, int d)
    {
       
        cout<<"area of triangle is "<<c * c * 0.5 <<endl;
    }

    void calculate(int e)
    {
   
        cout<<"area of circle is :"<<  e * e * 3.14 <<endl;
    }
};

int main()
{
   Find f;

   f.calcualte(10,20);
   f.calcualte(10.0,5);
   f.calcualte(10,0);
   
    return 0;
}