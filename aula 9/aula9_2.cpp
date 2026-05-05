#include <iostream>
#include<string>
using namespace std;

struct pessoa {
    string nome;
    int idade;
    float altura;
};

int main() {
    pessoa p;

    cout << "digite o nome: ";
    getline(cin, p.nome);

    cout << "digite a idade:";
    cin >> p.idade;

    cout << "digite a altura (em metros): ";
    cin >> p.altura;

    cout << "\nDados da pessoa:\n";
    cout << "Nome: " << p.nome << endl;
    cout << "Idade: " << p.idade << " anos" << endl;
    cout << "Altura: " << p.altura << " m" << endl;

    return 0;
}