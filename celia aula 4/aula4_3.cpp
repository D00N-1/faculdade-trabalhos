
#include <iostream>
#include <string>
using namespace std;

int main() {

    string nome = "célia";
    string letra = "a"; 
    string sobrenome = " kouth cabral"; 

    cout << "meu nome é : " << nome << endl;
    
    cout << "nome completo " << (nome.append(sobrenome)) << endl; 
    
    cout << "tamanho " << (nome.length()) << endl;
    
    cout<<"\nPrimeira letra do nome: " <<nome[0];
    nome[0]='T'; 
    cout << "meu nome agora é : " << nome << endl;

    return 0;
}