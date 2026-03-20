#include <iostream>
using namespace std;

int main (){
    int k = 10, j = 10;

    cout << "Antes do pré-fixado: " << k << "\n";
    cout << "Durante o pré-fixado: " << ++k << "\n";
    cout << "Depois do pré-fixado: " << k << "\n";

    cout << "Antes do pós-fixado: " << j << "\n";
    cout << "Durante o pós-fixado: " << j++ 
         << " (primeiro imprime, depois incrementa)\n";
    cout << "Depois do pós-fixado: " << j << "\n";

    return 0;
}