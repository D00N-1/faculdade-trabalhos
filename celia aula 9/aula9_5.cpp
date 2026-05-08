#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<string> fila;

    
    fila.push("joao");
    fila.push("maria");
    fila.push("carlos");

    cout <<"Primeiro da fila: " << fila.front() << endl; 

 
    fila.pop();
    cout << "agora o primeiro da fila: " << fila.front() << endl; 

    // Verificando o tamanho da fila
    cout << "Tamanho da fila: " << fila.size() << endl; // 2

    return 0;
}   