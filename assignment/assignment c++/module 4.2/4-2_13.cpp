#include <iostream>
using namespace std;

class Number {
private:
    int num;
public:
    Number(int n) : num(n) {}

    friend void swapNumbers(Number &a, Number &b);
    
    void display() {
        cout << "Number: " << num << endl;
    }
};

void swapNumbers(Number &a, Number &b) {
    a.num = a.num + b.num;      //10 = 10 + 20 a=30
    b.num = a.num - b.num;      //20 = 30 - 20 b=10 
    a.num = a.num - b.num;      //30 = 30 - 10  a=20
}

int main() {
    int num1, num2;
    cout << "Enter number 1: ";
    cin >> num1;
    cout<<"enter number 2: ";
    cin>>num2;

    Number n1(num1);
    Number n2(num2);

    cout << "Before swapping:" << endl;
    n1.display();
    n2.display();

    swapNumbers(n1, n2);

    cout << "After swapping:" << endl;
    n1.display();
    n2.display();

    return 0;
}
