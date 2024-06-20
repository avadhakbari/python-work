#include <iostream>
using namespace std;

class Test
{
private:
    int x, y;

public:
    void input()
    {
        cout << "enter the number 1 :";
        cin >> x ;
        cout<<"enter the number 2: ";
        cin>>y;
    }
    friend void find(Test t);
};

void find(Test t)
{
    if (t.x > t.y)
    {
        cout << "largest is :" << t.x;
    }
    else
    {
        cout << "largest is " << t.y;
    }
}
int main()
{
    Test t;
    t.input();
    find(t);
    return 0;
}