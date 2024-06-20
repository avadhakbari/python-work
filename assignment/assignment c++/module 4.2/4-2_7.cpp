#include <iostream>
using namespace std;

class Person
{
    public:
    char name[50];
    int age;

    public:
    void readdata()
    {
        cout<<"enter name :";
        cin>>name;

        cout<<"enter age :";
        cin>>age;
    }

    void writedata()
    {
        cout<<"your name is :"<<name<<endl;
        cout<<"your age is :"<<age<<endl;
    }

};

class Student : public Person
{
    public:
    float precentage;

    public:
    void readdata()
    {
        cout<<"enter your precentage :";
        cin>>precentage;
    }

    void writedata()
    {
        cout<<"your precentage is :"<<precentage;
    }

};

class Teacher : public Person
{
    public:
    float salary;

    public:
    void readdata()
    {
        cout<<"enter your salary :";
        cin>>salary;
    }

    void writedata()
    {
        cout<<"your salary is :"<<salary;
    }
};

int main()
{
    Person p;
    Student s;
    Teacher t;

    cout<<"enter your Person details :"<<endl;
    p.readdata();

    cout<<"enter your student details :"<<endl;
    s.readdata();

    cout<<"enter your teacher details :"<<endl;
    t.readdata();

    cout<<" yours details is"<<endl;
    p.writedata();
    s.writedata();
    t.writedata();

    return 0;
}
