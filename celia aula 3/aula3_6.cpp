#include <iostream>
using namespace std;
#define PRECO 1.99 

int main() {
 
    int quantidade;
    char qualidade;
    float peso;
    bool dia;
    quantidade = 3;
    qualidade = 'A';
    peso = 0.653;
    dia = true;

    cout << "Quantidade     : " << quantidade << endl;
    cout << "Qualidade      : " << qualidade << endl;
    cout << "Peso           : " << peso << endl;
    cout << "Dia            : " << dia << endl;
    cout << "Preço          : " << PRECO << endl;
    return 0;
}