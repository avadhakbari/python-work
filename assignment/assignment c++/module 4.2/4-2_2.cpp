#include <iostream>
#include <string>
using namespace std;

class BankAccount
{
    public:

    string depositerName;
    int accountNumber;
    string typeofAccount;
    float balancneAmount;

    BankAccount(string name, int number, string type, float balance)
    {
        depositerName=name;
        accountNumber=number;
        typeofAccount=type;
        balancneAmount=balance;
    }

    void display()
    {
        cout<<"depositer name is "<<depositerName<<endl;
        cout<<"their account number is "<<accountNumber<<endl;
        cout<<"their account type is "<<typeofAccount<<endl;
        cout<<"their balance amount is "<<balancneAmount<<endl;
    }

    void assign(int a)
    {
        cout<<"assign value is "<<a;
    }

    void deposited(float b)
    {
        cout<<b <<"this amount is deposite in account"; 
    }
    
    void chekingBalance(float c)
    {
        cout<<"balance after withdraw is :"<<balancneAmount - c;
    }

    void nameBalance()
    {
        cout<<"depositer name is :"<<depositerName<<endl;
        // chekingBalance();

    }
    
};

int main()
{

    int a;
    float b,c;

    BankAccount bank("avadh", 2055126522641, "saving", 8595.25);

   bank.display();

   int num;
   cout<<"---------------------"<<endl;
   cout<<"choose number"<<endl;
   cout<<"asign value : 1"<<endl;
   cout<<"deposited in amount : 2"<<endl;
   cout<<"withdraw an amount after cheking balance : 3"<<endl;
   cout<<"display name and balance : 4"<<endl;
   cout<<"---------------------"<<endl;
   
   cout<<"enter number :";
   cin>>num;
   cout<<"-----------------------"<<endl;

   switch(num)
   {
    case 1:
    cout<<"enter number for assign value";
    cin>>a;
    bank.assign(a);
    break;

    case 2:
    cout<<"enter amount for deposite :";
    cin>>b;
    bank.deposited(b);
    break;

    case 3:
    cout<<"enter amount for withdraw ";
    cin>>c;
    bank.chekingBalance(c);
    break; 

    case 4:
    bank.nameBalance();
    bank.chekingBalance(c);
    break;

    default :
    cout<<"please enter valid number ";
   }

    return 0;
}