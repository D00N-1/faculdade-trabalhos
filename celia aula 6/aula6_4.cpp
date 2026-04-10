#include <iostream>
using namespace std;
int main(){
    char continua;
    continua = 's';
    char continua1;
    continua1 = 'S';

    while (continua1 == 'S') { 
       cout << "Repetindo....\n";
       cout << "Tecle 'S' se deseja continuar ou outra tecla";
       cout << "para parar\n";
       cin >> continua1;
    }

    while (continua == 's') { 
       cout << "Repetindo....\n";
       cout << "Tecle 's' se deseja continuar ou outra tecla";
       cout << "para parar\n";
       cin >> continua;
    }
}