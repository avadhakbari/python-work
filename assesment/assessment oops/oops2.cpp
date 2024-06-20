#include <iostream>
#include <string>
using namespace std;

int main()
{
  
   string name;
   int choice;
   int fav;
   int qut;
   int total;

   cout<<"enter your name :";
   cin>>name;

   cout<<"Hello " <<name<<"\n";

    cout<<"------------- MENU ---------------\n";

    cout<<"1) Pizzas\n";
    cout<<"2) Burgers\n";
    cout<<"3) Sandwich\n";
    cout<<"4) Rolls\n";
    cout<<"5) Biryani\n";
    
    cout<<"-----------------------------------\n";

    cout<<"enter your choice :";
    cin>>choice;

    cout<<"-----------------------------------\n";

    switch(choice)
    {
        case 1:
        cout<<"1) Margreta Pizza : 150\n";
        cout<<"2) seven cheesi Pizza : 250\n";
        cout<<"3) onion pizza : 175\n";

        cout<<"-----------------------------------\n";
        
         cout<<"which one do you have :";
         cin>>fav;

         cout<<"enter your quentity :";
         cin>>qut;

        cout<<"-----------------------------------\n";
 
           switch(fav)
           {
                case 1:
                total = 150 * qut;
                cout<<"margreta pizza \n";
                cout<<"your bill is :"<<total<<"\n";
                cout<<"your order will be dilivered in 40 min\n";
                cout<<"thank you for ordering food\n";
              
                break;

                case 2:
                total = 250 * qut;
                cout<<"seven cheesi pizza \n";
                cout<<"your bill is :"<<total<<"\n";
                cout<<"your order will be dilivered in 40 min\n";
                cout<<"thank you for ordering food\n";
                break;

                case 3:
                total = 175 * qut; 
                cout<<"onion pizza \n";
                cout<<"your bill is :"<<total<<"\n";
                cout<<"your order will be dilivered in 40 min\n";
                cout<<"thank you for ordering food\n";
                break;

                default :
                cout<<"enter valid number ";
               
            }
            break;

        case 2:
        cout<<"1) veg burger : 75\n";
        cout<<"2) onion burger : 100\n";
        cout<<"3) peri peri buger : 125\n";

        cout<<"-----------------------------------\n";
    
        cout<<"which one do you have :";
        cin>>fav;

        cout<<"enter your quentity :";
        cin>>qut;

        cout<<"-----------------------------------\n";
 
           switch(fav)
           {
                case 1:
                total = 75 * qut;
                cout<<"margreta pizza \n";
                cout<<"your bill is :"<<total<<"\n";
                cout<<"your order will be dilivered in 40 min\n";
                cout<<"thank you for ordering food\n";
                break;

                case 2:
                total = 100 * qut;
                cout<<"seven cheesi pizza \n";
                cout<<"your bill is :"<<total<<"\n";
                cout<<"your order will be dilivered in 40 min\n";
                cout<<"thank you for ordering food\n";
                break;
                
                case 3:
                total = 125 * qut;
                cout<<"onion pizza \n";
                cout<<"your bill is :"<<total<<"\n";
                cout<<"your order will be dilivered in 40 min\n";
                cout<<"thank you for ordering food\n";
                break;

                default :
                cout<<"enter valid number ";
               
            }
            break;

        case 3:
        cout<<"1) veg sandwich : 150\n";
        cout<<"2) cheesi sandwich : 200\n";
        cout<<"3) grill sandwich : 165\n";

        cout<<"-----------------------------------\n";
        
        cout<<"which one do you have :";
        cin>>fav;

        cout<<"enter your quentity :";
        cin>>qut;

        cout<<"-----------------------------------\n";
 
            switch(fav)
            {
                case 1:
                total = 150 * qut;
                cout<<"veg sandwich \n";
                cout<<"your bill is :"<<total<<"\n";
                cout<<"your order will be dilivered in 40 min\n";
                cout<<"thank you for ordering food\n";
              
                break;

                case 2:
                total = 200 * qut;
                cout<<"cheesi sandwich\n";
                cout<<"your bill is :"<<total<<"\n";
                cout<<"your order will be dilivered in 40 min\n";
                cout<<"thank you for ordering food\n";
                break;

                case 3:
                total = 165 * qut;
                cout<<"grill sandwich \n";
                cout<<"your bill is :"<<total<<"\n";
                cout<<"your order will be dilivered in 40 min\n";
                cout<<"thank you for ordering food\n";
                break;

                default :
                cout<<"enter valid number ";
               
            }
            break;

        case 4:
        cout<<"1) zini roll : 200\n";
        cout<<"2) sev roll : 150\n";
        cout<<"3) chilli roll : 135\n";
        
        cout<<"-----------------------------------\n";

        cout<<"which one do you have :";
        cin>>fav;

        cout<<"enter your quentity :";
        cin>>qut;

        cout<<"-----------------------------------\n";
 
           switch(fav)
           {
                case 1:
                total = 200 * qut;
                cout<<"zini roll \n";
                cout<<"your bill is :"<<total<<"\n";
                cout<<"your order will be dilivered in 40 min\n";
                cout<<"thank you for ordering food\n";
              
                break;

                case 2:
                total = 150 * qut;
                cout<<"sev roll  \n";
                cout<<"your bill is :"<<total<<"\n";
                cout<<"your order will be dilivered in 40 min\n";
                cout<<"thank you for ordering food\n";
                break;

                case 3:
                total = 135 * qut;
                cout<<"chilli roll  \n";
                cout<<"your bill is :"<<total<<"\n";
                cout<<"your order will be dilivered in 40 min\n";
                cout<<"thank you for ordering food\n";
                break;

                default :
                cout<<"enter valid number ";
               
            }
            break;

        case 5:
        cout<<"1) veg biriyani : 250\n";
        cout<<"2) chilli biriyani : 230\n";
        cout<<"3) cheesi biriyani : 310\n";
        
        cout<<"-----------------------------------\n";

        cout<<"which one do you have :";
        cin>>fav;

        cout<<"enter your quentity :";
        cin>>qut;

        cout<<"-----------------------------------\n";
 
           switch(fav)
           {
                case 1:
                total = 250 * qut;
                cout<<"veg biriyani \n";
                cout<<"your bill is :"<<total<<"\n";
                cout<<"your order will be dilivered in 40 min\n";
                cout<<"thank you for ordering food\n";
              
                break;

                case 2:
                total = 230 * qut;
                cout<<" chilli biriyani  \n";
                cout<<"your bill is :"<<total<<"\n";
                cout<<"your order will be dilivered in 40 min\n";
                cout<<"thank you for ordering food\n";
                break;

                case 3:
                total = 310 * qut;
                cout<<"cheesi biriyani  \n";
                cout<<"your bill is :"<<total<<"\n";
                cout<<"your order will be dilivered in 40 min\n";
                cout<<"thank you for ordering food\n";
                break;

                default :
                cout<<"enter valid number ";
               
            }
            
            default:
            cout<<"choose your valid food";
    }
    

return 0;
}