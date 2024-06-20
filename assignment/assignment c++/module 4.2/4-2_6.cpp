#include <iostream>
using namespace std;

class Cricketer
{

};

class Batsman : public Cricketer
{
    public:
    int total_runs;
    float avg_runs;
    int best_performance;

    public:

    void inputdata()
    {
        cout<<"enter total run :";
        cin>>total_runs;

        calculate_average_runs();


        cout<<"enter best performance :";
        cin>>best_performance;

        // calculate_average_runs();

    }

    void calculate_average_runs()
    {
        float match;
        cout<<"enter total match :";
        cin>>match;

        avg_runs =total_runs / match;
    }

    void displaydata()
    {
        cout<<"total runs of that team is :"<<total_runs<<endl;
        cout<<"average of runs is :"<<avg_runs<<endl;
        cout<<"best performance is "<<best_performance<<endl;
    }

};

int main()
{
    Batsman bat;
    bat.inputdata();
    bat.displaydata();

    return 0;
}