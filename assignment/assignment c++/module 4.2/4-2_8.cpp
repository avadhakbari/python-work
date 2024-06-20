#include <iostream>
using namespace std;

class Student 
{
  protected:
    int rollNumber;
  public:
    void setRollNumber(int roll)
    {
        rollNumber = roll;
    }
    int getRollNumber()
    {
        return rollNumber;
    }
};

class Test : public Student
{
  protected:
    int subject1Marks;
    int subject2Marks;
  public:
    void setMarks(int sub1, int sub2) 
    {
        subject1Marks = sub1;
        subject2Marks = sub2;
    }
    void displayMarks() 
    {
        cout << "Marks in Subject 1: " << subject1Marks << endl;
        cout << "Marks in Subject 2: " << subject2Marks << endl;
    }
};

class Result : public Test 
{
  private:
    int totalMarks;
  public:
    void calculateTotal() 
    {
        totalMarks = subject1Marks + subject2Marks;
    }
    void displayResult() 
    {
        cout << "Roll Number: " << getRollNumber() << endl;
        displayMarks();
        cout << "Total Marks: " << totalMarks << endl;
    }
};

int main() 
{
    Result studentResult;

    
    studentResult.setRollNumber(101);

    studentResult.setMarks(85, 90);

    studentResult.calculateTotal();
    studentResult.displayResult();

    return 0;
}
