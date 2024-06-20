#include <iostream> 
using namespace std;
inline int mul(int a, int b)
{
    return a*b;
}

inline int cube(int c)
{
    return c*c*c;
}

int main()
{
    int a,b;
    int c;

    cout<<"enter the number 1 :";
    cin>>a;

    cout<<"enter the number 2 :";
    cin>>b;

    float multi = mul(a,b);

    cout<<"multiplication of two number is :"<<multi<<endl;

    cout<<"enter the number of find cubic values :";
    cin>>c;

    float cubic = cube(c);
    cout<<"cube of given number is :"<<cubic;
    
    return 0;

}